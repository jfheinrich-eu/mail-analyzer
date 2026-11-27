<p align="center">
  <img src="assets/social-media-preview-compress.png" alt="Mail Analyzer social media preview" width="700">
</p>

# Mail Analyzer

Read-only Outlook Mailbox Analysis.

## Status

Early Development

## Security

The application only requires:

- User.Read
- Mail.Read
- offline_access

No mail modification permissions.

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest
```
