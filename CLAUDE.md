# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Claude Desktop plugins marketplace - a collection of plugins that extend Claude's capabilities through commands and skills.

## Architecture

```
vilem-claude-plugins/
├── .claude-plugin/
│   └── marketplace.json       # Plugin registry - lists all plugins
├── <plugin-name>/             # Each plugin is a directory
│   ├── .claude-plugin/
│   │   └── plugin.json        # Plugin manifest (name, version, author)
│   ├── commands/              # Slash commands (*.md files)
│   └── skills/                # Skills with SKILL.md definitions
│       └── <skill-name>/
│           ├── SKILL.md       # Skill definition and instructions
│           ├── examples.md    # Usage examples (optional)
│           ├── reference.md   # API/technical reference (optional)
│           └── templates/     # Output templates (optional)
```

## Plugin Components

### Commands (`commands/*.md`)
- Slash commands invoked via `/command-name [args]`
- YAML frontmatter with `description` field
- Use `$ARGUMENTS` to access command-line arguments
- Markdown body contains instructions for Claude

### Skills (`skills/<name>/SKILL.md`)
- Complex capabilities with multi-step instructions
- YAML frontmatter with `name` and `description`
- Can use WebFetch, Bash, and other tools
- Activated automatically based on description matching

### Plugin Manifest (`plugin.json`)
```json
{
  "name": "plugin-name",
  "description": "Plugin description",
  "version": "1.0.0",
  "author": { "name": "...", "email": "...", "url": "..." }
}
```

### Marketplace Registry (`.claude-plugin/marketplace.json`)
```json
{
  "name": "vilem-claude-plugins",
  "plugins": [
    { "name": "plugin-name", "source": "./plugin-name", "description": "..." }
  ]
}
```

## Current Plugins

- **demo-plugin**: Weather and stocks skills, hello command
- **anvil**: Git workflow helper with `/cmsg` command for conventional commits

## Creating New Plugins

1. Create plugin directory with `.claude-plugin/plugin.json`
2. Add commands in `commands/` as markdown files
3. Add skills in `skills/<name>/SKILL.md`
4. Register in `.claude-plugin/marketplace.json`

## Language Preferences

- Avoid Python for scripts
- Prefer JavaScript or Bash for any scripting needs
