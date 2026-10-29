"""Compare deployed public bytes. No credentials or page contents enter logs."""
from pathlib import Path
import hashlib
import subprocess
import time
ROOT = Path(__file__).resolve().parent.parent
PAGES = ['index.html', 'systems-down-household-binder.html', 'purchase-complete-7f4c9.html', 'car-battery-inverter-backup-power.html']


def main():
    for attempt in range(4):
        failures = []
        for path in PAGES:
            result = subprocess.run(['curl', '--fail', '--silent', '--show-error', '--location', '--max-time', '15', 'https://livsolv.com/' + path], capture_output=True)
            expected = (ROOT / path).read_bytes()
            if result.returncode:
                failures.append(path)
                print(f'{path}: request failed (curl exit {result.returncode})')
            elif result.stdout != expected:
                failures.append(path)
                print(f'{path}: content differs; received {len(result.stdout)} bytes, expected {len(expected)}; received SHA256 {hashlib.sha256(result.stdout).hexdigest()}')
            else:
                print(f'{path}: public content matches repository')
        if not failures:
            print('Verified four public pages match this commit. Checkout remains paused.')
            return
        if attempt < 3:
            time.sleep(5)
    raise SystemExit('Could not verify public content: ' + ', '.join(failures))
if __name__ == '__main__':
    main()
