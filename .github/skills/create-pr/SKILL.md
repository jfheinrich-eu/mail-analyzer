---
name: create-pr
description: Create and verify a Mail Analyzer pull request using the repository's actual branch, diff, and checks.
disable-model-invocation: true
---
Create a pull request for the current Mail Analyzer branch when explicitly requested. Do not make unrelated project changes.

## Preflight

1. Resolve the repository root and read repository instructions and any existing contribution or pull-request templates.
2. Confirm `HEAD` is attached to a feature branch and no merge, rebase, cherry-pick, revert, or bisect is in progress.
3. Inspect the worktree and staged changes. A pull request contains committed changes only. If local changes exist, do not stage, commit, stash, discard, or silently omit them; explain and ask whether to proceed with the committed scope.
4. Determine the base branch from explicit direction, branch configuration, and the repository default. Do not guess.
5. Inspect all commits and the complete diff against the base. Check for unrelated changes, secrets, credentials, personal mailbox data, generated files, and binaries.
6. Check whether an open pull request already exists for the branch; do not create a duplicate.
7. Link issues only when confirmed by explicit context or repository references.

## Verify and prepare

- Run focused checks appropriate to the diff, including `git diff --check` and relevant tests.
- State exactly which checks passed, failed, or were not run.
- Use an English Conventional Commit-style title without a trailing period.
- Use an existing pull-request template if present. If there is none, prepare a concise body with Summary, Verification, and Risks sections.
- Do not claim CI, review, or mailbox validation that was not performed.

## Create and verify

- Use the authenticated GitHub CLI (`gh`) when available.
- Confirm repository, head, and base before creation. If pushing is necessary, confirm the intended remote and obtain explicit approval; never force-push.
- After creation, verify and report the URL, title, head, base, checks, and remaining review steps.
- Do not approve, merge, or alter staging.
