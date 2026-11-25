---
name: commit
description: Prepare reviewed atomic Conventional Commit groups and create only commits explicitly approved by the user.
disable-model-invocation: true
---
Prepare and create reviewed atomic commits for the current repository. Follow all repository instructions. Do not modify project files while running this workflow.

## Safety

- Resolve the repository root and verify the current branch and Git state before proceeding.
- Stop if a merge, rebase, cherry-pick, revert, or bisect is in progress, or if `HEAD` is detached.
- Never discard changes, stash, amend, rebase, reset, clean, push, or force-push.
- Preserve existing staging. Do not stage broadly with `git add .` or `git add -A`.
- Do not expose secrets or mailbox data. Stop before staging any credentials, tokens, personal data, generated output, or suspicious binaries.
- Do not commit until the user approves the exact file list and complete commit message.

## Inspect and group

1. Inspect `git status --porcelain=v1 -z --untracked-files=all`, `git diff`, and `git diff --cached`.
2. Read relevant changes, including complete untracked files, and check for secrets and generated files.
3. If files are already staged, preserve them as an indivisible group unless the user explicitly authorizes non-destructive unstaging.
4. Propose coherent groups, assigning each candidate file to exactly one group. Do not split files by hunk.
5. For each group, show its purpose, exact paths, risk, checks, and an English Conventional Commit message.
6. Ask for approval before staging or committing each group.

## Commit and verify

- Stage only the exact approved paths. Before committing, compare staged paths with the approved list and inspect the staged diff.
- Run `git diff --cached --check` and relevant focused tests.
- Do not bypass hooks. If a check fails, keep the state and report the failure.
- After committing, verify the commit hash, subject, changed paths, and remaining worktree state.
- Do not push.
