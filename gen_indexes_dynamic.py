#!/usr/bin/env python3
"""
Erdpuls OER — Dynamic Index Generator
======================================
Scans the repository filesystem and generates index.html for every directory.
Skips Jekyll internals, build artifacts, and the generated files themselves.

From 1.4.0 it also builds the OER publication layer from the YAML front
matter of every published Markdown source:

    resources/                                   catalogue of all collections
    resources/<collection>/                      one collection, all works
    resources/<collection>/<id>/                 one work, all languages
    resources/<collection>/<id>/<lang>/          one work in one language
    catalogue/catalogue.json                     schema.org / LRMI JSON-LD
    catalogue/oer_commons.csv                    OER Commons bulk-import rows
    sitemap.xml, robots.txt

The <id> comes from the front matter field `id:` when present, otherwise
from the filename without its language code and version, so the URL stays
the same when a file is renamed for a new version. These URLs are the ones
to give to OER Commons, Zenodo, WLO and OERSI.

A Markdown file becomes a resource when its front matter has a title and a
license, holds no template placeholders, and does not sit in a standards/
or reports/ folder. `oer: false` in the front matter leaves a file out.

Usage:
    python gen_indexes_dynamic.py [--repo-root PATH] [--dry-run]
                                  [--no-oer] [--report PATH]

    --no-oer        directory indexes only, as before 1.4.0
    --report PATH   write a CSV of missing OER metadata per resource

Called automatically by GitHub Actions on every push.

Version: 1.4.0
Changelog:
    1.4.0 - OER publication layer: stable landing pages per work and
            language with LRMI JSON-LD, hreflang and attribution; a
            catalogue of all resources; catalogue.json, an OER Commons
            bulk-import CSV, sitemap.xml and robots.txt; a metadata gap
            report. Stylesheet moved to BASE_CSS (output unchanged).
            Directory index footers link to the resource catalogue.
    1.3.3 - Carpathian OER Commons: label for foundations/grounding/, the
            philosophy, survey, and proposal beside the foundations.
    1.3.2 - Carpathian OER Commons: label for the foundations/ folder,
            which holds the foundations paper of the collection.
    1.3.1 - Carpathian OER Commons: label for the seventh module group,
            settlement, shown as "Open Hamlet"; labels for the
            patterns/ and narrative/ folders of the place's pattern
            language.
    1.3.0 - Per-collection branding: pages under Carpathian_OER_Commons/
            carry "Soil and Peace" in title, logo, and footer; all other
            pages keep "Erdpuls". Added DIR_LABELS for the Carpathian OER
            Commons collection, its six module groups, and modules,
            drawings, and data folders.
    1.2.2 - Added 'advocacy' to DIR_LABELS (advocacy strand under oer/docs).
    1.2.1 - Renamed site logo/footer text "Erdpuls" -> "Erdpuls".
    1.2.0 - Added language switcher + hreflang alternates + per-directory
            <html lang> for directories inside a language subtree.
    1.1.0 - Added Ukrainian (UK / uk) to DIR_LABELS language labels.
    1.0.0 - Baseline (pre-versioning): initial dynamic index generator.

License: GNU Affero General Public License v3.0 (AGPL-3.0)

This project uses the services of Claude and Anthropic PBC to inform our
decisions and recommendations. This project was made possible with the
assistance of Claude and Anthropic PBC.
"""

__version__ = "1.4.0"

import os
import re
import csv
import io
import json
import argparse
from html import escape
from pathlib import Path
from urllib.parse import quote

try:                                    # PyYAML when installed (CI installs it);
    import yaml                         # a small built-in reader otherwise
except ImportError:                     # (see read_front_matter)
    yaml = None

# ── Configuration ─────────────────────────────────────────────────────────────

BASE_URL    = "https://ubeccommon.github.io"
GITHUB_BLOB = "https://github.com/ubeccommon/ubeccommon.github.io/blob/main"
RAW_BASE    = "https://raw.githubusercontent.com/ubeccommon/ubeccommon.github.io/main"

# Directories to skip entirely (never generate an index inside these)
SKIP_DIRS = {
    '.git', '.github', '_site', '_includes', '_layouts',
    '_sass', '_data', 'node_modules', '__pycache__', '.jekyll-cache',
}

# Top-level directories written by the OER layer, which makes its own pages
ROOT_SKIP_DIRS = {'resources', 'catalogue'}

# Files to skip in listings (never show these in indexes)
SKIP_FILES = {
    'index.html',       # the file we're generating
    'viewer.html',      # the viewer itself
    '.gitignore',
    '.nojekyll',
    'Gemfile',
    'Gemfile.lock',
    '.DS_Store',
}

# File extensions to link to the viewer (rendered client-side)
VIEWER_EXTENSIONS = {'.md'}

# File extensions to link to GitHub blob viewer
GITHUB_EXTENSIONS = {'.py', '.jsx', '.yml', '.yaml', '.txt', '.docx', '.xlsx', '.js', '.css'}

# Friendly directory labels
DIR_LABELS = {
    'DE':                       '🇩🇪 Deutsch',
    'EN':                       '🇬🇧 English',
    'PL':                       '🇵🇱 Polski',
    'UK':                       '🇺🇦 Українська',
    'soil_art':                 '🎨 Soil Art',
    'soil_questions':           '❓ Soil Questions',
    'soil':                     '🌱 Soil',
    'advocacy':                 '📣 Advocacy',
    'audit':                    '✅ Audit',
    'pdf':                      '📕 PDF',
    'docs':                     '📚 Docs',
    'oer':                      '🔓 OER',
    'standards':                '📐 Standards',
    'reports':                  '📊 Reports',
    'Learning_Pathways':        '🗺️ Learning Pathways',
    'Pattern_Language_of_Place':'🏛️ Pattern Language of Place',
    'Carpathian_OER_Commons':   '🌲 Carpathian OER Commons',
    'foundations':              '🌿 Foundations',
    'grounding':                '🪨 Grounding',
    'modules':                  '🧩 Modules',
    'drawings':                 '✏️ Drawings',
    'data':                     '📈 Data',
    'ground':                   '🛡️ Ground and Safety',
    'utilities':                '💧 Utilities',
    'buildings':                '🏠 Buildings',
    'land':                     '🌳 Land, Forest, Food',
    'programme':                '🧭 Programme',
    'organisation':             '🤝 Organisation',
    'settlement':               '🏘️ Open Hamlet',
    'patterns':                 '🧵 Patterns',
    'narrative':                '📜 Narrative',
}

# Per-collection branding: first path segment -> (brand, subtitle, icon).
# Anything not listed carries the default Erdpuls branding.
DEFAULT_BRAND = ('Erdpuls', 'Open Educational Resources', '🌱')
COLLECTION_BRANDS = {
    'Carpathian_OER_Commons': ('Soil and Peace', 'Carpathian OER Commons', '🌲'),
}


def collection_brand(rel_path):
    parts = list(rel_path.parts)
    if parts and parts[0] in COLLECTION_BRANDS:
        return COLLECTION_BRANDS[parts[0]]
    return DEFAULT_BRAND

# Language directory codes (keys of DIR_LABELS that denote a content language)
# mapped to their BCP 47 code used in <html lang> / hreflang.
LANG_HTML = {'DE': 'de', 'EN': 'en', 'PL': 'pl', 'UK': 'uk'}
LANG_ORDER = ['DE', 'EN', 'PL', 'UK']   # stable display order for the switcher


def lang_context(rel_path, repo_root):
    """Compute language-switch context for a directory.

    If rel_path lies inside a language subtree (one path segment is a known
    language code), return (current_code, available) where available is a list
    of (code, url) pairs for the sibling-language directories that ACTUALLY
    exist on disk (including the current one). Otherwise return (None, []).

    Existence is checked so we never link to languages that have no content yet.
    """
    parts = list(rel_path.parts)
    idx = next((i for i, part in enumerate(parts) if part in LANG_HTML), None)
    if idx is None:
        return None, []
    current = parts[idx]
    available = []
    for code in LANG_ORDER:
        cand = parts.copy()
        cand[idx] = code
        if (repo_root / Path(*cand)).is_dir():
            available.append((code, f"{BASE_URL}/{'/'.join(cand)}/"))
    return current, available

# ── Helpers ───────────────────────────────────────────────────────────────────

