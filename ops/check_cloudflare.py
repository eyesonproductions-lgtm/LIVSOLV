"""Read-only access check. Never print credentials, binding values or Worker code."""
import json
import os
import re
import sys
import urllib.error
import urllib.request

BASE = "https://api.cloudflare.com/client/v4"


def api(path, token):
    request = urllib.request.Request(BASE + path, headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = json.load(response)
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"Cloudflare returned HTTP {error.code}; check the token scope and permissions.") from None
    except (urllib.error.URLError, TimeoutError, ValueError):
        raise RuntimeError("Cloudflare could not be reached or returned an invalid response. Retry this check later.") from None
    if not data.get("success"):
        raise RuntimeError("Cloudflare rejected the request. Check token validity and permissions.")
    return data.get("result")


def select_worker(token, account_id=""):
    if account_id:
        if not re.fullmatch(r"[0-9a-f]{32}", account_id):
            raise RuntimeError("CLOUDFLARE_ACCOUNT_ID must be the 32-character account ID, not a domain or token.")
        accounts = [{"id": account_id}]
    else:
        accounts = api("/accounts?per_page=50", token)
        if not isinstance(accounts, list) or not accounts:
            raise RuntimeError("No accounts visible. Add Account Settings Read, or supply CLOUDFLARE_ACCOUNT_ID as a secret.")
    matches = []
    for account in accounts:
        identifier = account.get("id", "")
        if not re.fullmatch(r"[0-9a-f]{32}", identifier):
            raise RuntimeError("Cloudflare returned an invalid account identifier.")
        try:
            settings = api(f"/accounts/{identifier}/workers/scripts/livsolv/settings", token)
        except RuntimeError:
            if len(accounts) == 1:
                raise
            continue
        if isinstance(settings, dict):
            matches.append(settings)
    if len(matches) != 1:
        raise RuntimeError("Could not uniquely identify the livsolv Worker. Scope the token to its account or supply CLOUDFLARE_ACCOUNT_ID.")
    return matches[0]


def main():
    token = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
    if not token:
        raise RuntimeError("Add the repository Actions secret CLOUDFLARE_API_TOKEN, then run this workflow again.")
    settings = select_worker(token, os.environ.get("CLOUDFLARE_ACCOUNT_ID", "").strip())
    bindings = settings.get("bindings", [])
    # Types only: text, JSON and secret values can contain private delivery data.
    types = sorted({b.get("type", "unknown") for b in bindings})
    safe_types = [t for t in types if re.fullmatch(r"[a-z0-9_]+", t)]
    report = ("Cloudflare connection verified: livsolv Worker settings are readable.\n"
              "No deployments, files, routes, billing or access settings were changed.\n"
              "Binding types: " + (", ".join(safe_types) or "none") + ".\n"
              "Deployment permission and private automatic delivery are NOT yet verified.\n")
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as output:
            output.write("## LIVSOLV Cloudflare access\n\n" + report)


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        print("ERROR: " + str(error), file=sys.stderr)
        sys.exit(1)
