#!/usr/bin/env python3
"""
Generate a .md file for each command defined in Commands.md.

Parsing rules:
- Each command starts with a markdown H2 heading line like:
  ## COMMAND_NAME (Command|Express Tool|...)
- The description is all following lines up to (but not including) the next H2 heading (## ...) or EOF.
- Some entries might miss a description; those will still get a file with a placeholder.
- File names are sanitized for Windows: invalid filename characters are replaced with '-'.

Outputs:
- Creates a folder named 'commands' (relative to the repo root) and writes one file per command: commands/<COMMAND_NAME>.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] if (Path(__file__).parent.name == 'scripts') else Path(__file__).resolve().parent
SOURCE = ROOT / 'Commands.md'
OUT_DIR = ROOT / 'commands'

HEADING_RE = re.compile(r'^##\s+(.+?)(?:\s+\(([^)]+)\))?\s*$')
INVALID_CHARS_RE = re.compile(r'[<>:"/\\|?*]')  # Windows invalid filename chars
WHITESPACE_RE = re.compile(r'\s+')


def sanitize_filename(name: str) -> str:
	"""Sanitize command name for safe Windows filename usage."""
	# Replace invalid characters with '-'
	name = INVALID_CHARS_RE.sub('-', name)
	# Collapse whitespace to single hyphen
	name = WHITESPACE_RE.sub('-', name.strip())
	# Avoid trailing dots or spaces
	name = name.rstrip(' .')
	# Ensure not empty
	return name or 'UNTITLED'


def parse_commands(md_text: str) -> list[dict]:
	"""Parse the markdown text into a list of command dicts.

	Each dict: { 'name': str, 'kind': str|None, 'body': str }
	"""
	lines = md_text.splitlines()
	commands: list[dict] = []
	current = None
	body_lines: list[str] = []

	for line in lines:
		m = HEADING_RE.match(line)
		if m:
			# Flush previous
			if current is not None:
				current['body'] = '\n'.join(body_lines).strip()
				commands.append(current)
				body_lines = []
			name = m.group(1).strip()
			kind = (m.group(2) or '').strip() or None
			current = {'name': name, 'kind': kind, 'body': ''}
		else:
			# Accumulate
			if current is not None:
				body_lines.append(line)
	# Flush last
	if current is not None:
		current['body'] = '\n'.join(body_lines).strip()
		commands.append(current)
	return commands


def render_command_md(name: str, kind: str | None, body: str) -> str:
	"""Render the per-command Markdown file content."""
	head = f"# {name}\n\n"
	meta = f"- Type: {kind}\n\n" if kind else ""
	if not body:
		body = "_No description available in source file._"
	return head + meta + body.strip() + "\n"


def main(argv: list[str]) -> int:
	if not SOURCE.exists():
		print(f"Source file not found: {SOURCE}", file=sys.stderr)
		return 1
	md_text = SOURCE.read_text(encoding='utf-8')
	cmds = parse_commands(md_text)
	if not cmds:
		print("No commands found in Commands.md", file=sys.stderr)
		return 2
	OUT_DIR.mkdir(parents=True, exist_ok=True)
	count = 0
	for cmd in cmds:
		fname = sanitize_filename(cmd['name']) + '.md'
		out_path = OUT_DIR / fname
		content = render_command_md(cmd['name'], cmd['kind'], cmd['body'])
		out_path.write_text(content, encoding='utf-8', newline='\n')
		count += 1
	print(f"Wrote {count} command files to {OUT_DIR.relative_to(ROOT)}")
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