def get_file_icon(filename):
    ext = Path(filename).suffix.lower()
    return {
        '.md':   ('📄', 'Markdown'),
        '.html': ('🌐', 'HTML'),
        '.jsx':  ('⚛️',  'React'),
        '.py':   ('🐍', 'Python'),
        '.pdf':  ('📕', 'PDF'),
        '.xlsx': ('📊', 'Spreadsheet'),
        '.docx': ('📝', 'Document'),
        '.yml':  ('⚙️',  'Config'),
        '.yaml': ('⚙️',  'Config'),
        '.txt':  ('📃', 'Text'),
        '.js':   ('📜', 'JavaScript'),
        '.css':  ('🎨', 'CSS'),
    }.get(ext, ('📄', 'File'))


def dir_label(name):
    return DIR_LABELS.get(name, f'📁 {name}')


def format_display(name):
    return Path(name).stem.replace('_', ' ').replace('-', ' ')


def build_breadcrumb(rel_path):
    """Return list of (label, url) pairs for breadcrumb nav."""
    parts = rel_path.parts if rel_path != Path('') else []
    crumbs = [('🏠 Root', BASE_URL + '/')]
    for i, part in enumerate(parts):
        partial = '/'.join(str(p) for p in parts[:i+1])
        crumbs.append((part, f"{BASE_URL}/{partial}/"))
    return crumbs


def file_url(repo_rel_path, filename):
    """Return the URL for a file link."""
    ext = Path(filename).suffix.lower()
    full = f"{repo_rel_path}/{filename}" if repo_rel_path else filename

    if ext in VIEWER_EXTENSIONS:
        return f"{BASE_URL}/viewer.html?file={full}"
    elif ext in GITHUB_EXTENSIONS:
        return f"{GITHUB_BLOB}/{full}"
    else:
        return f"{BASE_URL}/{full}"


def file_badge(filename):
    ext = Path(filename).suffix.lower()
    if ext in VIEWER_EXTENSIONS:
        return "<span class='gh-badge'>viewer ↗</span>"
    elif ext in GITHUB_EXTENSIONS:
        return "<span class='gh-badge'>GitHub ↗</span>"
    return ""


# ── Shared stylesheet ─────────────────────────────────────────────────────────
# Used by directory indexes and by the OER landing pages, so both look alike.

BASE_CSS = """  :root {
    --soil-dark: #2C1810;
    --soil-mid: #5C3A1E;
    --soil-warm: #8B5E3C;
    --clay: #C4874A;
    --sand: #E8C99A;
    --parchment: #F5EDD8;
    --leaf: #4A7C59;
    --leaf-light: #7CAD8A;
    --text-primary: #1A0F08;
    --text-muted: #8B7355;
    --border: rgba(92,58,30,0.15);
    --shadow: 0 2px 12px rgba(44,24,16,0.08);
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--parchment);
    color: var(--text-primary);
    min-height: 100vh;
    background-image:
      radial-gradient(ellipse at 20% 50%, rgba(196,135,74,0.08) 0%, transparent 60%),
      radial-gradient(ellipse at 80% 20%, rgba(74,124,89,0.06) 0%, transparent 50%);
  }
  .header {
    background: linear-gradient(120deg, #155799 0%, #159957 100%);
    color: white;
    padding: 0 2rem;
    position: sticky;
    top: 0;
    z-index: 100;
    border-bottom: none;
  }
  .header-inner {
    max-width: 900px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    gap: 1rem;
    height: 60px;
  }
  .site-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    color: white;
    text-decoration: none;
    letter-spacing: 0.02em;
    white-space: nowrap;
  }
  .header-divider {
    width: 1px; height: 24px;
    background: rgba(255,255,255,0.3);
    flex-shrink: 0;
  }
  .breadcrumb {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    flex-wrap: wrap;
    font-size: 0.78rem;
    overflow: hidden;
  }
  .bc-link { color: rgba(255,255,255,0.85); text-decoration: none; transition: color 0.2s; }
  .bc-link:hover { color: white; }
  .bc-sep { color: rgba(255,255,255,0.4); }
  .bc-current { color: white; font-weight: 500; }
  .main { max-width: 900px; margin: 0 auto; padding: 2.5rem 2rem 4rem; }
  .dir-header { margin-bottom: 2.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--border); }
  .dir-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    color: var(--soil-dark);
    font-weight: 600;
    line-height: 1.2;
    margin-bottom: 0.5rem;
  }
  .dir-path {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: var(--text-muted);
    background: rgba(92,58,30,0.06);
    padding: 0.3rem 0.7rem;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 0.8rem;
  }
  .dir-meta {
    font-size: 0.85rem;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
  }
  .back-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.82rem;
    color: var(--leaf);
    text-decoration: none;
    border: 1px solid var(--leaf-light);
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    transition: all 0.2s;
  }
  .back-btn:hover { background: var(--leaf); color: white; }
  .lang-switch {
    display: flex; align-items: center; gap: 0.4rem; flex-wrap: wrap;
    margin-top: 1rem;
  }
  .lang-switch-label {
    font-family: 'DM Mono', monospace; font-size: 0.62rem; font-weight: 500;
    letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-muted);
    margin-right: 0.2rem;
  }
  .lang-chip {
    font-size: 0.8rem; text-decoration: none; padding: 0.25rem 0.7rem;
    border-radius: 20px; border: 1px solid var(--border); color: var(--soil-mid);
    background: white; transition: all 0.18s;
  }
  .lang-chip:hover { border-color: var(--clay); color: var(--clay); }
  .lang-chip.current {
    background: var(--leaf); color: white; border-color: var(--leaf); cursor: default;
  }
  .section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    color: var(--text-muted);
    text-transform: uppercase;
    margin: 2rem 0 0.8rem;
    padding-left: 0.2rem;
  }
  .items-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 0.75rem;
  }
  .dir-card {
    display: flex;
    align-items: center;
    gap: 0.9rem;
    padding: 1rem 1.1rem;
    background: white;
    border: 1px solid var(--border);
    border-radius: 10px;
    text-decoration: none;
    color: var(--text-primary);
    transition: all 0.2s;
    box-shadow: var(--shadow);
  }
  .dir-card:hover {
    border-color: var(--clay);
    box-shadow: 0 4px 20px rgba(196,135,74,0.15);
    transform: translateY(-1px);
  }
  .item-icon { font-size: 1.5rem; flex-shrink: 0; }
  .item-info { flex: 1; min-width: 0; }
  .item-name { font-weight: 500; font-size: 0.9rem; color: var(--soil-mid); }
  .item-meta { font-family: 'DM Mono', monospace; font-size: 0.7rem; color: var(--text-muted); margin-top: 0.15rem; }
  .item-arrow { color: var(--clay); font-size: 1.2rem; flex-shrink: 0; }
  .items-list { display: flex; flex-direction: column; gap: 0.4rem; }
  .file-row {
    display: flex;
    align-items: center;
    gap: 0.9rem;
    padding: 0.75rem 1.1rem;
    background: white;
    border: 1px solid var(--border);
    border-radius: 8px;
    text-decoration: none;
    color: var(--text-primary);
    transition: all 0.15s;
  }
  .file-row:hover {
    border-color: var(--leaf-light);
    background: rgba(74,124,89,0.03);
    box-shadow: 0 2px 10px rgba(74,124,89,0.1);
  }
  .file-icon { font-size: 1.2rem; flex-shrink: 0; width: 28px; text-align: center; }
  .file-info { flex: 1; min-width: 0; }
  .file-name {
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    color: var(--soil-mid);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .file-display { font-size: 0.75rem; color: var(--text-muted); margin-top: 0.1rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .file-type {
    font-size: 0.68rem;
    font-family: 'DM Mono', monospace;
    color: var(--text-muted);
    background: var(--parchment);
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    flex-shrink: 0;
    border: 1px solid var(--border);
    white-space: nowrap;
  }
  .gh-badge {
    display: inline-block;
    font-size: 0.6rem;
    background: #24292e;
    color: #fff;
    padding: 0.1rem 0.35rem;
    border-radius: 3px;
    margin-left: 0.3rem;
    vertical-align: middle;
    font-family: "DM Mono", monospace;
  }
  .footer-link { color: var(--leaf); }
  .empty-state { text-align: center; padding: 4rem 2rem; color: var(--text-muted); }
  .empty-icon { font-size: 3rem; margin-bottom: 1rem; }
  .footer {
    text-align: center;
    padding: 2rem;
    font-size: 0.75rem;
    color: var(--text-muted);
    border-top: 1px solid var(--border);
    margin-top: 4rem;
    font-family: 'DM Mono', monospace;
  }
  @media (max-width: 600px) {
    .items-grid { grid-template-columns: 1fr; }
    .dir-title { font-size: 1.6rem; }
    .main { padding: 1.5rem 1rem 3rem; }
    .site-logo { font-size: 0.85rem; }
    .header-inner { height: auto; min-height: 60px; flex-wrap: wrap; padding: 0.6rem 0; gap: 0.3rem 1rem; }
    .header-divider { display: none; }
    .breadcrumb { width: 100%; }
  }
"""


