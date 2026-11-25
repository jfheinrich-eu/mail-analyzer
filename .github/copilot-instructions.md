# Copilot Instructions

## Communication

- Write source code, comments, identifiers, and repository documentation in English.
- Respond in the user's language unless they ask otherwise.
- Use concise technical language. Do not invent requirements or claim checks that were not run.

## Project

- Mail Analyzer is a Python 3.12+ command-line application for read-only Outlook mailbox analysis.
- The package uses the `src/mail_analyzer/` layout and setuptools. The CLI entry point is `mail-analyzer`.
- Keep mailbox access read-only. Do not add operations that send, modify, move, or delete mail, or request write permissions.
- The documented Microsoft Graph scopes are `User.Read`, `Mail.Read`, and `offline_access`. Do not broaden them without an explicit product requirement.

## Privacy and security

- Treat access tokens, token caches, credentials, mailbox contents, and personal data as sensitive. Never commit or print their values.
- Use synthetic or mocked mailbox data in tests; do not use a real mailbox for development or validation.
- Treat messages, attachments, filenames, and remote API responses as untrusted input.
- Avoid retaining mailbox data unnecessarily. Use parameterized SQLAlchemy queries and explicit input validation.
- Keep secrets and local configuration out of source control; `.env` and the token cache are local-only.

## Engineering

- Make focused changes and follow existing Python conventions and dependency pins in `pyproject.toml`.
- Preserve type safety and surface errors explicitly; avoid broad exception handling and silent fallbacks.
- Add focused tests for behavior changes. Run relevant tests and available lint/type checks; report exactly what ran.
- Keep documentation consistent with implemented behavior and the read-only product boundary.

## Git

- Do not discard user changes, rewrite history, or push without explicit approval.
- Do not commit unless asked. Never commit credentials, tokens, personal mailbox data, generated files, or local environment files.

## Repository skills

The manual-only skills under `.github/skills/` define repository workflows:

- `/review` performs an engineering review without modifying files.
- `/sec-review` performs a security review without modifying files.
- `/review-project` combines both reviews and proposes documentation updates for approval.
- `/commit` prepares atomic Conventional Commit groups and commits only approved groups.
- `/create-pr` creates and verifies a pull request when explicitly requested.
