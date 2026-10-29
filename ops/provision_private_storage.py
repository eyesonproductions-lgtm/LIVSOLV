"""Create the dedicated private bucket only; do not enable public URLs or billing."""
import json
import os
import re
import urllib.request
from check_cloudflare import api
BUCKET = "livsolv-paid-products"

def main():
    token = os.environ["CLOUDFLARE_API_TOKEN"].strip()
    matches = []
    for account in api("/accounts?per_page=50", token):
        aid = account["id"]
        if not re.fullmatch("[0-9a-f]{32}", aid):
            raise RuntimeError("Invalid account identifier")
        if any(w.get("id") == "livsolv" for w in api(f"/accounts/{aid}/workers/scripts", token)):
            matches.append(aid)
    if len(matches) != 1:
        raise RuntimeError("Cannot uniquely identify LIVSOLV account")
    aid = matches[0]
    base = f"/accounts/{aid}/r2/buckets"
    existing = api(base, token).get("buckets", [])
    if not any(b.get("name") == BUCKET for b in existing):
        req = urllib.request.Request(
            "https://api.cloudflare.com/client/v4" + base,
            data=json.dumps({"name": BUCKET}).encode(),
            headers={"Authorization":"Bearer "+token, "Content-Type":"application/json"},
            method="POST")
        with urllib.request.urlopen(req, timeout=20) as response:
            data=json.load(response)
        if not data.get("success"):
            raise RuntimeError("Bucket creation failed")
        print("Dedicated binder bucket created.")
    else:
        print("Dedicated binder bucket already exists; preserving it.")
    managed = api(base + "/" + BUCKET + "/domains/managed", token)
    custom = api(base + "/" + BUCKET + "/domains/custom", token)
    domains = custom if isinstance(custom, list) else custom.get("domains", [])
    if managed.get("enabled") is not False or domains:
        raise RuntimeError("Public-access verification did not pass; do not upload paid files")
    print("Verified: public r2.dev access is disabled and no custom public domains are attached.")
    print("No paid files uploaded. No checkout, runtime, billing or domain changes made.")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        raise SystemExit("Private-storage setup did not finish verification. No paid file was uploaded; inspect before continuing.")
