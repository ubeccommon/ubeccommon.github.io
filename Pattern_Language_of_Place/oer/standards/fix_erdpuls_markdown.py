#!/usr/bin/env python3
"""
fix_erdpuls_markdown.py
=======================
Applies ERDPULS_MARKDOWN_STANDARD_v1.1 to all markdown files in a folder.

Fixes applied per file:
  1. Insert YAML front matter if missing
  2. Replace --- body dividers with * * *  (skips YAML block & fenced code blocks)
  3. Replace emoji with text equivalents
  4. Replace &nbsp; HTML entities in table cells

Usage:
  python fix_erdpuls_markdown.py                              # fix ./docs in place
  python fix_erdpuls_markdown.py --dir path/to/docs           # fix a specific folder
  python fix_erdpuls_markdown.py --dir docs --output fixed/   # write to separate folder
  python fix_erdpuls_markdown.py --dry-run                    # preview changes only
  python fix_erdpuls_markdown.py --dir docs --backup          # keep .bak copies

When --output is given the source files are never modified; fixed copies are written
to the output folder (which is created if it does not exist). Unchanged files are
still copied so the output folder is a complete, self-contained set.

The script is idempotent — running it twice produces the same result.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

# ─────────────────────────────────────────────────────────────
# YAML BLOCKS
# Key = exact filename (case-sensitive). Files not listed here
# will still get --- → * * * and emoji fixes, but no YAML block.
# ─────────────────────────────────────────────────────────────

YAML_BLOCKS: dict[str, str] = {

    # ── Group A: EN OER Guides ────────────────────────────────
    "01_learning_guide_grades_1-4_EN.md": """\
---
title: "Earth Detectives: First Encounters with Living Ground"
subtitle: "Learning Guide 01 — Grades 1-4"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "02_learning_guide_grades_5-8_EN.md": """\
---
title: "Field Investigators: Measuring the Living World"
subtitle: "Learning Guide 02 — Grades 5-8"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "03_learning_guide_grades_9-12_EN.md": """\
---
title: "Place as Laboratory: Research Methods for the Living World"
subtitle: "Learning Guide 03 — Grades 9-12"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "04_teachers_guide_EN.md": """\
---
title: "Bringing Your Class to the Living Laboratory"
subtitle: "Teachers' Comprehensive Guide (04)"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "05_citizen_scientist_handbook_EN.md": """\
---
title: "How to Monitor, Contribute, and Connect"
subtitle: "Citizen Scientist Handbook (05)"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    # ── Group B: DE Lernleitfäden ─────────────────────────────
    "01_lernleitfaden_klassen_1-4_DE.md": """\
---
title: "Erddetektive: Erste Begegnungen mit lebendigem Boden"
subtitle: "Lernleitfaden 01 — Klassen 1-4"
date: "Februar 2026"
lang: de
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "02_lernleitfaden_klassen_5-8_DE.md": """\
---
title: "Feldforscher: Die lebendige Welt messen"
subtitle: "Lernleitfaden 02 — Klassen 5-8"
date: "Februar 2026"
lang: de
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "03_lernleitfaden_klassen_9-12_DE.md": """\
---
title: "Ort als Labor: Forschungsmethoden für die lebendige Welt"
subtitle: "Lernleitfaden 03 — Klassen 9-12"
date: "Februar 2026"
lang: de
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "04_lehrerhandbuch_DE.md": """\
---
title: "Mit der Klasse ins Lebendige Labor"
subtitle: "Lehrerhandbuch (04)"
date: "Februar 2026"
lang: de
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "05_citizen_scientist_handbuch_DE.md": """\
---
title: "Beobachten, Beitragen und Vernetzen"
subtitle: "Handbuch für Bürgerwissenschaftler*innen (05)"
date: "Februar 2026"
lang: de
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    # ── Group C: Living Experience Guide Collections ───────────
    "questions_to_the_soil_living_guides_EN.md": """\
---
title: "Questions to the Soil — Living Experience Guides"
subtitle: "Five Target-Group-Specific Workshop Guides — Appendix A"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "token_economy_living_guides_EN.md": """\
---
title: "Reciprocal Token Economy — Living Experience Guides"
subtitle: "Five Target-Group-Specific Workshop Guides — Appendix B"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "bioregion_mapping_living_guides_EN.md": """\
---
title: "Bioregion Mapping — Living Experience Guides"
subtitle: "Five Target-Group-Specific Workshop Guides — Appendix C"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "bne_quality_living_guides_EN.md": """\
---
title: "BNE Quality Framework — Living Experience Guides"
subtitle: "Five Target-Group-Specific Workshop Guides — Appendix D"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    # ── Group D: Operational Documents ───────────────────────
    "facilitator_implementation_handbook_EN.md": """\
