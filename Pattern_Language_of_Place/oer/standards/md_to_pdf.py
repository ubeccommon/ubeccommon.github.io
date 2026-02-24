#!/usr/bin/env python3
"""
md_to_pdf.py — Markdown to PDF with proper frontmatter, \newpage, and styling.
Usage: python3 md_to_pdf.py input.md output.pdf [optional_style.css]
"""

import sys
import re
from pathlib import Path
import markdown
from weasyprint import HTML

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

try:
    from pygments.formatters import HtmlFormatter
    HAS_PYGMENTS = True
except ImportError:
    HAS_PYGMENTS = False


def extract_frontmatter(text):
    """Strip YAML frontmatter and return (meta_dict, body_text)."""
    meta = {}
    body = text

    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            yaml_block = text[3:end].strip()
            body = text[end + 4:].lstrip()
            if HAS_YAML:
                try:
                    meta = yaml.safe_load(yaml_block) or {}
                except Exception:
                    pass
            else:
                # Minimal parser fallback
                for line in yaml_block.splitlines():
                    if ":" in line:
                        k, _, v = line.partition(":")
                        meta[k.strip()] = v.strip().strip('"').strip("'")

    return meta, body





def clean_body(text):
    """Remove Pandoc-specific artifacts that don't render in standard Markdown."""
    # Strip raw latex/html blocks: ```{=latex}...``` or ```{=html}...```
    text = re.sub(r'```\{=[a-z]+\}.*?```', '', text, flags=re.DOTALL)
    return text.strip()



    """Build an HTML title block from frontmatter metadata."""
    if not meta:
        return ""

    parts = []
    if meta.get("title"):
        parts.append(f'<h1 class="doc-title">{meta["title"]}</h1>')
    if meta.get("subtitle"):
        parts.append(f'<p class="doc-subtitle">{meta["subtitle"]}</p>')

    details = []
    if meta.get("author"):
        details.append(f'<span class="meta-author">{meta["author"]}</span>')
    if meta.get("date"):
        details.append(f'<span class="meta-date">{meta["date"]}</span>')
    if meta.get("version"):
        details.append(f'<span class="meta-version">Version {meta["version"]}</span>')
    if meta.get("license"):
        details.append(f'<span class="meta-license">{meta["license"]}</span>')
    if details:
        parts.append('<p class="doc-meta">' + " &nbsp;|&nbsp; ".join(details) + '</p>')

    if parts:
        return f'<div class="title-block">{"".join(parts)}</div>\n<div class="page-break"></div>'
    return ""


def build_title_block(meta):
    """Build an HTML title block from frontmatter metadata."""
    if not meta:
        return ""

    parts = []
    if meta.get("title"):
        parts.append(f'<h1 class="doc-title">{meta["title"]}</h1>')
    if meta.get("subtitle"):
        parts.append(f'<p class="doc-subtitle">{meta["subtitle"]}</p>')

    details = []
    if meta.get("author"):
        details.append(f'<span class="meta-author">{meta["author"]}</span>')
    if meta.get("date"):
        details.append(f'<span class="meta-date">{meta["date"]}</span>')
    if meta.get("version"):
        details.append(f'<span class="meta-version">Version {meta["version"]}</span>')
    if meta.get("license"):
        details.append(f'<span class="meta-license">{meta["license"]}</span>')
    if details:
        parts.append('<p class="doc-meta">' + " &nbsp;|&nbsp; ".join(details) + '</p>')

    if parts:
        return f'<div class="title-block">{"".join(parts)}</div>\n<div class="page-break"></div>'
    return ""


def convert(input_md, output_pdf, css_file=None):
    raw = Path(input_md).read_text(encoding="utf-8")
    meta, body = extract_frontmatter(raw)
    body = clean_body(body)

    # Markdown extensions — "extra" covers tables, footnotes, fenced code, attr_list
    # sane_lists fixes mixed list behaviour; no nl2br (converts every newline to <br>)
    extensions = ["extra", "sane_lists"]
    extension_configs = {}
    if HAS_PYGMENTS:
        extensions.append("codehilite")
        extension_configs["codehilite"] = {"guess_lang": False, "noclasses": False}

    html_body = markdown.markdown(
        body,
        extensions=extensions,
        extension_configs=extension_configs,
    )

    title_block = build_title_block(meta)

    # Build syntax highlighting CSS
    syntax_css = ""
    if HAS_PYGMENTS:
        syntax_css = HtmlFormatter(style="friendly").get_style_defs(".codehilite")

    # Load custom CSS if provided
    custom_css = ""
    if css_file and Path(css_file).exists():
        custom_css = Path(css_file).read_text(encoding="utf-8")

    doc_title = meta.get("title", Path(input_md).stem)

    full_html = f"""<!DOCTYPE html>
<html lang="{meta.get('lang', 'en')}">
<head>
  <meta charset="utf-8">
  <title>{doc_title}</title>
  <style>
{DEFAULT_CSS}
{syntax_css}
{custom_css}
  </style>
</head>
<body>
  {title_block}
  <div class="content">
    {html_body}
  </div>
</body>
</html>"""

    HTML(string=full_html, base_url=str(Path(input_md).parent)).write_pdf(output_pdf)
    print(f"✓ PDF written to: {output_pdf}")


