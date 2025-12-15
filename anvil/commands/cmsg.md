---
description: Generate conventional commit message from local git changes
---

# Commit Message Command

Invoke the `cmsg` skill to generate a commit message.

## Argument

Issue number (optional): `$ARGUMENTS`

## Instructions

1. Run `git diff --staged` to see staged changes
2. If no staged changes found, run `git diff` to see unstaged changes
3. Analyze the changes and determine the commit type (feat, fix, refactor, etc.)
4. Generate commit message in format: `<type>(dzb): $ARGUMENTS <description>`
   - If `$ARGUMENTS` is empty, omit the issue number: `<type>(dzb): <description>`
5. Output ONLY the commit message, nothing else