---
title: "Facilitator's Implementation Handbook"
subtitle: "Annual Calendar, Checklists, and Spatial Design Guide"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "pattern_language_assembly_guide_EN.md": """\
---
title: "Pattern Language Assembly Guide"
subtitle: "How Workshop Outputs Become Collective Knowledge"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    # ── Group E: Theoretical Foundation ──────────────────────
    "proxemic_integration_EN.md": """\
---
title: "Proxemic Integration"
subtitle: "Edward T. Hall's Proxemics as Spatial Grammar for the Pattern Discovery Toolkit"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "pattern_discovery_toolkit_EN.md": """\
---
title: "Pattern Discovery Toolkit"
subtitle: "Parts 1-5: Theory, Method, and Field Application"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "pattern_discovery_toolkit_appendices_EN.md": """\
---
title: "Pattern Discovery Toolkit — Appendices A-D"
subtitle: "Questions to the Soil, Token Economy, Bioregion Mapping, BNE Quality Framework"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    # ── Group F: Master Index ─────────────────────────────────
    "erdpuls_master_index_v1_3_EN.md": """\
---
title: "Erdpuls Müllrose — Master Document Index"
subtitle: "Complete Guide to All Project Documents"
date: "February 2026"
lang: en
version: "1.3"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    # ── Group G: Standards Documents ─────────────────────────
    "ERDPULS_MARKDOWN_STANDARD_v1_1.md": """\
---
title: "Erdpuls Markdown Authoring Standard"
subtitle: "Authoring Rules for All Files in the Erdpuls OER Collection"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",

    "ERDPULS_CLAUDE_PROMPT_v1_1.md": """\
---
title: "Claude Prompt: Create or Update Erdpuls Markdown Files"
subtitle: "Prompt Block and Request Templates — Version 1.1"
date: "February 2026"
lang: en
version: "1.1"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---""",
}

# ─────────────────────────────────────────────────────────────
# EMOJI → TEXT SUBSTITUTIONS
# Applied globally (outside code blocks only).
# Order matters: longer/more specific strings first.
# ─────────────────────────────────────────────────────────────

EMOJI_SUBS: list[tuple[str, str]] = [
    # Translation status lines (EN guides)
    ("🇩🇪 DE — *pending Phase 3*",   "[DE] — *pending Phase 3*"),
    ("🇩🇪 DE — pending Phase 3",      "[DE] — pending Phase 3"),
    ("🇩🇪 DE — *this version*",        "[DE] — *this version*"),
    ("🇩🇪 DE — this version",          "[DE] — this version"),
    ("🇵🇱 PL — *pending Phase 3*",   "[PL] — *pending Phase 3*"),
    ("🇵🇱 PL — pending Phase 3",      "[PL] — pending Phase 3"),
    # Translation status lines (DE guides)
    ("🇩🇪 DE — diese Fassung",         "[DE] — diese Fassung"),
    ("🇩🇪 DE — *diese Fassung*",       "[DE] — *diese Fassung*"),
    ("🇵🇱 PL — *ausstehend Phase 3*", "[PL] — *ausstehend Phase 3*"),
    ("🇵🇱 PL — ausstehend Phase 3",   "[PL] — ausstehend Phase 3"),
    # Bare flag emoji (fallback — catch any remaining instances)
    ("🇩🇪",  "[DE]"),
    ("🇵🇱",  "[PL]"),
    # Master index status emoji
    ("⛔ Not started",  "(not started)"),
    ("⛔ not started",  "(not started)"),
    ("🆕 Draft",        "Draft"),
    ("🆕",              ""),
    ("⏳ pending",      "(pending)"),
    ("⏳",              "(pending)"),
    ("✅",              "(done)"),
]

# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────

def has_yaml(text: str) -> bool:
    """Return True if the file already starts with a YAML front matter block."""
    return text.startswith("---\n") or text.startswith("---\r\n")


def insert_yaml(text: str, yaml_block: str) -> tuple[str, bool]:
    """
    Prepend yaml_block to text (with a trailing newline separator).
    Returns (new_text, changed).
    """
    if has_yaml(text):
        return text, False
    new_text = yaml_block + "\n" + text.lstrip("\n")
    return new_text, True