DEFAULT_CSS = """
/* ── Page layout ── */
@page {
    size: A4;
    margin: 2.8cm 2.5cm 2.8cm 2.5cm;
    @top-center {
        content: string(chapter-title);
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 8.5pt;
        color: #888;
        padding-bottom: 4px;
        border-bottom: 0.5px solid #ddd;
    }
    @bottom-right {
        content: counter(page);
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 8.5pt;
        color: #999;
    }
    @bottom-left {
        content: string(doc-title);
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 8.5pt;
        color: #999;
    }
}

@page :first { @top-center { content: none; } @bottom-left { content: none; } @bottom-right { content: none; } }

/* ── Base typography ── */
body {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 10.5pt;
    line-height: 1.65;
    color: #1a1a1a;
    orphans: 3;
    widows: 3;
}

/* ── Title block (from frontmatter) ── */
.title-block {
    text-align: center;
    padding: 4cm 1cm 3cm;
}

.doc-title {
    string-set: doc-title content();
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 26pt;
    font-weight: 700;
    color: #111;
    border: none;
    margin: 0 0 0.4em;
    padding: 0;
    line-height: 1.2;
}

.doc-subtitle {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 14pt;
    color: #444;
    margin: 0 0 1.5em;
    font-style: italic;
    font-weight: 300;
}

.doc-meta {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 9pt;
    color: #777;
    margin: 0;
    padding-top: 1.5em;
    border-top: 1px solid #ddd;
}

/* ── Headings ── */
h1, h2, h3, h4 {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    color: #111;
    page-break-after: avoid;
    line-height: 1.25;
}

h1 {
    font-size: 18pt;
    font-weight: 700;
    margin: 2em 0 0.5em;
    padding-bottom: 0.25em;
    border-bottom: 2px solid #2a6b3e;
    color: #1e4d2b;
}

/* Only content h1s (inside .content) update the running chapter header */
.content h1 {
    string-set: chapter-title content();
}

h2 {
    font-size: 13.5pt;
    font-weight: 600;
    margin: 1.6em 0 0.4em;
    padding-bottom: 0.2em;
    border-bottom: 1px solid #e0e0e0;
    color: #2a4a30;
}

h3 {
    font-size: 11.5pt;
    font-weight: 600;
    margin: 1.3em 0 0.3em;
    color: #333;
}

h4 {
    font-size: 10.5pt;
    font-weight: 600;
    font-style: italic;
    margin: 1em 0 0.2em;
    color: #444;
}

/* ── Paragraphs ── */
p {
    margin: 0 0 0.75em;
}

/* ── Links ── */
a {
    color: #1a5c32;
    text-decoration: underline;
}

/* ── Tables ── */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.2em 0 1.5em;
    font-size: 9.5pt;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    /* Note: no page-break-inside:avoid here — long evidence tables need to split */
}

thead {
    background-color: #2a6b3e;
    color: #fff;
}

th {
    padding: 8px 12px;
    text-align: left;
    font-weight: 600;
    letter-spacing: 0.02em;
    border: 1px solid #000;
}

td {
    padding: 7px 12px;
    border: 1px solid #000;
    vertical-align: top;
    word-break: break-word;
    overflow-wrap: break-word;
}

thead {
    display: table-header-group; /* repeat header row on page splits */
}

tr:nth-child(even) td {
    background-color: #f7faf8;
}

/* ── Code ── */
code {
    font-family: 'Courier New', Courier, monospace;
    font-size: 9pt;
    background: #f4f4f4;
    border: 1px solid #e0e0e0;
    border-radius: 3px;
    padding: 1px 4px;
}

pre {
    background: #f8f8f8;
    border: 1px solid #ddd;
    border-left: 4px solid #2a6b3e;
    padding: 12px 16px;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 8.5pt;
    line-height: 1.5;
    page-break-inside: avoid;
    margin: 1em 0 1.2em;
}

pre code {
    background: none;
    border: none;
    padding: 0;
}

/* ── Blockquotes ── */
blockquote {
    border-left: 4px solid #2a6b3e;
    margin: 1em 0 1em 0;
    padding: 0.5em 1em;
    background: #f5faf6;
    color: #444;
    font-style: italic;
}

/* ── Lists ── */
ul, ol {
    margin: 0.5em 0 0.8em 1.5em;
    padding: 0;
}

li {
    margin-bottom: 0.25em;
}

/* ── Definition lists ── */
dl {
    margin: 0.5em 0;
}
dt {
    font-weight: bold;
    margin-top: 0.5em;
}
dd {
    margin-left: 1.5em;
}

/* ── Horizontal rule ── */
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 1.5em 0;
}

/* ── Images ── */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0.5em auto;
}

/* ── Page break helper ── */
.page-break {
    page-break-after: always;
    break-after: page;
}

/* Auto page break before each major section (all h1s after the first) */
.content h1:not(:first-of-type) {
    page-break-before: always;
    break-before: page;
}

/* ── Avoid breaks inside short elements; tables allowed to split ── */
pre, blockquote, figure {
    page-break-inside: avoid;
    break-inside: avoid;
}

/* Keep individual table rows together */
tr {
    page-break-inside: avoid;
    break-inside: avoid;
}

h1, h2, h3, h4 {
    page-break-after: avoid;
    break-after: avoid;
}
"""


