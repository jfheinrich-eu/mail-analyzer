---
name: review
description: Review current changes or the complete clean Mail Analyzer repository for engineering defects without modifying files.
disable-model-invocation: true
---
Perform an engineering review of Mail Analyzer without modifying files.

## Scope

1. Inspect Git status, staged and unstaged diffs, and untracked files.
2. Review current changes and their impact when the worktree is dirty; otherwise review the repository.
3. Read complete relevant untracked files and apply repository instructions.

## Review criteria

Review for:

- correctness, regressions, architecture, maintainability, and CLI behavior;
- read-only access guarantees and least-privilege Microsoft Graph scopes;
- OAuth token handling, secret exposure, and privacy of mailbox contents;
- robust handling of API errors, pagination, retries, timeouts, and malformed or large responses;
- SQLAlchemy usage, query safety, data validation, and persistence behavior;
- Python 3.12 compatibility, packaging, typing, tests, dependency consistency, and CI;
- documentation accuracy and agreement with implemented behavior.

Distinguish confirmed defects from suggestions. Do not expose token values or personal data.

## Verification

Run safe checks and focused tests when appropriate. Do not modify files or claim a check passed unless it ran successfully.

## Output

Report only actionable findings by P0 through P3 severity. Include exact file and line, evidence, impact, and a recommended correction. Then list open questions, checks performed and omitted, and residual test gaps. If there are no findings, say so explicitly.
