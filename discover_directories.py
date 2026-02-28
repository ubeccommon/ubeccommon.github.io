"""
discover_directories.py
Generates a tree-style project structure of the current working directory,
excluding .git, and writes the result to structure.txt.
"""

import os
from pathlib import Path
from datetime import datetime

CWD = Path.cwd()
OUTPUT_FILE = Path("structure.txt")


def build_tree(root: Path, prefix: str = "") -> list[str]:
    lines = []
    try:
        entries = sorted(root.iterdir(), key=lambda e: (e.is_file(), e.name.lower()))
    except PermissionError:
        return lines

    entries = [e for e in entries if e.name != ".git"]
    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        lines.append(f"{prefix}{connector}{entry.name}")
        if entry.is_dir():
            extension = "    " if i == len(entries) - 1 else "│   "
            lines.extend(build_tree(entry, prefix + extension))
    return lines


def count_entries(root: Path) -> tuple[int, int]:
    dir_count, file_count = 0, 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        dir_count += len(dirnames)
        file_count += len(filenames)
    return dir_count, file_count


def main():
    print(f"Scanning: {CWD}")
    tree_lines = build_tree(CWD)
    dir_count, file_count = count_entries(CWD)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        f.write(f"Project Structure: {CWD.name}/\n")
        f.write(f"Generated:         {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Directories: {dir_count}  |  Files: {file_count}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"{CWD.name}/\n")
        for line in tree_lines:
            f.write(line + "\n")

    print(f"Done — {dir_count} dirs, {file_count} files → '{OUTPUT_FILE}'")


if __name__ == "__main__":
    main()
