# Private delivery remaining work

Access setup is complete. Stripe session read and private R2 access are verified. Runtime Stripe, download signing and webhook secrets are installed. No additional owner credential is currently required.

The reviewed runtime and signed webhook handler are deployed. Downloads remain disabled and Stripe checkout remains paused.

1. Assemble and verify the final ZIP using the approved v8 binder, not an older review ZIP. Reconcile all advertised components and editions. The approved PDF is printable, not an interactive fillable form; correct the sales claim.
2. Upload the validated customer ZIP privately. Current private staging contains approved v8 and the calculator only.
3. Run a complete purchase/webhook/download test, including failed payment and anonymous denial. Mocked tests and configuration probes do not establish a successful end-to-end purchase.
4. Enable the delivery gate and checkout only after those checks pass. Verify the deployed sales and confirmation pages afterward.

The one-time encrypted import file is removed after successful import; its private decryption key has been deleted. Do not upload paid plaintext files or secrets into this public repository.
