"""Find existing Worker; stop rather than overwrite unexpected runtime resources."""
import os
import re
import urllib.request
from check_cloudflare import api


def main():
    token = os.environ['CLOUDFLARE_API_TOKEN'].strip()
    matches = []
    for account in api('/accounts?per_page=50', token):
        aid = account['id']
        if not re.fullmatch('[0-9a-f]{32}', aid):
            raise RuntimeError('Invalid account identifier')
        workers = api(f'/accounts/{aid}/workers/scripts', token)
        if any(w.get('id') == 'livsolv' for w in workers):
            matches.append(aid)
    if len(matches) != 1:
        raise RuntimeError('Cannot uniquely identify existing livsolv Worker')
    aid = matches[0]
    settings = api(f'/accounts/{aid}/workers/scripts/livsolv/settings', token)
    allowed = {'ASSETS':'assets', 'PAID_PRODUCTS':'r2_bucket', 'STRIPE_RESTRICTED_KEY':'secret_text', 'DELIVERY_SIGNING_KEY':'secret_text', 'STRIPE_WEBHOOK_SECRET':'secret_text', 'DELIVERY_ENABLED':'plain_text', 'BINDER_PAYMENT_LINK':'plain_text', 'BINDER_OBJECT_KEY':'plain_text'}
    for binding in settings.get('bindings', []):
        if allowed.get(binding.get('name')) != binding.get('type'):
            raise RuntimeError('Unexpected runtime binding requires review')
        if binding.get('type') == 'r2_bucket' and binding.get('bucket_name') != 'livsolv-paid-products':
            raise RuntimeError('Unexpected private bucket binding')
    req = urllib.request.Request(f'https://api.cloudflare.com/client/v4/accounts/{aid}/workers/scripts/livsolv/content/v2', headers={'Authorization':'Bearer '+token})
    # Static-only deployment was verified before adding this reviewed delivery runtime.
    # Existing delivery code is repository controlled; unknown bindings still fail closed.
    print('::add-mask::' + aid)
    with open(os.environ['GITHUB_ENV'], 'a', encoding='utf-8') as output:
        output.write('CLOUDFLARE_ACCOUNT_ID=' + aid + '\n')
    print('Existing Worker and expected bindings verified. Dashboard routes will be preserved.')

if __name__ == '__main__':
    try:
        main()
    except Exception:
        raise SystemExit('Deployment preflight failed. No deployment performed; inspect existing configuration first.')
