# LIVSOLV Cloudflare connection

Prepared 2026-10-29. This is a read-only connection workflow, not a completed delivery repair.

## Owner setup

1. In Cloudflare, create a custom API token named `LIVSOLV GitHub deployment`. Restrict Account Resources to the account that contains the existing `livsolv` Worker. Give **Account / Account Settings / Read** and **Account / Workers Scripts / Edit**. No DNS, billing, user-management, R2 or global-key access is needed for this first connection. Prefer a short expiration; revoke after the repair if ongoing deployment is not wanted.
2. In GitHub repository Settings > Secrets and variables > Actions, add a repository secret named `CLOUDFLARE_API_TOKEN`, with that token as its value. Never paste it into chat, source files, issues or workflow inputs. An account-scoped token lets the check discover the account. If discovery is unavailable, add `CLOUDFLARE_ACCOUNT_ID` as a second repository secret.
3. Tell the assistant the secret is saved. The assistant can trigger the check by changing `ops/cloudflare-request.txt`; alternatively run **Check LIVSOLV Cloudflare access** in GitHub Actions on main.

Only trusted main-branch source is executed. Checkout is pinned and credentials are not persisted. This workflow never runs on pull requests and prints no token, binding value or Worker source. GitHub logs in this public repository must be treated as public.

## What comes next

After the check passes, inspect and preserve the existing Worker configuration and diagnose the deployment failure before preparing a deployment workflow. Do not replace unknown runtime code, bindings or routes. A successful connection check proves read access only, not deployment permission. Do not reopen checkout until private purchase-validated delivery and a full payment/download test pass. Never put the paid bundle into public website assets or this repository.

Reference: https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/
