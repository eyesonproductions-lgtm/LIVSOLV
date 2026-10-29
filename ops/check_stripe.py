"""Read-only Stripe credential check. Never logs secrets or customer records."""
import json, os, sys, urllib.request, urllib.error
key = os.environ.get("STRIPE_RESTRICTED_KEY", "").strip()
if not key:
    sys.exit("STRIPE_RESTRICTED_KEY is missing or empty.")
if key.startswith("rk_test_"):
    sys.exit("The saved key is a TEST restricted key. A live restricted key is required for existing live purchases. No request made.")
if not key.startswith("rk_live_"):
    sys.exit("The saved value is not a recognized live restricted key. No value or prefix logged; no request made.")
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
