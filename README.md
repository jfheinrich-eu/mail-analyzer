<p align="center">
  <img src="assets/social-media-preview-compress.png" alt="Mail Analyzer social media preview" width="700">
</p>

# Mail Analyzer

Read-only Outlook Mailbox Analysis.

## Status

Early Development

Only the `health` command is currently implemented. Outlook authentication and mailbox analysis are not available yet.

## Security

Currently, the application implements only the `health` command; it does not authenticate to Outlook or access mailbox data.

No software can guarantee that access will never be compromised. Before mailbox access is implemented, it must use defense-in-depth controls:

- Request only delegated read-only Microsoft Graph scopes:
  - User.Read
  - Mail.Read
  - offline_access
- Protect any persistent token cache with operating-system access controls; never log or commit tokens, credentials, or mailbox content.
- Use HTTPS with certificate validation, fixed trusted Graph endpoints, request timeouts, and response-size limits.
- Treat messages, attachments, filenames, and API responses as untrusted; validate inputs and never execute attachments.
- Use parameterized database queries and safely escape rendered report content.

These controls reduce risk but cannot eliminate compromise. They are requirements for future mailbox functionality, not claims that unimplemented access paths are already protected. The CI workflow blocks on Bandit source scans and `pip-audit` vulnerability checks against the resolved runtime, development, and build-tool dependency set.

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest
```
