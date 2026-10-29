"""Install write-only runtime secrets and create a temporary private file-transfer key."""
import base64, json, os, secrets, subprocess, tempfile, urllib.request
from check_cloudflare import api

def main():
    token=os.environ['CLOUDFLARE_API_TOKEN'].strip()
    aid=os.environ['CLOUDFLARE_ACCOUNT_ID']
    key=os.environ['STRIPE_RESTRICTED_KEY'].strip()
    if not key.startswith('rk_live_'): raise RuntimeError('Live restricted Stripe key missing')
    def put_secret(name,value):
        payload=json.dumps({'name':name,'text':value,'type':'secret_text'}).encode()
        req=urllib.request.Request(f'https://api.cloudflare.com/client/v4/accounts/{aid}/workers/scripts/livsolv/secrets',data=payload,headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'},method='PUT')
        with urllib.request.urlopen(req,timeout=30) as r:
            if not json.load(r).get('success'):raise RuntimeError('Secret installation rejected')
    put_secret('STRIPE_RESTRICTED_KEY',key)
    names={s['name'] for s in api(f'/accounts/{aid}/workers/scripts/livsolv/secrets',token)}
    if 'DELIVERY_SIGNING_KEY' not in names:put_secret('DELIVERY_SIGNING_KEY',secrets.token_urlsafe(48))
    print('Runtime Stripe verification and download-signing secrets installed. Values omitted.')
    # Only the public certificate is emitted. The matching private key stays in private R2.
    with tempfile.TemporaryDirectory() as tmp:
        private=tmp+'/key.pem';cert=tmp+'/certificate.pem'
        result=subprocess.run(['openssl','req','-x509','-newkey','rsa:3072','-keyout',private,'-out',cert,'-sha256','-days','7','-nodes','-subj','/CN=LIVSOLV Private Transfer'],capture_output=True)
        if result.returncode:raise RuntimeError('Transfer certificate generation failed')
        for path,obj in [(private,'internal/transfer-private.pem'),(cert,'internal/transfer-certificate.pem')]:
            r=subprocess.run(['npx','wrangler','r2','object','put','livsolv-paid-products/'+obj,'--file',path,'--remote'],capture_output=True)
            if r.returncode:raise RuntimeError('Private transfer key storage failed')
        print('PUBLIC_TRANSFER_CERTIFICATE_BASE64='+base64.b64encode(open(cert,'rb').read()).decode())
        print('Temporary transfer private key stored only in private storage. No customer files uploaded.')
if __name__=='__main__':
    try:main()
    except Exception:raise SystemExit('Private delivery configuration failed. No secret or provider response logged.')
