#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
relicense_learning_pathway_v1.py

Surgically relicenses the Erdpuls Learning Pathway System source documents
from CC BY-NC-SA 4.0 to CC BY-SA 4.0, in place.

Scope: EN, DE, PL v1.1 files only. Touches ONLY each document's own license
declaration (YAML front matter, metadata table row, colophon link + share/adapt
sentence). Does NOT touch the CC BY-SA references in body content (student
output descriptions), which are already BY-SA and correct.

Design: exact science. Every replacement rule carries an expected occurrence
count. If reality does not match, the file is reported as ANOMALY and left
untouched — the script never guesses.

Idempotent: a file already relicensed reports CLEAN and is skipped.
Default mode is dry-run. Pass --apply to write. Backups (.bak.<timestamp>)
are written before any modification.

This project uses the services of Claude and Anthropic PBC to inform our
decisions and recommendations. This project was made possible with the
assistance of Claude and Anthropic PBC.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path

# Repo-relative default paths (run from the repo root).
BASE = Path("Pattern_Language_of_Place/Learning_Pathways")

# Replacement rules shared by all three language files.
# Each tuple: (old, new, expected_count)
COMMON_RULES = [
    ("CC BY-NC-SA 4.0", "CC BY-SA 4.0", 3),
    ("by-nc-sa/4.0", "by-sa/4.0", 1),
]

# Language-specific colophon phrasing (the human-readable license name and the
# "you are free to share and adapt ... for non-commercial purposes" sentence).
LANG_RULES = {
    "EN": [
        ("Attribution-NonCommercial-ShareAlike 4.0 International",
         "Attribution-ShareAlike 4.0 International", 1),
        ("share and adapt this material for non-commercial purposes",
         "share and adapt this material", 1),
    ],
    "DE": [
        ("Namensnennung \u2013 Nicht kommerziell \u2013 Weitergabe unter gleichen Bedingungen 4.0 International",
         "Namensnennung \u2013 Weitergabe unter gleichen Bedingungen 4.0 International", 1),
        ("Sie d\u00fcrfen dieses Material f\u00fcr nicht-kommerzielle Zwecke teilen und anpassen",
         "Sie d\u00fcrfen dieses Material teilen und anpassen", 1),
    ],
    "PL": [
        ("Uznanie autorstwa-U\u017cycie niekomercyjne-Na tych samych warunkach",
         "Uznanie autorstwa-Na tych samych warunkach", 1),
        ("udost\u0119pnia\u0107 i adaptowa\u0107 ten materia\u0142 do cel\u00f3w niekomercyjnych",
         "udost\u0119pnia\u0107 i adaptowa\u0107 ten materia\u0142", 1),
    ],
}

FNAME = "Erdpuls_Learning_Pathway_System_{lang}_v1_1.md"


def file_path(root: Path, lang: str) -> Path:
    return root / BASE / lang / FNAME.format(lang=lang)


def process(path: Path, lang: str, apply: bool) -> str:
    """Return a one-word status: CLEAN | PATCHED | WOULD-PATCH | ANOMALY | MISSING."""
    if not path.is_file():
        print(f"  [MISSING] {path}")
        return "MISSING"

    with open(path, "r", encoding="utf-8", newline="") as fh:
        original = fh.read()
    rules = COMMON_RULES + LANG_RULES[lang]

    # Idempotency check: if no OLD strings remain, treat as already relicensed.
    remaining_old = sum(original.count(old) for old, _new, _n in rules)
    if remaining_old == 0:
        # Confirm the NEW strings are present as expected before declaring CLEAN.
        ok = all(original.count(new) >= n for _old, new, n in rules)
        print(f"  [{'CLEAN' if ok else 'ANOMALY'}] {path.name} "
              f"(no NC strings found; {'BY-SA already present' if ok else 'BY-SA strings NOT found'})")
        return "CLEAN" if ok else "ANOMALY"

    # Verify every rule matches its expected count exactly before touching anything.
    text = original
    anomalies = []
    for old, _new, expected in rules:
        found = text.count(old)
        if found != expected:
            anomalies.append(f"    '{old[:48]}...' expected {expected}, found {found}")
    if anomalies:
        print(f"  [ANOMALY] {path.name} — counts do not match; file left untouched:")
        print("\n".join(anomalies))
        return "ANOMALY"

    # Apply.
    for old, new, _expected in rules:
        text = text.replace(old, new)

    # Post-condition: zero NC markers remain.
    residual = text.count("BY-NC-SA") + text.count("by-nc-sa") + \
        text.count("NonCommercial") + text.count("Nicht kommerziell") + \
        text.count("niekomercyjn")
    if residual != 0:
        print(f"  [ANOMALY] {path.name} — {residual} residual NC marker(s) after patch; NOT written.")
        return "ANOMALY"

    if not apply:
        print(f"  [WOULD-PATCH] {path.name} — {remaining_old} NC string(s) -> BY-SA (dry-run)")
        return "WOULD-PATCH"

    stamp = _dt.datetime.now().strftime("%Y%m%d%H%M%S")
    backup = path.with_suffix(path.suffix + f".bak.{stamp}")
    with open(backup, "w", encoding="utf-8", newline="") as fh:
        fh.write(original)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print(f"  [PATCHED] {path.name} — {remaining_old} NC string(s) -> BY-SA "
          f"(backup: {backup.name})")
    return "PATCHED"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="write changes (default is dry-run)")
    ap.add_argument("--root", default=".",
                    help="repo root (default: current directory)")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"Relicense EN/DE/PL Learning Pathway  CC BY-NC-SA 4.0 -> CC BY-SA 4.0")
    print(f"Mode: {mode}   Root: {root}\n")

    results = {}
    for lang in ("EN", "DE", "PL"):
        results[lang] = process(file_path(root, lang), lang, args.apply)

    print("\nSummary:", ", ".join(f"{k}={v}" for k, v in results.items()))
    # Non-zero exit if any anomaly/missing so the caller notices.
    bad = {"ANOMALY", "MISSING"} & set(results.values())
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