# ── HTML generation ───────────────────────────────────────────────────────────

def generate_html(rel_path, subdirs, files, repo_root):
    """Generate a complete index.html for a directory."""

    if rel_path == Path(''):
        dir_name = "ubeccommon.github.io"
        repo_rel = ""
        parent_url = None
    else:
        dir_name = rel_path.name
        repo_rel  = str(rel_path).replace('\\', '/')
        parent    = rel_path.parent
        parent_url = BASE_URL + ('/' + str(parent).replace('\\','/') if str(parent) != '.' else '') + '/'

    breadcrumbs = build_breadcrumb(rel_path)
    brand, brand_sub, brand_icon = collection_brand(rel_path)

    # Language switch context (only inside a language subtree)
    current_code, available = lang_context(rel_path, repo_root)
    html_lang = LANG_HTML.get(current_code, 'en')
    hreflang_html = ''
    switcher_html = ''
    if current_code and len(available) >= 2:
        alt_links = [f'<link rel="alternate" hreflang="{LANG_HTML[c]}" href="{u}">'
                     for c, u in available]
        xdef = next((u for c, u in available if c == 'EN'), available[0][1])
        alt_links.append(f'<link rel="alternate" hreflang="x-default" href="{xdef}">')
        hreflang_html = '\n'.join(alt_links)

        chips = []
        for c, u in available:
            label = DIR_LABELS.get(c, c)
            if c == current_code:
                chips.append(f'<span class="lang-chip current">{label}</span>')
            else:
                chips.append(f'<a class="lang-chip" href="{u}">{label}</a>')
        switcher_html = ('<div class="lang-switch"><span class="lang-switch-label">'
                         'Languages</span>' + ''.join(chips) + '</div>')

    # Breadcrumb HTML
    bc_parts = []
    for i, (label, url) in enumerate(breadcrumbs):
        if i < len(breadcrumbs) - 1:
            bc_parts.append(f'<a href="{url}" class="bc-link">{label}</a><span class="bc-sep">›</span>')
        else:
            bc_parts.append(f'<span class="bc-current">{dir_name}</span>')
    bc_html = ''.join(bc_parts)

    # Subdirectory cards
    dirs_html = ''
    if subdirs:
        dirs_html = '<div class="section-label">DIRECTORIES</div><div class="items-grid">'
        for sd in sorted(subdirs):
            sd_url = f"{BASE_URL}/{repo_rel}/{sd}/" if repo_rel else f"{BASE_URL}/{sd}/"
            label  = dir_label(sd)
            dirs_html += f'''
            <a href="{sd_url}" class="item-card dir-card">
                <div class="item-icon">📁</div>
                <div class="item-info">
                    <div class="item-name">{label}</div>
                    <div class="item-meta">{sd}</div>
                </div>
                <div class="item-arrow">›</div>
            </a>'''
        dirs_html += '</div>'

    # File rows
    files_html = ''
    if files:
        files_html = '<div class="section-label">FILES</div><div class="items-list">'
        for f in sorted(files):
            icon, ftype = get_file_icon(f)
            url     = file_url(repo_rel, f)
            display = format_display(f)
            badge   = file_badge(f)
            files_html += f'''
            <a href="{url}" class="item-row file-row" target="_blank">
                <div class="file-icon">{icon}</div>
                <div class="file-info">
                    <div class="file-name">{f}</div>
                    <div class="file-display">{display}</div>
                </div>
                <div class="file-type">{ftype} {badge}</div>
            </a>'''
        files_html += '</div>'

    empty_html = ''
    if not subdirs and not files:
        empty_html = '<div class="empty-state"><div class="empty-icon">🌿</div><p>This directory is empty or under construction.</p></div>'

    back_btn = ''
    if parent_url:
        back_btn = f'<a href="{parent_url}" class="back-btn">← Parent Directory</a>'

    count_info = (f'{len(subdirs)} director{"ies" if len(subdirs)!=1 else "y"}, '
                  f'{len(files)} file{"s" if len(files)!=1 else ""}')

    dir_path_display = '/' + repo_rel if repo_rel else '/'

    return f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{dir_name} — {brand} · {brand_sub}</title>
{hreflang_html}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
{BASE_CSS}</style>
</head>
<body>
<header class="header">
  <div class="header-inner">
    <a href="{BASE_URL}/" class="site-logo">{brand_icon} {brand} — {brand_sub}</a>
    <div class="header-divider"></div>
    <nav class="breadcrumb">{bc_html}</nav>
  </div>
</header>
<main class="main">
  <div class="dir-header">
    <h1 class="dir-title">{dir_name}</h1>
    <div class="dir-path">{dir_path_display}</div>
    <div class="dir-meta">
      <span>{count_info}</span>
      {back_btn}
    </div>
    {switcher_html}
  </div>
  {dirs_html}
  {files_html}
  {empty_html}
</main>
<footer class="footer">
  {brand} · {brand_sub} · ubeccommon.github.io · <a href="{BASE_URL}/{RESOURCES_DIR}/" class="footer-link">Resource catalogue</a>
