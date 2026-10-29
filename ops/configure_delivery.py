"""Install write-only runtime secrets without printing values."""
import json, os, secrets, urllib.request
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
if __name__=='__main__':
    try:main()
    except Exception:raise SystemExit('Private delivery configuration failed. No secret or provider response logged.')
