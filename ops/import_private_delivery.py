"""Decrypt the one-time CMS envelope inside CI and put files only in private R2."""
import hashlib,json,os,pathlib,subprocess,tempfile,urllib.request,zipfile
from check_cloudflare import api
EXPECTED='163a38bf381a622c7c18ff8d1da6f2382ca17b53fff7b110a5566115077e5388'
def main():
 token=os.environ['CLOUDFLARE_API_TOKEN'].strip();aid=os.environ['CLOUDFLARE_ACCOUNT_ID'];bucket='livsolv-paid-products'
 base=f'/accounts/{aid}/r2/buckets/{bucket}/domains/'
 if api(base+'managed',token).get('enabled') is not False or api(base+'custom',token).get('domains'):
  raise RuntimeError('Storage is not private')
 envelope=pathlib.Path('ops/private-transfer.cms')
 if hashlib.sha256(envelope.read_bytes()).hexdigest()!=EXPECTED:raise RuntimeError('Envelope hash mismatch')
 def command(args):
  p=subprocess.run(args,capture_output=True)
  if p.returncode:raise RuntimeError('Private file operation failed')
 with tempfile.TemporaryDirectory() as tmp:
  private=tmp+'/private.pem';payload=tmp+'/payload.zip'
  command(['npx','wrangler','r2','object','get',bucket+'/internal/transfer-private.pem','--file',private,'--remote'])
  command(['openssl','cms','-decrypt','-binary','-inform','DER','-in',str(envelope),'-inkey',private,'-out',payload])
  with zipfile.ZipFile(payload) as z:
   if set(z.namelist())!={'approved-binder-v8.pdf','calculator-v2.xlsx','runtime-secrets.json'}:raise RuntimeError('Unexpected envelope contents')
   for name,obj in [('approved-binder-v8.pdf','staging/approved-binder-v8.pdf'),('calculator-v2.xlsx','staging/calculator-v2.xlsx')]:
    data=z.read(name);p=pathlib.Path(tmp)/name;p.write_bytes(data)
    command(['npx','wrangler','r2','object','put',bucket+'/'+obj,'--file',str(p),'--remote'])
    downloaded=str(p)+'.verified';command(['npx','wrangler','r2','object','get',bucket+'/'+obj,'--file',downloaded,'--remote'])
    if hashlib.sha256(data).digest()!=hashlib.sha256(pathlib.Path(downloaded).read_bytes()).digest():raise RuntimeError('Private object verification failed')
   secret=json.loads(z.read('runtime-secrets.json'))['STRIPE_WEBHOOK_SECRET']
   if not secret.startswith('whsec_'):raise RuntimeError('Webhook secret format invalid')
   body=json.dumps({'name':'STRIPE_WEBHOOK_SECRET','text':secret,'type':'secret_text'}).encode()
   req=urllib.request.Request(f'https://api.cloudflare.com/client/v4/accounts/{aid}/workers/scripts/livsolv/secrets',data=body,method='PUT',headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
   with urllib.request.urlopen(req,timeout=30) as r:
    if not json.load(r).get('success'):raise RuntimeError('Webhook secret installation failed')
  # Destroy the temporary decryption key after successful import.
  command(['npx','wrangler','r2','object','delete',bucket+'/internal/transfer-private.pem','--remote'])
 print('PASS: approved binder PDF and calculator uploaded privately and SHA-256 verified after download.')
 print('PASS: webhook signing secret installed; temporary transfer private key deleted.')
 print('Files remain in staging. No customer ZIP released; checkout and download gate remain paused.')
if __name__=='__main__':
 try:main()
 except Exception:raise SystemExit('Private import failed. No credentials or file contents logged. Checkout remains paused.')