HELP = """
md_to_pdf.py — Convert Markdown files to styled PDF

USAGE
  Single file:   python3 md_to_pdf.py input.md output.pdf [style.css]
  Whole folder:  python3 md_to_pdf.py /input/folder [/output/folder] [style.css]

ARGUMENTS
  input.md          Path to a single Markdown file
  output.pdf        Path for the output PDF (single file mode)
  /input/folder     Folder containing .md files to convert
  /output/folder    Destination folder for PDFs (default: <input_folder>/pdf/)
  style.css         Optional CSS file to override or extend default styles

EXAMPLES
  python3 md_to_pdf.py report.md report.pdf
  python3 md_to_pdf.py report.md report.pdf custom.css
  python3 md_to_pdf.py ./docs
  python3 md_to_pdf.py ./docs ./output
  python3 md_to_pdf.py ./docs ./output custom.css

MARKDOWN FEATURES SUPPORTED
  - YAML frontmatter  (title, subtitle, author, date, version, license)
  - Tables, fenced code blocks, footnotes  (via "extra" extension)
  - Syntax highlighting  (requires: pip install pygments)
  - Automatic page breaks before top-level headings (#)
  - Repeating table headers across page breaks
  - Running section header and page numbers in footer

DEPENDENCIES
  Required:  pip install weasyprint markdown
  Optional:  pip install pygments pyyaml
"""


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(HELP)
        sys.exit(0)

    first_arg = Path(sys.argv[1])

    # ── Folder mode ──────────────────────────────────────────────────────────
    if first_arg.is_dir():
        folder = first_arg

        # Second arg is output folder if provided, otherwise default to <folder>/pdf
        if len(sys.argv) > 2 and not sys.argv[2].endswith(".css"):
            pdf_dir = Path(sys.argv[2])
            css_file = sys.argv[3] if len(sys.argv) > 3 else None
        else:
            pdf_dir = folder / "pdf"
            css_file = sys.argv[2] if len(sys.argv) > 2 else None

        pdf_dir.mkdir(parents=True, exist_ok=True)

        md_files = sorted(folder.glob("*.md"))
        if not md_files:
            print(f"No .md files found in {folder}")
            sys.exit(0)

        print(f"Converting {len(md_files)} file(s) → {pdf_dir}/")
        errors = []
        for md_file in md_files:
            out = pdf_dir / (md_file.stem + ".pdf")
            try:
                convert(str(md_file), str(out), css_file)
            except Exception as e:
                print(f"  ✗ {md_file.name}: {e}")
                errors.append(md_file.name)

        print(f"\nDone. {len(md_files) - len(errors)}/{len(md_files)} converted successfully.")
        if errors:
            print(f"Failed: {', '.join(errors)}")

    # ── Single file mode ─────────────────────────────────────────────────────
    else:
        if len(sys.argv) < 3:
            print("Usage: python3 md_to_pdf.py input.md output.pdf [style.css]")
            sys.exit(1)

        input_md = sys.argv[1]
        output_pdf = sys.argv[2]
        css_file = sys.argv[3] if len(sys.argv) > 3 else None

        convert(input_md, output_pdf, css_file)
