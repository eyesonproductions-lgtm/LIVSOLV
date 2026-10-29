"""Verify public deployed bytes without logging private links or page contents."""
from pathlib import Path
import time
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
PAGES = ['index.html', 'systems-down-household-binder.html', 'purchase-complete-7f4c9.html', 'car-battery-inverter-backup-power.html']


def main():
    for attempt in range(6):
        failures = []
        for path in PAGES:
            try:
                req = urllib.request.Request('https://livsolv.com/' + path + '?deployment-check=20261029', headers={'Cache-Control':'no-cache','User-Agent':'LIVSOLV-owner-deployment-check'})
                with urllib.request.urlopen(req, timeout=15) as response:
                    actual = response.read(2_000_000)
                if actual != (ROOT / path).read_bytes():
                    failures.append(path)
            except Exception:
                failures.append(path)
        if not failures:
            print('Verified public bytes match the deployed commit on four key pages. Checkout remains paused.')
            return
        if attempt < 5:
            time.sleep(5)
    raise SystemExit('Public verification did not match the commit: ' + ', '.join(failures))

if __name__ == '__main__':
    main()
