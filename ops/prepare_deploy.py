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
    if settings.get('bindings'):
        raise RuntimeError('Existing bindings require review before a static-only deployment')
    req = urllib.request.Request(f'https://api.cloudflare.com/client/v4/accounts/{aid}/workers/scripts/livsolv/content/v2', headers={'Authorization':'Bearer '+token})
    with urllib.request.urlopen(req, timeout=20) as response:
        if response.read(1):
            raise RuntimeError('Existing runtime code requires review before a static-only deployment')
    print('::add-mask::' + aid)
    with open(os.environ['GITHUB_ENV'], 'a', encoding='utf-8') as output:
        output.write('CLOUDFLARE_ACCOUNT_ID=' + aid + '\n')
    print('Existing static-only Worker verified. Dashboard routes and variables will be preserved.')

if __name__ == '__main__':
    try:
        main()
    except Exception:
        raise SystemExit('Deployment preflight failed. No deployment performed; inspect existing configuration first.')