</footer>
</body>
</html>'''


# ── Main scan ─────────────────────────────────────────────────────────────────

def scan_and_generate(repo_root: Path, dry_run: bool = False):
    """Walk the entire repo and generate index.html for every directory."""
    generated = []
    skipped   = []

    for dirpath, dirnames, filenames in os.walk(repo_root):
        current = Path(dirpath)
        rel     = current.relative_to(repo_root)

        # Skip hidden/build directories (modify in-place to prevent os.walk descending)
        dirnames[:] = sorted(
            d for d in dirnames
            if d not in SKIP_DIRS and not d.startswith('.')
        )

        # Skip the root index.html (Jekyll's index.md handles that)
        if rel == Path('.') or str(rel) == '.':
            rel = Path('')
            # resources/ and catalogue/ are written by the OER layer
            dirnames[:] = [d for d in dirnames if d not in ROOT_SKIP_DIRS]

        # Filter files
        visible_files = sorted(
            f for f in filenames
            if f not in SKIP_FILES and not f.startswith('.')
        )

        html = generate_html(rel, dirnames[:], visible_files, repo_root)

        out_path = current / 'index.html'

        if dry_run:
            print(f"[DRY RUN] Would write: {out_path.relative_to(repo_root)}")
        else:
            out_path.write_text(html, encoding='utf-8')
            rel_str = str(rel) if str(rel) not in ('.', '') else '(root)'
            print(f"✓ {rel_str}/index.html  ({len(dirnames)}d, {len(visible_files)}f)")
            generated.append(str(out_path))

    # Skip root — Jekyll handles it
    root_index = repo_root / 'index.html'
    if root_index.exists() and not dry_run:
        root_index.unlink()
        print("✗ Removed root index.html (Jekyll's index.md takes precedence)")

    print(f"\n✅ Generated {len(generated)-1} index files")  # -1 for root removal
    return generated


# ══════════════════════════════════════════════════════════════════════════════
# OER publication layer (1.4.0)
# ══════════════════════════════════════════════════════════════════════════════
#
# Reads the YAML front matter of every published Markdown source and writes
# stable landing pages plus machine-readable catalogue files. Everything here
# is deterministic (no timestamps), so an unchanged tree produces unchanged
# files and the workflow commits nothing.

RESOURCES_DIR = 'resources'
CATALOGUE_DIR = 'catalogue'
GENERATOR_TAG = f'<meta name="generator" content="gen_indexes_dynamic.py {__version__}">'
GENERATOR_MARK = 'content="gen_indexes_dynamic.py'      # version-free, for cleanup
REPO_COMMITS = "https://github.com/ubeccommon/ubeccommon.github.io/commits/main"

# Top-level collection folder -> (url slug, collection name shown in the catalogue)
OER_COLLECTIONS = {
    'Pattern_Language_of_Place': ('erdpuls',    'Erdpuls OER Collection'),
    'Carpathian_OER_Commons':    ('carpathian', 'Carpathian OER Commons'),
}

# Folders whose Markdown is not a learning resource (authoring standards,
# templates, internal reports). Matched against any path segment.
OER_EXCLUDE_DIRS = {'standards', 'reports'}

LANG_NAMES    = {'en': 'English', 'de': 'Deutsch', 'uk': 'Українська', 'pl': 'Polski'}
LANG_NAMES_EN = {'en': 'English', 'de': 'German',  'uk': 'Ukrainian',  'pl': 'Polish'}
OER_LANG_ORDER = ['en', 'de', 'uk', 'pl']

# Licence as written in front matter (normalised) -> (SPDX, URL, full name)
LICENSES = {
    'CC BY-SA 4.0':    ('CC-BY-SA-4.0',    'https://creativecommons.org/licenses/by-sa/4.0/',
                        'Creative Commons Attribution-ShareAlike 4.0 International'),
    'CC BY-NC-SA 4.0': ('CC-BY-NC-SA-4.0', 'https://creativecommons.org/licenses/by-nc-sa/4.0/',
                        'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International'),
    'CC BY 4.0':       ('CC-BY-4.0',       'https://creativecommons.org/licenses/by/4.0/',
                        'Creative Commons Attribution 4.0 International'),
    'CC BY-NC 4.0':    ('CC-BY-NC-4.0',    'https://creativecommons.org/licenses/by-nc/4.0/',
                        'Creative Commons Attribution-NonCommercial 4.0 International'),
    'CC0 1.0':         ('CC0-1.0',         'https://creativecommons.org/publicdomain/zero/1.0/',
                        'Creative Commons CC0 1.0 Universal'),
}

# Fields OER Commons requires beyond title, URL, language and licence
OER_REQUIRED = ['description', 'keywords', 'educational_level', 'resource_type',
                'subject', 'audience']

# Month names in the four content languages (nominative), for "Month YYYY" dates
_MONTHS = [
    ('january',   'januar',    'styczeń',     'січень'),
    ('february',  'februar',   'luty',        'лютий'),
    ('march',     'märz',      'marzec',      'березень'),
    ('april',     'april',     'kwiecień',    'квітень'),
    ('may',       'mai',       'maj',         'травень'),
    ('june',      'juni',      'czerwiec',    'червень'),
    ('july',      'juli',      'lipiec',      'липень'),
    ('august',    'august',    'sierpień',    'серпень'),
    ('september', 'september', 'wrzesień',    'вересень'),
    ('october',   'oktober',   'październik', 'жовтень'),
    ('november',  'november',  'listopad',    'листопад'),
    ('december',  'dezember',  'grudzień',    'грудень'),
]
MONTHS = {name: i + 1 for i, names in enumerate(_MONTHS) for name in names}

# Interface words on landing pages, in the page's own language
LABELS = {
    'en': dict(read='Read online', pdf='Download PDF', md='Markdown source',
               about='About this resource', author='Author', publisher='Publisher',
               version='Version', date='Date', language='Language', licence='Licence',
               status='Status', level='Educational level', age='Age range',
               audience='Audience', type='Resource type', subject='Subject',
               keywords='Keywords', duration='Duration', languages='Available in',
               cite='How to cite', history='Version history', part_of='Part of',
               machine='Machine translation, to be reviewed', from_='Translated from',
               catalogue='Resource catalogue',
               pdf_old='The PDF is version {pdf}; the source is version {src}.'),
    'de': dict(read='Online lesen', pdf='PDF herunterladen', md='Markdown-Quelle',
               about='Über diese Ressource', author='Autor', publisher='Herausgeber',
               version='Version', date='Datum', language='Sprache', licence='Lizenz',
               status='Status', level='Bildungsstufe', age='Altersgruppe',
               audience='Zielgruppe', type='Materialart', subject='Fach',
               keywords='Schlagwörter', duration='Dauer', languages='Verfügbar in',
               cite='Zitiervorschlag', history='Versionsgeschichte', part_of='Teil von',
               machine='Maschinelle Übersetzung, wird geprüft', from_='Übersetzt aus',
               catalogue='Ressourcenkatalog',
               pdf_old='Das PDF ist Version {pdf}; die Quelle ist Version {src}.'),
    'uk': dict(read='Читати онлайн', pdf='Завантажити PDF', md='Джерело Markdown',
               about='Про цей ресурс', author='Автор', publisher='Видавець',
               version='Версія', date='Дата', language='Мова', licence='Ліцензія',
               status='Статус', level='Освітній рівень', age='Вік',
               audience='Аудиторія', type='Тип ресурсу', subject='Предмет',
               keywords='Ключові слова', duration='Тривалість', languages='Доступно мовами',
               cite='Як цитувати', history='Історія версій', part_of='Частина',
               machine='Машинний переклад, на перевірці', from_='Перекладено з',
               catalogue='Каталог ресурсів',
               pdf_old='PDF має версію {pdf}; джерело має версію {src}.'),
    'pl': dict(read='Czytaj online', pdf='Pobierz PDF', md='Źródło Markdown',
               about='O tym zasobie', author='Autor', publisher='Wydawca',
               version='Wersja', date='Data', language='Język', licence='Licencja',
               status='Status', level='Poziom edukacyjny', age='Przedział wiekowy',
               audience='Odbiorcy', type='Rodzaj zasobu', subject='Przedmiot',
               keywords='Słowa kluczowe', duration='Czas trwania', languages='Dostępne w językach',
               cite='Jak cytować', history='Historia wersji', part_of='Część',
               machine='Tłumaczenie maszynowe, do weryfikacji', from_='Przetłumaczono z',
               catalogue='Katalog zasobów',
               pdf_old='PDF ma wersję {pdf}; źródło ma wersję {src}.'),
}

LANDING_CSS = """
  .res-kicker { font-family: 'DM Mono', monospace; font-size: 0.7rem; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--text-muted); margin-bottom: 0.6rem; }
  .res-sub { font-size: 1.05rem; color: var(--soil-mid); margin-bottom: 1rem; }
  .res-desc { font-size: 0.98rem; line-height: 1.6; color: var(--text-primary); max-width: 68ch; }
  .res-actions { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0 0.4rem; }
  .btn { display: inline-flex; align-items: center; font-size: 0.85rem; text-decoration: none;
    padding: 0.45rem 1rem; border-radius: 20px; border: 1px solid var(--leaf-light);
    color: var(--leaf); background: white; transition: all 0.18s; }
  .btn:hover { background: var(--leaf); color: white; }
  .btn.primary { background: var(--leaf); color: white; border-color: var(--leaf); }
  .btn.primary:hover { background: var(--soil-mid); border-color: var(--soil-mid); }
  .notice { font-size: 0.8rem; color: var(--soil-mid); background: rgba(196,135,74,0.12);
    border: 1px solid rgba(196,135,74,0.35); border-radius: 6px; padding: 0.4rem 0.7rem;
    display: inline-block; margin: 0.5rem 0; }
  .meta-grid { display: grid; grid-template-columns: max-content 1fr; gap: 0.45rem 1.2rem;
    background: white; border: 1px solid var(--border); border-radius: 10px;
    padding: 1rem 1.2rem; box-shadow: var(--shadow); font-size: 0.88rem; }
  .meta-grid dt { color: var(--text-muted); font-family: 'DM Mono', monospace; font-size: 0.75rem;
    padding-top: 0.12rem; }
  .meta-grid dd { color: var(--text-primary); min-width: 0; overflow-wrap: anywhere; }
  .meta-grid a, .cite a, .plain-link { color: var(--leaf); }
  .cite { background: white; border: 1px solid var(--border); border-radius: 10px;
    padding: 0.9rem 1.2rem; font-size: 0.85rem; line-height: 1.55; overflow-wrap: anywhere; }
  .plain-link { font-size: 0.82rem; display: inline-block; margin-top: 1rem; }
  .work-row { display: flex; flex-wrap: wrap; align-items: center; gap: 0.6rem; padding: 0.8rem 1.1rem;
    background: white; border: 1px solid var(--border); border-radius: 8px; }
  .work-title { flex: 1 1 18rem; min-width: 0; font-size: 0.92rem; color: var(--soil-mid);
    text-decoration: none; font-weight: 500; }
  .work-title:hover { color: var(--clay); }
  .work-meta { font-family: 'DM Mono', monospace; font-size: 0.7rem; color: var(--text-muted); }
  @media (max-width: 600px) {
    .meta-grid { grid-template-columns: 1fr; gap: 0.1rem; }
    .meta-grid dd { margin-bottom: 0.5rem; }
  }
"""


# ── Front matter ──────────────────────────────────────────────────────────────

_FM_RE = re.compile(r'\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)', re.S)


def _scalar(raw):
    """One YAML scalar as the small reader understands it."""
    v = raw.strip()
    if not v or v in ('~', 'null', 'Null', 'NULL'):
        return None
    if v in ('true', 'True', 'TRUE'):
        return True
    if v in ('false', 'False', 'FALSE'):
        return False
    m = re.fullmatch(r'"((?:[^"\\]|\\.)*)"\s*(?:#.*)?', v)       # "text"  # comment
    if m:
        try:
            return json.loads(f'"{m.group(1)}"')
        except ValueError:
            return m.group(1)
    m = re.fullmatch(r"'((?:[^']|'')*)'\s*(?:#.*)?", v)          # 'text'  # comment
    if m:
        return m.group(1).replace("''", "'")
    return re.sub(r'\s+#.*$', '', v)            # unquoted: drop a trailing comment


def _split_flow(inner):
    """Split the inside of [a, "b, c", d] on top-level commas."""
    items, buf, quote_ch = [], '', None
    for ch in inner:
        if quote_ch:
            buf += ch
            if ch == quote_ch:
                quote_ch = None
        elif ch in '"\'':
            quote_ch = ch
            buf += ch
        elif ch == ',':
            items.append(buf)
            buf = ''
        else:
            buf += ch
    if buf.strip():
        items.append(buf)
    return [_scalar(i) for i in items if i.strip()]


def simple_yaml(text):
    """Flat `key: value` front matter, with [flow] and `- item` lists.

    Used only when PyYAML is not installed. Covers every construct the
    Erdpuls and Carpathian front matter uses; anything else is ignored.
    """
    data, key = {}, None
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        item = re.match(r'^\s+-\s+(.*)$', line)
        if item and key is not None:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(_scalar(item.group(1)))
            continue
        m = re.match(r'^([A-Za-z_][\w-]*)\s*:\s*(.*)$', line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if value.startswith('[') and value.rstrip().endswith(']'):
            data[key] = _split_flow(value.strip()[1:-1])
        else:
            data[key] = _scalar(value)
    return data


def read_front_matter(text):
    """Return (front matter dict or None, body text)."""
    m = _FM_RE.match(text)
    if not m:
        return None, text
    raw, data = m.group(1), None
    if yaml is not None:
        try:
            data = yaml.safe_load(raw)
        except yaml.YAMLError:
            data = None
    if not isinstance(data, dict):
        data = simple_yaml(raw)
    return (data or None), text[m.end():]


# ── Normalisers ───────────────────────────────────────────────────────────────

_LANG_SUFFIX_RE = re.compile(r'^(?P<base>.*?)_(?P<lang>EN|DE|UK|PL)(?:_v\d+(?:[._]\d+)*)?$')
_VERSION_RE     = re.compile(r'_v(\d+(?:[._]\d+)*)$')


def slugify(value):
    s = re.sub(r'[^0-9a-z]+', '-', str(value).lower())
    return s.strip('-')


def file_key(filename):
    """(work key, LANG) from a filename: language code and version stripped.

    module_utilities_water_EN_v0_4.md -> ('module-utilities-water', 'EN')
    """
    stem = Path(str(filename)).stem
    m = _LANG_SUFFIX_RE.match(stem)
    if m:
        return slugify(m.group('base')), m.group('lang')
    return slugify(_VERSION_RE.sub('', stem)), None


def file_version(filename):
    m = _VERSION_RE.search(Path(str(filename)).stem)
    return m.group(1).replace('_', '.') if m else None


def norm_version(value):
    if value is None:
        return None
    return str(value).strip().lstrip('vV') or None


def as_list(value):
    """A front-matter value as a list of non-empty strings."""
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(v).strip() for v in value if v is not None and str(v).strip()]
    return [p.strip() for p in str(value).split(',') if p.strip()]


def as_text(value):
    if value is None:
        return ''
    if isinstance(value, (list, tuple)):
        return ', '.join(as_list(value))
    return str(value).strip()


def iso_date(value, explicit=None):
    """ISO 8601 (YYYY, YYYY-MM or YYYY-MM-DD) from a front-matter date, or None."""
    for v in (explicit, value):
        if v is None:
            continue
        if hasattr(v, 'isoformat'):                       # YAML parsed a date
            return v.isoformat()[:10]
        s = str(v).strip()
        if not s or s.startswith('['):                    # template placeholder
            continue
        m = re.fullmatch(r'(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?', s)
        if m:
            return s
        m = re.fullmatch(r'([^\W\d_]+)\s+(\d{1,2}),?\s+(\d{4})', s)        # February 27, 2026
        if m and m.group(1).lower() in MONTHS:
            return f'{m.group(3)}-{MONTHS[m.group(1).lower()]:02d}-{int(m.group(2)):02d}'
        m = re.fullmatch(r'(\d{1,2})\.?\s+([^\W\d_]+)\s+(\d{4})', s)        # 27. Februar 2026
        if m and m.group(2).lower() in MONTHS:
            return f'{m.group(3)}-{MONTHS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}'
        m = re.fullmatch(r'([^\W\d_]+)\s+(\d{4})', s)                       # Februar 2026
        if m and m.group(1).lower() in MONTHS:
            return f'{m.group(2)}-{MONTHS[m.group(1).lower()]:02d}'
    return None


def licence_info(value):
    """(label, SPDX, URL, full name); SPDX and URL are None if unknown."""
    label = re.sub(r'\s+', ' ', as_text(value))
    for key, (spdx, url, name) in LICENSES.items():
        if label.upper() == key.upper():
            return key, spdx, url, name
    return label, None, None, label


def is_machine_translation(fm):
    if fm.get('machine_translated') is True:
        return True
    status = as_text(fm.get('status')).lower()
    return any(k in status for k in ('machine translation', 'maschinelle übersetzung',
                                     'машинний переклад', 'tłumaczenie maszynowe'))


def url_path(rel):
    return quote(str(rel).replace('\\', '/'), safe='/')


# ── Resource model ────────────────────────────────────────────────────────────

class Resource:
    """One published Markdown source: one work in one language."""

    def __init__(self, collection_dir, path, fm, pdfs):
        self.collection_dir = collection_dir
        self.coll_slug, self.coll_name = OER_COLLECTIONS[collection_dir]
        self.path = path                                   # repo-relative POSIX path
        self.fm = fm
        name = Path(path).name
        own_key, own_lang = file_key(name)
        self.file_key = own_key

        # Stable work id: explicit `id`; else this file's own name without
        # language and version (pairs translations named by the convention);
        # else, for a name without a language code, the name it was
        # translated from. `translated_from` may name a file since renamed,
        # so it never overrides a conventional filename.
        if fm.get('id'):
            self.rid = slugify(fm['id'])
            self.id_source = 'front matter'
        elif own_lang is None and fm.get('translated_from'):
            self.rid = file_key(fm['translated_from'])[0]
            self.id_source = 'translated_from'
        else:
            self.rid = own_key
            self.id_source = 'filename'

        lang = as_text(fm.get('lang')).lower()[:2] or (own_lang or 'en').lower()
        self.lang = lang
        self.title = as_text(fm.get('title'))
        self.subtitle = as_text(fm.get('subtitle'))
        self.description = as_text(fm.get('description') or fm.get('abstract'))
        self.author = as_text(fm.get('author'))
        self.publisher = as_text(fm.get('publisher'))
        self.project = as_text(fm.get('project') or fm.get('part_of'))
        self.status = as_text(fm.get('status'))
        self.version = norm_version(fm.get('version'))
        self.date = as_text(fm.get('date'))
        self.date_iso = iso_date(fm.get('date'), fm.get('date_iso'))
        (self.licence, self.licence_spdx,
         self.licence_url, self.licence_name) = licence_info(fm.get('license'))
        self.keywords = as_list(fm.get('keywords'))
        self.level = as_list(fm.get('educational_level'))
        self.age = as_text(fm.get('age_range'))
        self.audience = as_list(fm.get('audience'))
        self.rtype = as_list(fm.get('resource_type'))
        self.subject = as_list(fm.get('subject'))
        self.duration = as_text(fm.get('duration'))
        self.machine = is_machine_translation(fm)
        self.translated_from = as_text(fm.get('translated_from'))

        # Matching PDF: same filename key and language anywhere in the collection
        self.pdf = pdfs.get((collection_dir, own_key, (own_lang or lang.upper())))
        self.pdf_version = file_version(self.pdf) if self.pdf else None

    # URLs -------------------------------------------------------------------
    @property
    def work_url(self):
        return f"{BASE_URL}/{RESOURCES_DIR}/{self.coll_slug}/{self.rid}/"

    @property
    def url(self):
        return f"{self.work_url}{self.lang}/"

    @property
    def viewer_url(self):
        return f"{BASE_URL}/viewer.html?file={url_path(self.path)}"

    @property
    def raw_url(self):
        return f"{RAW_BASE}/{url_path(self.path)}"

    @property
    def pdf_url(self):
        return f"{BASE_URL}/{url_path(self.pdf)}" if self.pdf else None

    @property
    def history_url(self):
        return f"{REPO_COMMITS}/{url_path(self.path)}"

    def gaps(self):
        """Missing OER fields and other problems a cataloguer would hit."""
        out = [f for f, v in (('description', self.description), ('keywords', self.keywords),
                              ('educational_level', self.level), ('resource_type', self.rtype),
                              ('subject', self.subject), ('audience', self.audience)) if not v]
        if not self.licence_url:
            out.append('licence not recognised')
        if not self.date_iso:
            out.append('date not parseable')
        if not self.pdf:
            out.append('no PDF')
        elif self.pdf_version and self.version and self.pdf_version != self.version:
            out.append(f'PDF is v{self.pdf_version}, source v{self.version}')
        if self.id_source == 'filename':
            out.append('id from filename')
        return out


def is_template(fm):
    """Front matter still holding template placeholders such as [YYYY-MM-DD]."""
    return any(as_text(fm.get(k)).startswith('[') for k in ('title', 'date', 'status'))


def discover_resources(repo_root):
    """All publishable Markdown sources, grouped by (collection, id)."""
    pdfs = {}
    for coll in OER_COLLECTIONS:
        base = repo_root / coll
        if not base.is_dir():
            continue
        for p in sorted(base.rglob('*.pdf')):
            key, lang = file_key(p.name)
            if lang:
                pdfs.setdefault((coll, key, lang), p.relative_to(repo_root).as_posix())

    works, warnings = {}, []
    for coll in OER_COLLECTIONS:
        base = repo_root / coll
        if not base.is_dir():
            continue
        for p in sorted(base.rglob('*.md')):
            rel = p.relative_to(repo_root)
            parts = set(rel.parts[:-1])
            if parts & (OER_EXCLUDE_DIRS | SKIP_DIRS) or any(x.startswith('.') for x in rel.parts):
                continue
            fm, _ = read_front_matter(p.read_text(encoding='utf-8', errors='replace'))
            if not fm or not fm.get('title') or not fm.get('license') or is_template(fm):
                continue
            if fm.get('oer') is False:                     # `oer: false` opts a file out
                continue
            r = Resource(coll, rel.as_posix(), fm, pdfs)
            langs = works.setdefault((coll, r.rid), {})
            if r.lang in langs:
                warnings.append(f"duplicate {r.coll_slug}/{r.rid}/{r.lang}: "
                                f"{langs[r.lang].path} kept, {r.path} skipped")
                continue
            langs[r.lang] = r
    return works, warnings


def ordered(langs):
    """Language versions of one work in display order."""
    rank = {c: i for i, c in enumerate(OER_LANG_ORDER)}
    return [langs[c] for c in sorted(langs, key=lambda c: (rank.get(c, 99), c))]


def lead(langs):
    """The version that names a work: English if present, else the first."""
    return langs.get('en') or ordered(langs)[0]


# ── JSON-LD ───────────────────────────────────────────────────────────────────

def jsonld(r, langs):
    """schema.org LearningResource (LRMI) record for one language version."""
    d = {
        '@context': 'https://schema.org',
        '@type': ['LearningResource', 'CreativeWork'],
        '@id': r.url,
        'url': r.url,
        'identifier': f'{r.coll_slug}/{r.rid}/{r.lang}',
        'name': r.title,
        'inLanguage': r.lang,
        'isAccessibleForFree': True,
    }
    if r.subtitle:
        d['alternativeHeadline'] = r.subtitle
    if r.description:
        d['description'] = r.description
    if r.licence_url:
        d['license'] = r.licence_url
    if r.author:
        d['author'] = {'@type': 'Person', 'name': r.author}
    if r.publisher:
        d['publisher'] = {'@type': 'Organization', 'name': r.publisher}
    if r.version:
        d['version'] = r.version
    if r.date_iso:
        d['datePublished'] = r.date_iso
    if r.status:
        d['creativeWorkStatus'] = r.status
    if r.keywords:
        d['keywords'] = r.keywords
    if r.level:
        d['educationalLevel'] = r.level
    if r.age:
        d['typicalAgeRange'] = r.age
    if r.audience:
        d['audience'] = [{'@type': 'EducationalAudience', 'educationalRole': a} for a in r.audience]
    if r.rtype:
        d['learningResourceType'] = r.rtype
    if r.subject:
        d['about'] = [{'@type': 'Thing', 'name': s} for s in r.subject]
    d['isPartOf'] = {'@type': 'Collection', 'name': r.coll_name,
                     'url': f"{BASE_URL}/{RESOURCES_DIR}/{r.coll_slug}/"}
    enc = [{'@type': 'MediaObject', 'contentUrl': r.raw_url, 'encodingFormat': 'text/markdown'}]
    if r.pdf_url:
        enc.append({'@type': 'MediaObject', 'contentUrl': r.pdf_url,
                    'encodingFormat': 'application/pdf'})
    d['encoding'] = enc
    # The lead version (English, else the first) is the original; the others
    # are its translations.
    original = lead(langs)
    if r is original:
        others = [o for o in ordered(langs) if o is not r]
        if others:
            d['workTranslation'] = [{'@id': o.url} for o in others]
    else:
        d['translationOfWork'] = {'@id': original.url}
    return d


def script_json(obj):
    """JSON safe to place inside <script type="application/ld+json">."""
    return json.dumps(obj, ensure_ascii=False, indent=2).replace('</', '<\\/')


# ── Page building ─────────────────────────────────────────────────────────────

def page_shell(*, lang, title, description, brand_dir, crumbs, body, head_extra=''):
    """A complete HTML page in the look of the directory indexes."""
    brand, brand_sub, brand_icon = collection_brand(Path(brand_dir) if brand_dir else Path(''))
    bc = []
    for i, (label, url) in enumerate(crumbs):
        if i < len(crumbs) - 1:
            bc.append(f'<a href="{url}" class="bc-link">{escape(label)}</a><span class="bc-sep">›</span>')
        else:
            bc.append(f'<span class="bc-current">{escape(label)}</span>')
    meta_desc = f'\n<meta name="description" content="{escape(description)}">' if description else ''
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)} — {brand} · {brand_sub}</title>{meta_desc}
{GENERATOR_TAG}
{head_extra}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
{BASE_CSS}{LANDING_CSS}</style>
</head>
<body>
<header class="header">
  <div class="header-inner">
    <a href="{BASE_URL}/" class="site-logo">{brand_icon} {brand} — {brand_sub}</a>
    <div class="header-divider"></div>
    <nav class="breadcrumb">{''.join(bc)}</nav>
  </div>
</header>
<main class="main">
{body}
</main>
<footer class="footer">
  {brand} · {brand_sub} · ubeccommon.github.io · <a href="{BASE_URL}/{RESOURCES_DIR}/" class="footer-link">Resource catalogue</a>
</footer>
</body>
</html>
'''


