"""Read-only Stripe credential check. Never logs secrets or customer records."""
import json, os, sys, urllib.request, urllib.error
key = os.environ.get("STRIPE_RESTRICTED_KEY", "")
if not key:
    sys.exit("STRIPE_RESTRICTED_KEY is missing or empty.")
if not key.startswith("rk_live_"):
    sys.exit("Expected a live restricted Stripe key; no request made.")
req = urllib.request.Request("https://api.stripe.com/v1/checkout/sessions?limit=1", headers={"Authorization": "Bearer " + key})
try:
    with urllib.request.urlopen(req, timeout=30) as response:
        data = json.load(response)
except urllib.error.HTTPError as exc:
    sys.exit("Stripe read-only credential check failed with HTTP " + str(exc.code) + ". No response body logged.")
except Exception:
    sys.exit("Stripe credential check could not reach the provider. No sensitive details logged.")
if data.get("object") != "list" or not isinstance(data.get("data"), list):
    sys.exit("Stripe returned an unexpected response. No response body logged.")
print("PASS: live restricted key authenticated and Checkout Sessions read succeeded.")
print("No payments, refunds, checkout links or Stripe settings changed. No customer data logged.")