def _split_into_segments(text: str) -> list[tuple[str, bool]]:
    """
    Split text into (segment, is_code_block) pairs.

    Segments inside fenced code blocks (``` or ~~~) are marked is_code_block=True
    and will not be processed for --- → * * * or emoji substitution.

    The YAML front matter block (lines 1 to closing ---) is also protected.
    """
    segments: list[tuple[str, bool]] = []
    lines = text.split("\n")
    i = 0
    # Skip YAML front matter
    yaml_end = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                yaml_end = j
                break
        if yaml_end:
            segments.append(("\n".join(lines[0: yaml_end + 1]), True))  # protect YAML
            i = yaml_end + 1

    in_code = False
    fence_char = ""
    current: list[str] = []
    current_is_code = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not in_code and (stripped.startswith("```") or stripped.startswith("~~~")):
            # Flush current segment
            if current:
                segments.append(("\n".join(current), current_is_code))
                current = []
            in_code = True
            fence_char = stripped[:3]
            current_is_code = True
            current.append(line)
        elif in_code and stripped.startswith(fence_char):
            current.append(line)
            segments.append(("\n".join(current), True))
            current = []
            current_is_code = False
            in_code = False
            fence_char = ""
        else:
            if not current:
                current_is_code = in_code
            current.append(line)
        i += 1

    if current:
        segments.append(("\n".join(current), current_is_code))

    return segments


def fix_dividers(text: str) -> tuple[str, int]:
    """
    Replace bare --- horizontal rules with * * * outside YAML and code blocks.
    Returns (new_text, count_of_replacements).
    """
    segments = _split_into_segments(text)
    count = 0
    result_parts: list[str] = []

    for segment, is_protected in segments:
        if is_protected:
            result_parts.append(segment)
            continue
        # Match lines that are exactly --- (possibly with surrounding blank lines)
        # We replace the --- line; surrounding blank lines are preserved.
        new_seg, n = re.subn(r"^---$", "* * *", segment, flags=re.MULTILINE)
        count += n
        result_parts.append(new_seg)

    return "\n".join(result_parts), count


def fix_emoji(text: str) -> tuple[str, int]:
    """
    Apply EMOJI_SUBS outside code blocks.
    Returns (new_text, total_count_of_replacements).
    """
    segments = _split_into_segments(text)
    count = 0
    result_parts: list[str] = []

    for segment, is_protected in segments:
        if is_protected:
            result_parts.append(segment)
            continue
        for old, new in EMOJI_SUBS:
            if old in segment:
                n = segment.count(old)
                segment = segment.replace(old, new)
                count += n
        result_parts.append(segment)

    return "\n".join(result_parts), count


def fix_nbsp(text: str) -> tuple[str, int]:
    """
    Replace &nbsp; (and &#160;) inside markdown table cells with a regular space.
    Applied globally — these have no legitimate use in Erdpuls table cells.
    Returns (new_text, count_of_replacements).
    """
    new_text, n1 = re.subn(r"&nbsp;", " ", text)
    new_text, n2 = re.subn(r"&#160;", " ", new_text)
    # Collapse multiple spaces that may result into a single space within cells
    # (only between pipe chars to avoid touching code indentation)
    new_text = re.sub(r"(\|[^|\n]*?) {2,}([^|\n]*?\|)", lambda m: m.group(0).replace("  ", " "), new_text)
    return new_text, n1 + n2