def hreflang_links(langs):
    """One alternate set shared by every page of a work. The language-neutral
    work page, which lets the reader choose, is the x-default."""
    rs = ordered(langs)
    if len(rs) < 2:
        return ''
    links = [f'<link rel="alternate" hreflang="{r.lang}" href="{r.url}">' for r in rs]
    links.append(f'<link rel="alternate" hreflang="x-default" href="{lead(langs).work_url}">')
    return '\n'.join(links)


def lang_chips(langs, current, label):
    rs = ordered(langs)
    if len(rs) < 2:
        return ''
    chips = []
    for r in rs:
        name = escape(LANG_NAMES.get(r.lang, r.lang))
        if r is current:
            chips.append(f'<span class="lang-chip current">{name}</span>')
        else:
            chips.append(f'<a class="lang-chip" href="{r.url}" hreflang="{r.lang}" lang="{r.lang}">{name}</a>')
    return (f'<div class="lang-switch"><span class="lang-switch-label">{escape(label)}</span>'
            + ''.join(chips) + '</div>')


def citation(r):
    year = (r.date_iso or '')[:4]
    who = r.author or r.publisher or r.coll_name
    parts = [f'{escape(who)}{f" ({year})" if year else ""}.', f'<em>{escape(r.title)}</em>.']
    if r.version:
        parts.append(f'{escape(LABELS.get(r.lang, LABELS["en"])["version"])} {escape(r.version)}.')
    parts.append(f'{escape(r.coll_name)}.')
    if r.licence_url:
        parts.append(f'<a href="{r.licence_url}">{escape(r.licence)}</a>.')
    else:
        parts.append(f'{escape(r.licence)}.')
    parts.append(f'<a href="{r.url}">{r.url}</a>')
    return ' '.join(parts)


