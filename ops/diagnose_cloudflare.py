"""Read-only diagnosis. Emit classifications only, never raw configuration or logs."""
import hashlib
import json
import os
import re
import urllib.request
from check_cloudflare import api


def main():
    token = os.environ['CLOUDFLARE_API_TOKEN'].strip()
    accounts = api('/accounts?per_page=50', token)
    matches = []
    for a in accounts:
        aid = a['id']
        if not re.fullmatch('[0-9a-f]{32}', aid):
            raise RuntimeError('Invalid account identifier')
        for worker in api(f'/accounts/{aid}/workers/scripts', token):
            if worker.get('id') == 'livsolv':
                matches.append((aid, worker))
    if len(matches) != 1:
        raise RuntimeError('Expected exactly one livsolv Worker')
    aid, worker = matches[0]
    settings = api(f'/accounts/{aid}/workers/scripts/livsolv/settings', token)
    print('Worker exists: livsolv')
    print('Worker settings fields:', ', '.join(sorted(k for k in settings if re.fullmatch('[a-z_]+', k))))
    print('Assets configuration present:', bool(settings.get('assets')))
    print('Runtime binding count:', len(settings.get('bindings', [])))
    # Do not print Worker source: a legacy deployment may embed private links.
    try:
        request = urllib.request.Request(f'https://api.cloudflare.com/client/v4/accounts/{aid}/workers/scripts/livsolv/content/v2', headers={'Authorization':'Bearer '+token})
        with urllib.request.urlopen(request, timeout=20) as response:
            raw = response.read(20_000_000)
        text = raw.decode('utf-8', errors='replace')
        print('Existing runtime bytes:', len(raw))
        print('Existing runtime SHA256:', hashlib.sha256(raw).hexdigest())
        print('Runtime classification:', json.dumps({
            'hello_world_marker': 'Hello World' in text,
            'github_proxy_marker': 'raw.githubusercontent.com' in text,
            'assets_fetch_marker': 'ASSETS.fetch' in text,
            'stripe_marker': 'stripe' in text.lower(),
            'drive_marker': 'drive.google.com' in text,
        }))
    except Exception:
        print('Runtime content inspection unavailable; no source was printed.')
    tag = worker.get('tag', '')
    if re.fullmatch('[a-zA-Z0-9_-]+', tag):
        try:
            builds = api(f'/accounts/{aid}/builds/workers/{tag}/builds', token)
            if isinstance(builds, dict):
                builds = builds.get('builds', builds.get('items', []))
            print('Build records returned:', len(builds))
            for build in builds[:2]:
                bid = build.get('build_uuid', '')
                if not re.fullmatch('[a-zA-Z0-9_-]+', bid):
                    continue
                logs = api(f'/accounts/{aid}/builds/builds/{bid}/logs', token)
                text = json.dumps(logs).lower()
                patterns = ['missing entry-point', 'missing entry point', 'assets directory', 'authentication error', 'permission denied', 'wrangler.json', 'could not resolve', 'no such file', 'error 10000']
                print('Build error classifications:', json.dumps({p:p in text for p in patterns}))
        except RuntimeError as e:
            print('Build-log API access:', str(e))
    for path in ['systems-down-household-binder.html', 'purchase-complete-7f4c9.html', 'index.html']:
        try:
            req = urllib.request.Request('https://livsolv.com/'+path, headers={'User-Agent':'LIVSOLV-owner-deployment-check'})
            with urllib.request.urlopen(req, timeout=20) as response:
                text = response.read(2_000_000).decode('utf-8')
                code = response.status
            local = open(path, encoding='utf-8').read()
            print('Public page:', path, 'HTTP:', code, 'matches repository:', text == local, 'Stripe checkout present:', 'buy.stripe.com/' in text, 'Drive download present:', 'drive.google.com' in text)
        except Exception:
            print('Public page check unavailable:', path)

if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, KeyError):
        raise SystemExit('Diagnosis could not complete; no private response data was logged.')