def process_file(
    path: Path,
    dry_run: bool = False,
    backup: bool = False,
    output_path: Path | None = None,
) -> dict:
    """
    Process a single markdown file. Returns a result dict with change counts.

    output_path: if given, write the result here instead of overwriting path.
                 The file at path is never modified when output_path is set.
    """
    result = {
        "file": path.name,
        "yaml_added": False,
        "dividers_fixed": 0,
        "emoji_fixed": 0,
        "nbsp_fixed": 0,
        "skipped": False,
        "error": None,
    }

    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        result["error"] = str(e)
        result["skipped"] = True
        return result

    original = text

    # 1 ── YAML
    yaml_block = YAML_BLOCKS.get(path.name)
    if yaml_block and not has_yaml(text):
        text, changed = insert_yaml(text, yaml_block)
        result["yaml_added"] = changed
    elif not yaml_block and not has_yaml(text):
        # No YAML defined for this file — note it but continue with other fixes
        result["yaml_added"] = "NO_YAML_DEFINED"

    # 2 ── Dividers
    text, n = fix_dividers(text)
    result["dividers_fixed"] = n

    # 3 ── Emoji
    text, n = fix_emoji(text)
    result["emoji_fixed"] = n

    # 4 ── &nbsp;
    text, n = fix_nbsp(text)
    result["nbsp_fixed"] = n

    # Write if changed (or copy unchanged file to output folder)
    if not dry_run:
        dest = output_path if output_path is not None else path
        if output_path is not None:
            # Always write to output folder (copy even if unchanged)
            dest.write_text(text, encoding="utf-8")
        elif text != original:
            if backup:
                shutil.copy2(path, path.with_suffix(".md.bak"))
            dest.write_text(text, encoding="utf-8")

    result["changed"] = text != original
    return result


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply ERDPULS_MARKDOWN_STANDARD_v1.1 to all .md files in a directory."
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Path to the docs folder (default: current directory)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Write fixed files to this folder instead of modifying in place "
             "(folder is created if it does not exist; source files are untouched)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Save .bak copies of files before overwriting",
    )
    parser.add_argument(
        "--file",
        default=None,
        help="Process a single file instead of the whole directory",
    )
    args = parser.parse_args()

    # Resolve output directory
    output_dir: Path | None = None
    if args.output:
        output_dir = Path(args.output)
        if not args.dry_run:
            output_dir.mkdir(parents=True, exist_ok=True)

    if args.file:
        paths = [Path(args.file)]
    else:
        docs_dir = Path(args.dir)
        if not docs_dir.is_dir():
            print(f"ERROR: {docs_dir} is not a directory.", file=sys.stderr)
            sys.exit(1)
        paths = sorted(docs_dir.glob("*.md"))

    if not paths:
        print("No .md files found.")
        return

    mode = "DRY RUN — " if args.dry_run else ""
    print(f"\n{mode}Erdpuls Markdown Compliance Fixer")
    print(f"Standard: ERDPULS_MARKDOWN_STANDARD_v1.1")
    print(f"Files found: {len(paths)}")
    if output_dir:
        print(f"Output:      {output_dir}{'  (dry-run — folder not created)' if args.dry_run else ''}")
    print("=" * 70)

    total_yaml = 0
    total_dividers = 0
    total_emoji = 0
    total_nbsp = 0
    total_changed = 0
    skipped = []

    for path in paths:
        out = output_dir / path.name if output_dir else None
        res = process_file(path, dry_run=args.dry_run, backup=args.backup, output_path=out)

        if res.get("skipped"):
            skipped.append((path.name, res.get("error", "unknown error")))
            continue

        changed = res.get("changed", False)
        if changed:
            total_changed += 1

        yaml_status = ""
        if res["yaml_added"] is True:
            yaml_status = " +YAML"
            total_yaml += 1
        elif res["yaml_added"] == "NO_YAML_DEFINED":
            yaml_status = " [no YAML template — skipped]"

        dividers = res["dividers_fixed"]
        emoji    = res["emoji_fixed"]
        nbsp     = res["nbsp_fixed"]

        total_dividers += dividers
        total_emoji    += emoji
        total_nbsp     += nbsp

        if changed or yaml_status:
            parts = []
            if yaml_status: parts.append(yaml_status.strip())
            if dividers:    parts.append(f"{dividers} divider{'s' if dividers != 1 else ''}")
            if emoji:       parts.append(f"{emoji} emoji")
            if nbsp:        parts.append(f"{nbsp} &nbsp;")
            summary = ", ".join(parts) if parts else "no changes needed"
            marker = "(dry-run) " if args.dry_run else "(fixed)   "
            if not changed:
                marker = "(ok)      "
            print(f"  {marker}{path.name}: {summary}")
        else:
            print(f"  (ok)      {path.name}: no changes needed")

    print("=" * 70)
    verb = "Would change" if args.dry_run else "Changed"
    print(f"\nSummary:")
    print(f"  {verb} {total_changed} file(s)")
    print(f"  YAML blocks added:    {total_yaml}")
    print(f"  --- dividers fixed:   {total_dividers}")
    print(f"  Emoji replaced:       {total_emoji}")
    print(f"  &nbsp; replaced:      {total_nbsp}")

    if skipped:
        print(f"\nSkipped ({len(skipped)}):")
        for name, err in skipped:
            print(f"  {name}: {err}")

    if args.dry_run:
        print("\nNo files were modified (--dry-run). Re-run without --dry-run to apply.")
    else:
        print("\nDone.")


if __name__ == "__main__":
    main()