def resource_page(r, langs):
    L = LABELS.get(r.lang, LABELS['en'])
    rows = []

    def row(label, value_html):
        if value_html:
            rows.append(f'<dt>{escape(label)}</dt><dd>{value_html}</dd>')

    row(L['author'], escape(r.author))
    row(L['publisher'], escape(r.publisher))
    row(L['version'], escape(r.version or ''))
    row(L['date'], escape(r.date) if r.date and not r.date.startswith('[') else '')
    row(L['language'], escape(LANG_NAMES.get(r.lang, r.lang)))
    row(L['licence'], f'<a href="{r.licence_url}" rel="license">{escape(r.licence_name)}</a>'
        if r.licence_url else escape(r.licence))
    row(L['level'], escape(', '.join(r.level)))
    row(L['age'], escape(r.age))
    row(L['audience'], escape(', '.join(r.audience)))
    row(L['type'], escape(', '.join(r.rtype)))
    row(L['subject'], escape(', '.join(r.subject)))
    row(L['duration'], escape(r.duration))
    row(L['keywords'], escape(', '.join(r.keywords)))
    row(L['part_of'], escape(r.project) if r.project and r.project != r.coll_name else '')
    row(L['status'], escape(r.status))
    if r.translated_from and 'en' in langs and r.lang != 'en':
        src = langs['en']
        row(L['from_'], f'<a href="{src.url}" hreflang="en">{escape(src.title)}</a>')

    actions = [f'<a class="btn primary" href="{r.viewer_url}">{escape(L["read"])}</a>']
    if r.pdf_url:
        actions.append(f'<a class="btn" href="{r.pdf_url}" download>{escape(L["pdf"])}</a>')
    actions.append(f'<a class="btn" href="{r.raw_url}">{escape(L["md"])}</a>')

    notices = []
    if r.machine:
        notices.append(f'<div class="notice">{escape(L["machine"])}</div>')
    if r.pdf_version and r.version and r.pdf_version != r.version:
        notices.append('<div class="notice">'
                       + escape(L['pdf_old'].format(pdf=r.pdf_version, src=r.version)) + '</div>')

    body = f'''  <div class="dir-header">
    <div class="res-kicker">{escape(r.coll_name)} · {escape(LANG_NAMES.get(r.lang, r.lang))}</div>
    <h1 class="dir-title">{escape(r.title)}</h1>
    {f'<p class="res-sub">{escape(r.subtitle)}</p>' if r.subtitle else ''}
    <div class="res-actions">{''.join(actions)}</div>
    {''.join(notices)}
    {lang_chips(langs, r, L['languages'])}
  </div>
  {f'<p class="res-desc">{escape(r.description)}</p>' if r.description else ''}
  <div class="section-label">{escape(L["about"])}</div>
  <dl class="meta-grid">
    {chr(10).join("    " + x for x in rows).strip()}
  </dl>
  <div class="section-label">{escape(L["cite"])}</div>
  <div class="cite">{citation(r)}</div>
  <a class="plain-link" href="{r.history_url}">{escape(L["history"])} ↗</a>'''

    head = (hreflang_links(langs) + '\n<script type="application/ld+json">\n'
            + script_json(jsonld(r, langs)) + '\n</script>')
    crumbs = [('🏠 Root', BASE_URL + '/'),
              (L['catalogue'], f'{BASE_URL}/{RESOURCES_DIR}/'),
              (r.coll_name, f'{BASE_URL}/{RESOURCES_DIR}/{r.coll_slug}/'),
              (r.rid, r.work_url),
              (r.lang.upper(), r.url)]
    return page_shell(lang=r.lang, title=r.title, description=r.description or r.subtitle,
                      brand_dir=r.collection_dir, crumbs=crumbs, body=body, head_extra=head)


