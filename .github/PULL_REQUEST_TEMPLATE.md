# Summary

Describe the user problem, the focused change, and its impact.

## Verification

List the exact commands and manual checks that were run, with their results. Explain any relevant checks that were not run.

## Risks and privacy

Describe relevant compatibility, authentication, Microsoft Graph permission, data handling, and security risks. State whether the change preserves read-only mailbox access. Write `None identified` only after checking them.

## Checklist

- [ ] The change is focused and contains no generated output.
- [ ] Tests cover changed behavior and use synthetic or mocked mailbox data.
- [ ] Relevant tests and checks were run, or omissions are explained.
- [ ] Documentation reflects the implemented behavior.
- [ ] No credentials, access tokens, mailbox contents, or other personal data were added.
- [ ] The change does not add mail-modification behavior or broaden Microsoft Graph permissions without an explicit requirement.
- [ ] Dependency changes are necessary and reflected in `pyproject.toml`.
