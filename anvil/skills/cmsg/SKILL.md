---
name: cmsg
description: Generate conventional commit message from local git changes
---

# Commit Message Generator Skill

Generate a conventional commit message based on local git changes.

## When to Use

Use this skill when the user invokes the `/cmsg` command.

## Instructions

1. Run `git diff --staged` to see staged changes. If no staged changes, run `git diff` to see unstaged changes.

2. Analyze the changes to determine:
   - The type of change: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `build` `ops`
   - A brief description of what changed

3. Generate a commit message in this exact format:
   ```
   <type>(dzb): <issue> <description>
   ```

   - **type**: One of the conventional commit types based on the changes
   - **scope**: Always `dzb`
   - **issue**: The issue number from the argument (e.g., `CH-2588`) - only include if provided
   - **description**: Brief description in imperative mood, lowercase

## Format Rules

- Always use `dzb` as the scope
- If issue number is provided as argument, include it after the colon
- Keep description concise (under 50 chars ideally)
- Use imperative mood: "add" not "added", "fix" not "fixed"
- No period at the end

## Examples

With issue number argument `CH-2588`:
```
feat(dzb): CH-2588 add url fallback
fix(dzb): CH-2588 resolve null pointer exception
refactor(dzb): CH-2588 extract helper method
```

Without issue number:
```
feat(dzb): add new endpoint
fix(dzb): handle edge case in parser
chore(dzb): update dependencies
```

## Output

Output ONLY the commit message, nothing else. Ready to copy and use.