def work_row(langs):
    """One row for a work in a listing: title, languages, version."""
    first = lead(langs)
    chips = ''.join(f'<a class="lang-chip" href="{r.url}" hreflang="{r.lang}">{r.lang.upper()}</a>'
                    for r in ordered(langs))
    meta = f'v{escape(first.version)}' if first.version else ''
    return (f'<div class="work-row"><a class="work-title" href="{first.work_url}">{escape(first.title)}</a>'
            f'<span class="work-meta">{meta}</span>{chips}</div>')


def work_page(langs):
    first = lead(langs)
    items = []
    for r in ordered(langs):
        L = LABELS.get(r.lang, LABELS['en'])
        bits = [escape(LANG_NAMES.get(r.lang, r.lang))]
        if r.version:
            bits.append(f'v{escape(r.version)}')
        if r.machine:
            bits.append(escape(L['machine']))
        items.append(f'<div class="work-row" lang="{r.lang}"><a class="work-title" href="{r.url}" '
                     f'hreflang="{r.lang}">{escape(r.title)}</a>'
                     f'<span class="work-meta">{" · ".join(bits)}</span></div>')
    body = f'''  <div class="dir-header">
    <div class="res-kicker">{escape(first.coll_name)}</div>
    <h1 class="dir-title">{escape(first.title)}</h1>
    {f'<p class="res-sub">{escape(first.subtitle)}</p>' if first.subtitle else ''}
  </div>
  {f'<p class="res-desc">{escape(first.description)}</p>' if first.description else ''}
  <div class="section-label">{escape(LABELS["en"]["languages"])}</div>
  <div class="items-list">
    {chr(10).join(items)}
  </div>'''
    crumbs = [('🏠 Root', BASE_URL + '/'),
              (LABELS['en']['catalogue'], f'{BASE_URL}/{RESOURCES_DIR}/'),
              (first.coll_name, f'{BASE_URL}/{RESOURCES_DIR}/{first.coll_slug}/'),
              (first.rid, first.work_url)]
    return page_shell(lang=first.lang, title=first.title,
                      description=first.description or first.subtitle,
                      brand_dir=first.collection_dir, crumbs=crumbs, body=body,
                      head_extra=hreflang_links(langs))


def collection_page(coll, slug, name, coll_works):
    rows = [work_row(langs) for _, langs in
            sorted(coll_works.items(), key=lambda kv: lead(kv[1]).title.lower())]
    versions = sum(len(v) for v in coll_works.values())
    body = f'''  <div class="dir-header">
    <h1 class="dir-title">{escape(name)}</h1>
    <div class="dir-meta"><span>{len(coll_works)} works, {versions} language versions</span>
      <a href="{BASE_URL}/{coll}/" class="back-btn">Browse folders</a></div>
  </div>
  <div class="items-list">
    {chr(10).join(rows)}
  </div>'''
    crumbs = [('🏠 Root', BASE_URL + '/'),
              (LABELS['en']['catalogue'], f'{BASE_URL}/{RESOURCES_DIR}/'),
              (name, f'{BASE_URL}/{RESOURCES_DIR}/{slug}/')]
    return page_shell(lang='en', title=name, description=f'{name}: open educational resources',
                      brand_dir=coll, crumbs=crumbs, body=body)


