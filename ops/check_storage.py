"""Read-only R2 access check. Never emit token, account IDs or bucket names."""
import json
import os
import re
import urllib.error
import urllib.request
from check_cloudflare import api

def main():
    token = os.environ["CLOUDFLARE_API_TOKEN"].strip()
    matches = []
    for account in api("/accounts?per_page=50", token):
        aid = account["id"]
        if not re.fullmatch("[0-9a-f]{32}", aid):
            raise RuntimeError("Invalid account identifier")
        workers = api(f"/accounts/{aid}/workers/scripts", token)
        if any(w.get("id") == "livsolv" for w in workers):
            matches.append(aid)
    if len(matches) != 1:
        raise RuntimeError("Cannot uniquely identify LIVSOLV account")
    request = urllib.request.Request(
        "https://api.cloudflare.com/client/v4/accounts/" + matches[0] + "/r2/buckets",
        headers={"Authorization": "Bearer " + token, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = json.load(response)
    except urllib.error.HTTPError as error:
        try:
            data = json.load(error)
        except ValueError:
            data = {}
        codes = [e.get("code") for e in data.get("errors", []) if isinstance(e.get("code"), int)]
        print("R2 access check: HTTP", error.code, "Cloudflare error codes:", codes)
        if 10042 in codes:
            print("R2 activation is required in the owner dashboard. No activation or billing change was attempted.")
        raise SystemExit(1)
    if not data.get("success"):
        raise RuntimeError("R2 API rejected the request")
    print("R2 storage access verified: bucket listing succeeded.")
    print("Existing bucket count:", len(data.get("result", {}).get("buckets", [])))
    print("No storage, billing, access permissions or checkout settings were changed.")
    print("Write permission and paid delivery are not yet verified.")

if __name__ == "__main__":
    try:
        main()
    except (KeyError, RuntimeError):
        raise SystemExit("R2 access could not be verified. No private response data was logged.")
