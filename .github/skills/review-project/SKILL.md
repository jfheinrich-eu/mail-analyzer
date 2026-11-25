---
name: review-project
description: Run engineering and security reviews of Mail Analyzer, then propose documentation updates for explicit approval.
disable-model-invocation: true
---
Perform an engineering review and security review of Mail Analyzer, then check documentation for consistency. Do not modify source code, tests, configuration, or documentation during the reviews.

## Scope and review

1. Inspect Git state and determine whether to review current changes and their impact or the clean repository.
2. Read complete relevant untracked files and apply repository instructions.
3. Perform the engineering review required by `/review`.
4. Perform the security review required by `/sec-review`.
5. Compare relevant documentation with actual code, tests, dependencies, and CI. Check for stale or contradictory behavior claims.

Do not expose token values or mailbox data. Do not claim unrun checks passed.

## Documentation changes

- Report actionable review findings first, then list any proposed documentation changes.
- Do not modify documentation until the user explicitly approves the exact files and corrections.
- After approval, change only the approved documentation files. Keep repository documentation in English and do not claim unimplemented behavior.
- Run `git diff --check` and relevant documentation checks when available.

## Output

Report actionable findings by P0 through P3 severity, with exact locations, evidence, impact, and remediation. Include documentation reviewed and proposed, assumptions, checks performed and omitted, and residual risks. Do not create a separate report file unless the user requests one.
