# Remaining private-delivery work

Updated 2026-10-29. Website deployment is repaired. Paid checkout remains paused; this document is not a claim that delivery works.

## Access already verified

- GitHub repository writes and Actions runs.
- Cloudflare account-scoped token in Actions secret CLOUDFLARE_API_TOKEN; read access and a real Worker deployment succeeded.
- ChatGPT Stripe connector can manage the live LIVSOLV account. It is not a runtime credential that can be exported for the website.

## Remaining access, stated together

1. Existing Cloudflare token needs Account / Workers R2 Storage / Edit for private bucket provisioning and uploads. Keep it restricted to the LIVSOLV account. Do not grant DNS, billing or user-management permissions. Check whether R2 is already enabled before attempting any activation that requires accepting billing terms; do not assume paid services are authorized.
2. Website runtime needs a dedicated restricted Stripe API key. Use Checkout Sessions Read for purchase validation; automate webhook endpoint registration separately through the connected Stripe account. Store any runtime key and webhook signing secret only in encrypted runtime secrets, not source or chat. Verify exact API permissions in test before selecting the production key. The current Cloudflare key cannot substitute for this.

## Remaining implementation and launch gate

- Recover the current approved package privately. Approved review v8 and calculator v2 were located and copied locally. Earlier Digital Package and v2 REVIEW PACKAGE were also recovered but are superseded review materials, not interchangeable with the approved final binder. Verify the package contents without redesigning it or claiming outdated editions are final.
- Prepare private file transfer and storage without any permanent public URL or paid PDF/ZIP in the public repository or static upload directory.
- Implement and test signed Stripe completion and asynchronous-success webhooks, exact binder-product/payment-link validation, replay/idempotency handling, private purchase-validated downloads, expiry, failures and refunds.
- Verify Letter/A4/ink-saver and fillable marketing claims against the actual delivered package. Do not silently advertise files that are missing.
- Run a sandbox purchase, verify direct unauthenticated access is denied, then verify the approved production payment/delivery path. Reopen checkout only after all launch gates pass.

No protected-download runtime or fulfillment webhook has been deployed yet. Further owner access is required; do not report this task as complete.
