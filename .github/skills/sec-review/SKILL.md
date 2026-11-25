---
name: sec-review
description: Review current changes or the complete clean Mail Analyzer repository for security risks without modifying files.
disable-model-invocation: true
---
Perform a security-focused review of Mail Analyzer without modifying files.

## Scope

1. Inspect repository status and staged, unstaged, and untracked changes.
2. Review changed files and their security impact when the worktree is dirty; otherwise review the repository.
3. Read complete relevant untracked files and apply repository instructions.

## Threat model

Cover relevant risks, including:

- OAuth scopes, consent, token acquisition, token-cache storage, credential exposure, and token lifetime;
- accidental mail modification or permission expansion beyond read-only access;
- sensitive mailbox data in logs, reports, exceptions, database files, test output, and artifacts;
- untrusted message bodies, attachments, filenames, remote API responses, malformed or oversized inputs;
- SQL injection, unsafe deserialization, path traversal, symlink handling, and unsafe file access where applicable;
- HTML or template injection in generated reports, if present;
- pagination, rate limiting, timeouts, retries, and resource exhaustion against Microsoft Graph;
- dependency, packaging, CI, workflow permission, and build-chain risks.

Do not expose secret or personal-data values. Use safe read-only checks where available. Do not modify files.

## Output

Report actionable findings by P0 through P3 severity with exact file and line, scenario, impact, and concrete remediation. Include a CWE when applicable. Then list trust boundaries, checks performed and omitted, and residual risks. If there are no findings, say so and identify untested attack surfaces.
