#!/usr/bin/env python3
"""
Erdpuls OER — Dynamic Index Generator
======================================
Scans the repository filesystem and generates index.html for every directory.
Skips Jekyll internals, build artifacts, and the generated files themselves.

Usage:
    python gen_indexes_dynamic.py [--repo-root PATH] [--dry-run]

Called automatically by GitHub Actions on every push.
"""

import os
import argparse
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────

BASE_URL    = "https://ubeccommon.github.io"
GITHUB_BLOB = "https://github.com/ubeccommon/ubeccommon.github.io/blob/main"
RAW_BASE    = "https://raw.githubusercontent.com/ubeccommon/ubeccommon.github.io/main"

# Directories to skip entirely (never generate an index inside these)
SKIP_DIRS = {
    '.git', '.github', '_site', '_includes', '_layouts',
    '_sass', '_data', 'node_modules', '__pycache__', '.jekyll-cache',
}

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
    'soil_art':                 '🎨 Soil Art',
    'soil_questions':           '❓ Soil Questions',
    'soil':                     '🌱 Soil',
    'audit':                    '✅ Audit',
    'pdf':                      '📕 PDF',
    'docs':                     '📚 Docs',
    'oer':                      '🔓 OER',
    'standards':                '📐 Standards',
    'reports':                  '📊 Reports',
    'Learning_Pathways':        '🗺️ Learning Pathways',
    'Pattern_Language_of_Place':'🏛️ Pattern Language of Place',
}

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


# ── HTML generation ───────────────────────────────────────────────────────────

def generate_html(rel_path, subdirs, files):
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
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{dir_name} — Erdpuls OER Repository</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root {{
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
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'DM Sans', sans-serif;
    background: var(--parchment);
    color: var(--text-primary);
    min-height: 100vh;
    background-image:
      radial-gradient(ellipse at 20% 50%, rgba(196,135,74,0.08) 0%, transparent 60%),
      radial-gradient(ellipse at 80% 20%, rgba(74,124,89,0.06) 0%, transparent 50%);
  }}
  .header {{
    background: linear-gradient(120deg, #155799 0%, #159957 100%);
    color: white;
    padding: 0 2rem;
    position: sticky;
    top: 0;
    z-index: 100;
    border-bottom: none;
  }}
  .header-inner {{
    max-width: 900px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    gap: 1rem;
    height: 60px;
  }}
  .site-logo {{
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    color: white;
    text-decoration: none;
    letter-spacing: 0.02em;
    white-space: nowrap;
  }}
  .header-divider {{
    width: 1px; height: 24px;
    background: rgba(255,255,255,0.3);
    flex-shrink: 0;
  }}
  .breadcrumb {{
    display: flex;
    align-items: center;
    gap: 0.4rem;
    flex-wrap: wrap;
    font-size: 0.78rem;
    overflow: hidden;
  }}
  .bc-link {{ color: rgba(255,255,255,0.85); text-decoration: none; transition: color 0.2s; }}
  .bc-link:hover {{ color: white; }}
  .bc-sep {{ color: rgba(255,255,255,0.4); }}
  .bc-current {{ color: white; font-weight: 500; }}
  .main {{ max-width: 900px; margin: 0 auto; padding: 2.5rem 2rem 4rem; }}
  .dir-header {{ margin-bottom: 2.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--border); }}
  .dir-title {{
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    color: var(--soil-dark);
    font-weight: 600;
    line-height: 1.2;
    margin-bottom: 0.5rem;
  }}
  .dir-path {{
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: var(--text-muted);
    background: rgba(92,58,30,0.06);
    padding: 0.3rem 0.7rem;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 0.8rem;
  }}
  .dir-meta {{
    font-size: 0.85rem;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
  }}
  .back-btn {{
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
  }}
  .back-btn:hover {{ background: var(--leaf); color: white; }}
  .section-label {{
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    color: var(--text-muted);
    text-transform: uppercase;
    margin: 2rem 0 0.8rem;
    padding-left: 0.2rem;
  }}
  .items-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 0.75rem;
  }}
  .dir-card {{
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
  }}
  .dir-card:hover {{
    border-color: var(--clay);
    box-shadow: 0 4px 20px rgba(196,135,74,0.15);
    transform: translateY(-1px);
  }}
  .item-icon {{ font-size: 1.5rem; flex-shrink: 0; }}
  .item-info {{ flex: 1; min-width: 0; }}
  .item-name {{ font-weight: 500; font-size: 0.9rem; color: var(--soil-mid); }}
  .item-meta {{ font-family: 'DM Mono', monospace; font-size: 0.7rem; color: var(--text-muted); margin-top: 0.15rem; }}
  .item-arrow {{ color: var(--clay); font-size: 1.2rem; flex-shrink: 0; }}
  .items-list {{ display: flex; flex-direction: column; gap: 0.4rem; }}
  .file-row {{
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
  }}
  .file-row:hover {{
    border-color: var(--leaf-light);
    background: rgba(74,124,89,0.03);
    box-shadow: 0 2px 10px rgba(74,124,89,0.1);
  }}
  .file-icon {{ font-size: 1.2rem; flex-shrink: 0; width: 28px; text-align: center; }}
  .file-info {{ flex: 1; min-width: 0; }}
  .file-name {{
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    color: var(--soil-mid);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .file-display {{ font-size: 0.75rem; color: var(--text-muted); margin-top: 0.1rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  .file-type {{
    font-size: 0.68rem;
    font-family: 'DM Mono', monospace;
    color: var(--text-muted);
    background: var(--parchment);
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    flex-shrink: 0;
    border: 1px solid var(--border);
    white-space: nowrap;
  }}
  .gh-badge {{
    display: inline-block;
    font-size: 0.6rem;
    background: #24292e;
    color: #fff;
    padding: 0.1rem 0.35rem;
    border-radius: 3px;
    margin-left: 0.3rem;
    vertical-align: middle;
    font-family: "DM Mono", monospace;
  }}
  .empty-state {{ text-align: center; padding: 4rem 2rem; color: var(--text-muted); }}
  .empty-icon {{ font-size: 3rem; margin-bottom: 1rem; }}
  .footer {{
    text-align: center;
    padding: 2rem;
    font-size: 0.75rem;
    color: var(--text-muted);
    border-top: 1px solid var(--border);
    margin-top: 4rem;
    font-family: 'DM Mono', monospace;
  }}
  @media (max-width: 600px) {{
    .items-grid {{ grid-template-columns: 1fr; }}
    .dir-title {{ font-size: 1.6rem; }}
    .main {{ padding: 1.5rem 1rem 3rem; }}
    .site-logo {{ font-size: 0.85rem; }}
  }}
</style>
</head>
<body>
<header class="header">
  <div class="header-inner">
    <a href="{BASE_URL}/" class="site-logo">🌱 Erdpuls Müllrose — Open Educational Resources</a>
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
  </div>
  {dirs_html}
  {files_html}
  {empty_html}
</main>
<footer class="footer">
  Erdpuls Müllrose · Open Educational Resources · ubeccommon.github.io
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

        # Filter files
        visible_files = sorted(
            f for f in filenames
            if f not in SKIP_FILES and not f.startswith('.')
        )

        html = generate_html(rel, dirnames[:], visible_files)

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


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Erdpuls OER directory indexes')
    parser.add_argument('--repo-root', default='.', help='Path to repo root (default: current directory)')
    parser.add_argument('--dry-run', action='store_true', help='Print actions without writing files')
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    print(f"📂 Scanning: {repo_root}")
    print(f"🌐 Base URL: {BASE_URL}\n")

    scan_and_generate(repo_root, dry_run=args.dry_run)