def catalogue_page(by_coll):
    cards = []
    for coll, (slug, name) in OER_COLLECTIONS.items():
        cw = by_coll.get(coll, {})
        if not cw:
            continue
        versions = sum(len(v) for v in cw.values())
        cards.append(f'''
    <a href="{BASE_URL}/{RESOURCES_DIR}/{slug}/" class="item-card dir-card">
      <div class="item-info">
        <div class="item-name">{escape(name)}</div>
        <div class="item-meta">{len(cw)} works · {versions} language versions</div>
      </div>
      <div class="item-arrow">›</div>
    </a>''')
    body = f'''  <div class="dir-header">
    <h1 class="dir-title">Resource catalogue</h1>
    <div class="dir-meta"><span>Every open educational resource on this site, with stable links.</span></div>
  </div>
  <div class="items-grid">{''.join(cards)}
  </div>
  <a class="plain-link" href="{BASE_URL}/{CATALOGUE_DIR}/catalogue.json">catalogue.json (schema.org / LRMI)</a>'''
    crumbs = [('🏠 Root', BASE_URL + '/'), ('Resource catalogue', f'{BASE_URL}/{RESOURCES_DIR}/')]
    return page_shell(lang='en', title='Resource catalogue',
                      description='Catalogue of open educational resources on ubeccommon.github.io',
                      brand_dir='', crumbs=crumbs, body=body)


# ── Machine-readable outputs ──────────────────────────────────────────────────

OER_COMMONS_COLUMNS = ['Title', 'URL', 'Material Type', 'Sub-level', 'Abstract', 'Language',
                       'COU Title', 'Primary User', 'Subject', 'Keyword', 'Provider', 'Author',
                       'Creation Date', 'Media Format', 'Copyright Holder', 'Version']


def oer_commons_rows(resources):
    """Rows in OER Commons bulk-import field order; multi-values joined by |."""
    for r in resources:
        yield {
            'Title': r.title,
            'URL': r.url,
            'Material Type': '|'.join(r.rtype),
            'Sub-level': '|'.join(r.level),
            'Abstract': r.description,
            'Language': LANG_NAMES_EN.get(r.lang, r.lang),
            'COU Title': r.licence_name,
            'Primary User': '|'.join(r.audience),
            'Subject': '|'.join(r.subject),
            'Keyword': '|'.join(r.keywords),
            'Provider': r.publisher or r.coll_name,
            'Author': r.author,
            'Creation Date': r.date_iso or '',
            'Media Format': 'Downloadable docs' if r.pdf else '',
            'Copyright Holder': r.author or r.publisher,
            'Version': r.version or '',
        }


def csv_text(columns, rows):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=columns, lineterminator='\n')
    w.writeheader()
    for row in rows:
        w.writerow(row)
    return buf.getvalue()


def sitemap_xml(urls):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod in urls:
        lm = f'<lastmod>{lastmod}</lastmod>' if lastmod else ''
        lines.append(f'  <url><loc>{escape(loc)}</loc>{lm}</url>')
    lines.append('</urlset>')
    return '\n'.join(lines) + '\n'


ROBOTS_MARK = '# generated by gen_indexes_dynamic.py'


def robots_txt():
    return f'{ROBOTS_MARK}\nUser-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n'


# ── Writing ───────────────────────────────────────────────────────────────────

def _write(path, text, written, dry_run):
    written.add(path.resolve())
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding='utf-8') != text:
        path.write_text(text, encoding='utf-8')


def _prune(repo_root, written, dry_run):
    """Remove generated pages under resources/ that no longer belong to a work."""
    removed = 0
    base = repo_root / RESOURCES_DIR
    if not base.is_dir():
        return removed
    for p in sorted(base.rglob('index.html')):
        if p.resolve() in written:
            continue
        if GENERATOR_MARK in p.read_text(encoding='utf-8', errors='replace'):
            removed += 1
            if not dry_run:
                p.unlink()
    if not dry_run:
        for d in sorted((d for d in base.rglob('*') if d.is_dir()), key=lambda d: -len(d.parts)):
            if not any(d.iterdir()):
                d.rmdir()
    return removed


def build_oer_layer(repo_root, dry_run=False, report=None):
    works, warnings = discover_resources(repo_root)
    by_coll = {}
    for (coll, rid), langs in works.items():
        by_coll.setdefault(coll, {})[rid] = langs

    written, sitemap = set(), []
    res_root = repo_root / RESOURCES_DIR
    all_versions = []

    for coll, coll_works in by_coll.items():
        slug, name = OER_COLLECTIONS[coll]
        _write(res_root / slug / 'index.html', collection_page(coll, slug, name, coll_works),
               written, dry_run)
        sitemap.append((f'{BASE_URL}/{RESOURCES_DIR}/{slug}/', None))
        for rid, langs in sorted(coll_works.items()):
            _write(res_root / slug / rid / 'index.html', work_page(langs), written, dry_run)
            sitemap.append((lead(langs).work_url, None))
            for r in ordered(langs):
                _write(res_root / slug / rid / r.lang / 'index.html', resource_page(r, langs),
                       written, dry_run)
                sitemap.append((r.url, r.date_iso))
                all_versions.append((r, langs))

    _write(res_root / 'index.html', catalogue_page(by_coll), written, dry_run)
    sitemap.insert(0, (f'{BASE_URL}/{RESOURCES_DIR}/', None))

    records = [jsonld(r, langs) for r, langs in all_versions]
    graph = {'@context': 'https://schema.org',
             '@graph': [{k: v for k, v in d.items() if k != '@context'} for d in records]}
    cat = repo_root / CATALOGUE_DIR
    _write(cat / 'catalogue.json', json.dumps(graph, ensure_ascii=False, indent=2) + '\n',
           written, dry_run)
    resources = [r for r, _ in all_versions]
    _write(cat / 'oer_commons.csv', csv_text(OER_COMMONS_COLUMNS, oer_commons_rows(resources)),
           written, dry_run)
    _write(repo_root / 'sitemap.xml', sitemap_xml(sitemap), written, dry_run)

    robots = repo_root / 'robots.txt'
    if not robots.exists() or robots.read_text(encoding='utf-8').startswith(ROBOTS_MARK):
        _write(robots, robots_txt(), written, dry_run)
    else:
        warnings.append('robots.txt exists and was not written by this script; left as is '
                        f'(add "Sitemap: {BASE_URL}/sitemap.xml" by hand)')

    removed = _prune(repo_root, written, dry_run)

    # Report -----------------------------------------------------------------
    gap_rows = []
    for r in resources:
        g = r.gaps()
        gap_rows.append({'collection': r.coll_slug, 'id': r.rid, 'lang': r.lang,
                         'url': r.url, 'source': r.path, 'gaps': '; '.join(g)})
    if report:
        Path(report).parent.mkdir(parents=True, exist_ok=True)
        Path(report).write_text(csv_text(['collection', 'id', 'lang', 'url', 'source', 'gaps'],
                                         gap_rows), encoding='utf-8')

    counts = {}
    for r in resources:
        for g in r.gaps():
            key = 'PDF version differs from source' if g.startswith('PDF is v') else g
            counts[key] = counts.get(key, 0) + 1
    ready = sum(1 for r in resources if not any(f in r.gaps() for f in OER_REQUIRED))

    verb = '[DRY RUN] would write' if dry_run else 'Wrote'
    print(f"\n📚 OER layer: {len(works)} works, {len(resources)} language versions "
          f"in {len(by_coll)} collections")
    print(f"   {verb} {len(written)} files under {RESOURCES_DIR}/, {CATALOGUE_DIR}/, "
          f"sitemap.xml, robots.txt; {removed} stale page(s) removed")
    print(f"   OER Commons-ready (all required fields present): {ready} of {len(resources)}")
    for k, v in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"   - {k}: {v}")
    for w in warnings:
        print(f"   ⚠ {w}")
    if report:
        print(f"   Gap report: {report}")
    return works


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Erdpuls OER directory indexes')
    parser.add_argument('--repo-root', default='.', help='Path to repo root (default: current directory)')
    parser.add_argument('--dry-run', action='store_true', help='Print actions without writing files')
    parser.add_argument('--no-oer', action='store_true',
                        help='Directory indexes only; skip landing pages and catalogue files')
    parser.add_argument('--report', metavar='PATH',
                        help='Write a CSV of missing OER metadata per resource to PATH')
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    print(f"📂 Scanning: {repo_root}")
    print(f"🌐 Base URL: {BASE_URL}\n")

    scan_and_generate(repo_root, dry_run=args.dry_run)
    if not args.no_oer:
        build_oer_layer(repo_root, dry_run=args.dry_run, report=args.report)
