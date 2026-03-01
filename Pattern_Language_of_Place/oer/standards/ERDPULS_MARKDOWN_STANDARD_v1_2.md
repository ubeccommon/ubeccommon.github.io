# Erdpuls Markdown Authoring Standard
## Version 1.2 — March 2026
## For all files in the Erdpuls OER Collection

---

## Purpose

This standard governs how all Erdpuls markdown files are written. It serves three audiences simultaneously:

1. **GitHub readers** — files render correctly in any GitHub/GitLab/Codeberg viewer
2. **Converters** — files convert cleanly to PDF (Quarto/pandoc), DOCX, and HTML without manual fixes
3. **Claude** — files can be created or updated by Claude following this standard as a prompt

The standard is based on **CommonMark** (the industry-wide markdown specification) with selected **Pandoc extensions** that are backward-compatible with GitHub Flavored Markdown (GFM).

---

## 1. File Structure

Every file must begin with a YAML front matter block. No exceptions.

```yaml
---
title: "Full Document Title"
subtitle: "Optional Subtitle — No pipe characters here"
author: "Michel Garand"
date: "Month YYYY"
version: "1.x"
lang: en
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
status: "Concept Document — for review and programme development"
---
```

**Required fields (all nine must be present in every file):**

| Field | Value |
|---|---|
| `title` | Primary document identity — always first |
| `subtitle` | Secondary identity — always second |
| `author` | `"Michel Garand"` — human responsibility, before date |
| `date` | `"Month YYYY"` — this edition |
| `version` | `"1.x"` — this edition's revision |
| `lang` | BCP 47 code: `en`, `de`, or `pl` |
| `license` | `"CC BY-SA 4.0"` or `"CC BY-NC-SA 4.0"` |
| `project` | `"Erdpuls Müllrose OER Collection"` (EN) or `"Erdpuls Müllrose OER-Sammlung"` (DE) |
| `status` | Lifecycle state — most volatile field, always last |

**Status values:**
- EN: `"Concept Document — for review and programme development"`
- DE: `"Konzeptdokument — zur Prüfung und Programmentwicklung"`

**Optional fields** (append after `status` when present, in this order):
- `document` — document reference within a series
- `part_of` — parent collection reference
- `translated_from` — source document for translation pairs

**Additional rules:**
- Titles and subtitles must be in double quotes
- Never use `|` in YAML values — use `:` or `—` instead
- `lang` must be a valid BCP 47 code: `en`, `de`, `pl`
- The front matter block opens and closes with `---` on its own line
- Body content begins on the line immediately after the closing `---`

---

## 2. Section Dividers

**Never use `---` as a horizontal rule in the document body.** It conflicts with YAML parsing in Quarto and pandoc.

| Instead of | Use |
|---|---|
| `---` | `* * *` |

```markdown
<!-- WRONG -->
## Section One
---
## Section Two

<!-- CORRECT -->
## Section One

* * *

## Section Two
```

Always leave a blank line before and after `* * *`.

---

## 3. Headings

Use ATX-style headings (hash prefix). Maximum depth in body content: `####` (level 4).

```markdown
# Document Title          ← H1: used once, at top only if no YAML title
## Major Part             ← H2: main sections
### Chapter / Section     ← H3: subsections
#### Subsection           ← H4: sub-subsections (use sparingly)
```

**Never use H5 (`#####`) or H6 (`######`)** — they cause LaTeX compilation errors when adjacent to tables. Replace with bold paragraph text:

```markdown
<!-- WRONG -->
##### Tier 1 — Primary SDGs

<!-- CORRECT -->
**Tier 1 — Primary SDGs** (descriptive note here)
```

**Never put `|` in a heading line.** Use `:` or `—` instead:

```markdown
<!-- WRONG -->
### Version 1.1 | February 2026

<!-- CORRECT -->
### Version 1.1 — February 2026
```

---

## 4. Tables

### 4.1 Syntax

Use standard pipe tables with plain `-` separators only:

```markdown
| Column A | Column B | Column C |
|---|---|---|
| Cell | Cell | Cell |
```

**Never use:**
- Em dashes (`—`) in separator rows
- Colons for alignment (`:---:`) — these cause issues in some converters
- HTML `<table>` tags

### 4.2 Special Characters Inside Table Cells

| Character | Problem | Use instead |
|---|---|---|
| `&` | LaTeX column separator | `\&` |
| `%` | LaTeX comment | `\%` |
| `#` | LaTeX macro character | avoid or use `\#` |
| `<` | HTML tag start | `\<` or `&lt;` |
| `>` | HTML tag end | `\>` or `&gt;` |

### 4.3 Column Width Hints

Pandoc infers column widths from the relative number of dashes in separator rows. For documents that will be converted to PDF, use proportional dashes to guide layout:

```markdown
<!-- 2-column Field/Value table: 28% / 72% -->
| Field | Value |
|--|---------|

<!-- 4-column SDG-style table: 8% / 16% / 10% / 66% -->
| SDG | Title | Level | Evidence |
|--|---|---|----------------|

<!-- 3-column reference table: 20% / 20% / 60% -->
| Code | Name | Description |
|---|---|---------|
```

**Note:** When using the Erdpuls `column-widths.lua` Quarto filter (see `_quarto.yml`), this is handled automatically based on column count. Plain equal separators (`|---|`) are sufficient.

### 4.4 Wide Tables

For tables with long prose content in a 4+ column layout, keep cell text concise (under 30 words per cell where possible). Long evidence citations belong in footnotes or a separate appendix, not inline in cells.

---

## 5. Lists

Use `-` for unordered lists. Use `1.` for ordered lists. Do not use `*` or `+` as list markers.

```markdown
- Item one
- Item two
  - Nested item (two-space indent)

1. First step
2. Second step
```

Never use Unicode bullet characters (`•`, `·`, `▪`) directly — they may not render in all PDF engines.

---

## 6. Special Characters and Unicode

### 6.1 Always safe (use directly)
German: `ä ö ü Ä Ö Ü ß`
Polish: `ą ę ś ź ż ó ł ć ń`
Math/units: `°C µg/m³ CO₂ PM₂.₅ pH`
Punctuation: `— – " " ' '`
Arrows: `→ ← ↑ ↓`

### 6.2 Use with caution
Emoji (`✅ ⛔ ⏳ 🇩🇪 🇵🇱`) render correctly in GitHub and HTML but may render as boxes in PDF without a dedicated emoji font. For PDF-bound documents, replace with text equivalents:

| Emoji | Text equivalent |
|---|---|
| ✅ | `(done)` or `[x]` |
| ⛔ | `(not started)` |
| ⏳ | `(pending)` |
| 🇩🇪 | `[DE]` |
| 🇵🇱 | `[PL]` |

### 6.3 Box-drawing characters
The ASCII box-drawing diagram (`┌─┐│└┘`) in the master index must be inside a fenced code block to render correctly in both GitHub and PDF:

````markdown
```
┌─────────────────────┐
│   DIAGRAM CONTENT   │
└─────────────────────┘
```
````

---

## 7. Code Blocks

Always use fenced code blocks with a language identifier:

````markdown
```bash
quarto render file.md --to pdf
```

```python
import pandas as pd
```

```yaml
format:
  pdf:
    papersize: a4
```
````

For generic preformatted text with no language, use plain fences:

````markdown
```
Plain preformatted text
```
````

---

## 8. Links

Use standard inline links. Always include the `https://` prefix:

```markdown
[Link text](https://example.com)
```

For email addresses:

```markdown
[erdpuls@ubec.network](mailto:erdpuls@ubec.network)
```

Do not use bare URLs in prose — they render inconsistently across converters.

---

## 9. Emphasis and Bold

```markdown
**Bold text** for key terms, labels, field names
*Italic text* for titles of documents, foreign words, first use of a term
`Code formatting` for filenames, command names, field values, technical strings
```

Do not use bold for entire paragraphs or sentences. Do not use italic for general emphasis.

---

## 10. Footnotes

Use pandoc-style footnotes for citations and extended evidence. These render in GitHub (as hover text in some viewers) and correctly in PDF:

```markdown
The soil observation protocol connects directly to groundwater recharge.[^q8]

[^q8]: Appendix A, Question 8: "Pour a small amount of water onto the surface near your hole. 
Watch carefully... This connects immediately to flood risk, erosion, drought resilience, 
and groundwater recharge."
```

This is the preferred alternative to long prose in table cells.

---

## 11. File Naming

```
[two-digit-number]_[type]_[scope]_[language].md
```

Examples:
```
01_learning_guide_grades_1-4_EN.md
01_lernleitfaden_klassen_1-4_DE.md
01_przewodnik_klasy_1-4_PL.md
04_teachers_guide_EN.md
04_lehrerhandbuch_DE.md
00_METADATA_PACKAGE_v1_2.md
```

Rules:
- Lowercase except for acronyms and version markers
- Hyphens within scope descriptors, underscores between components
- Language suffix for all files with translations: `_EN`, `_DE`, `_PL`
- Version marker in metadata and index files: `_v1_2`
- No spaces in filenames

---

## 12. Quarto Conversion Requirements

When rendering to PDF via Quarto, two infrastructure files must be present in the OER directory root. These files handle all table formatting automatically for every document — **no manual `\begin{landscape}` tags or column width hints are ever needed in markdown source files.**

### Design principle

Write all tables as plain pipe tables with equal `|---|` separators. The `column-widths.lua` filter intercepts every table at render time and:

1. Sets column widths based on column count and position heuristics
2. Automatically wraps tables with 4 or more columns in landscape orientation

This applies uniformly to all `.md` files in the directory with zero per-file configuration.

---

**`_quarto.yml`** (place in OER directory root):

```yaml
format:
  pdf:
    papersize: a4
    geometry: margin=2.5cm
    mainfont: "Linux Libertine O"
    sansfont: "Linux Biolinum O"
    monofont: "DejaVu Sans Mono"
    toc: true
    toc-depth: 3
    colorlinks: true
    linkcolor: NavyBlue
    pandoc-args: ["--lua-filter=column-widths.lua"]
    include-in-header:
      text: |
        \usepackage{longtable}
        \usepackage{booktabs}
        \usepackage{array}
        \usepackage{tabularx}
        \usepackage{calc}
        \usepackage{pdflscape}
        \setlength{\tabcolsep}{4pt}
        \renewcommand{\arraystretch}{1.3}
        \AtBeginEnvironment{longtable}{\small}
```

---

**`column-widths.lua`** (place in OER directory root):

```lua
-- column-widths.lua
-- Erdpuls OER Collection — Quarto/pandoc Lua filter
-- Version 1.1 | February 2026
--
-- Automatically:
--   1. Sets intelligent column widths based on column count and position
--   2. Wraps tables with 4+ columns in landscape orientation (PDF only)
--
-- No manual \begin{landscape} tags needed in any markdown file.

local function needs_landscape(ncols)
  return ncols >= 4
end

local function set_widths(tbl, ncols)
  if ncols == 2 then
    -- Field / Value tables
    tbl.col_specs[1][2] = 0.28
    tbl.col_specs[2][2] = 0.72

  elseif ncols == 3 then
    -- Code / Name / Description  or  Guide / Level / Range
    tbl.col_specs[1][2] = 0.15
    tbl.col_specs[2][2] = 0.25
    tbl.col_specs[3][2] = 0.60

  elseif ncols == 4 then
    -- SDG-style: ID / Title / Level / Evidence
    -- Level is always a single word; evidence gets maximum space
    tbl.col_specs[1][2] = 0.06
    tbl.col_specs[2][2] = 0.16
    tbl.col_specs[3][2] = 0.06
    tbl.col_specs[4][2] = 0.72

  elseif ncols == 5 then
    -- SDG Tier 3: ID / Title / Level / Evidence / Author action
    tbl.col_specs[1][2] = 0.06
    tbl.col_specs[2][2] = 0.13
    tbl.col_specs[3][2] = 0.06
    tbl.col_specs[4][2] = 0.50
    tbl.col_specs[5][2] = 0.25

  else
    -- 6+ columns: distribute evenly
    local w = 1.0 / ncols
    for i = 1, ncols do
      tbl.col_specs[i][2] = w
    end
  end
end

function Table(tbl)
  local ncols = #tbl.col_specs
  if ncols == 0 then return end

  set_widths(tbl, ncols)

  if needs_landscape(ncols) then
    local before = pandoc.RawBlock("latex", "\\begin{landscape}")
    local after  = pandoc.RawBlock("latex", "\\end{landscape}")
    return { before, tbl, after }
  end

  return tbl
end
```

---

### Column width rationale

| Column count | Typical table type | Width allocation |
|---|---|---|
| 2 | Field / Value (metadata, checklists) | 28% / 72% |
| 3 | Phase / Duration / Description; Code / Name / Guides | 15% / 25% / 60% |
| 4 | SDG Tier 1–2 (ID / Title / Level / Evidence) | 6% / 16% / 6% / 72% |
| 5 | SDG Tier 3 (adds Author action column) | 6% / 13% / 6% / 50% / 25% |
| 6+ | Rare; split into multiple tables if possible | Equal distribution |

The "Level" column (col 3 in 4- and 5-column tables) is always a single word (Primary / Secondary / Tertiary) and is kept as narrow as possible to maximise space for the evidence column.

---

## 13. GitHub Compatibility Checklist

Before committing any file to GitHub, verify:

- [ ] YAML front matter present and correctly closed with `---`
- [ ] All nine required YAML fields present: `title`, `subtitle`, `author`, `date`, `version`, `lang`, `license`, `project`, `status`
- [ ] YAML fields in canonical order (title → subtitle → author → date → version → lang → license → project → status)
- [ ] `author` value is `"Michel Garand"`
- [ ] `status` value matches language: EN or DE variant
- [ ] No `---` horizontal rules in body (replaced with `* * *`)
- [ ] No H5/H6 headings
- [ ] No `|` in heading lines or YAML values
- [ ] All `&` inside table cells written as `\&`
- [ ] All tables use `-` separators (no em dashes)
- [ ] All code blocks fenced with triple backticks
- [ ] Colophon present and uses canonical heading and template (see §14)
- [ ] File named according to naming convention
- [ ] Language suffix present if file has translations

---

## 14. Erdpuls-Specific Conventions

### Document header block
Every guide begins with a standard overview table immediately after the YAML block:

```markdown
| | |
|---|---|
| **Title** | Full guide title |
| **Target Group** | Audience description |
| **Duration** | X hours |
| **Location** | Zone description |
| **Season** | Season guidance |
| **4A-Pathway Focus** | Stage name |
```

### Phase timing tables
All session phase tables use the 3-column format:

```markdown
| Phase | Duration | Description |
|---|---|---------|
| Phase 1 | 30 min | Description |
```

### Token economy references
Always use the four-element format with colour codes in parentheses:
- Cooperation (Green)
- Reciprocity (Blue)
- Mutualism (Orange)
- Regeneration (Gold)

### Cross-border content
Trilingual terms appear in this order: German / English / Polish, separated by ` / `

### Platform and tool names (capitalisation)
| Name | Correct form |
|---|---|
| openSenseMap | openSenseMap (lowercase o) |
| iNaturalist | iNaturalist (camelCase) |
| senseBox | senseBox (lowercase s) |
| UBECrc | UBECrc (exact case) |
| QGIS | QGIS (all caps) |
| BNE | BNE (all caps) |

### Canonical colophon

Every document ends with a canonical colophon block. The colophon is always at the **bottom** of the document, separated from the body by `* * *`. It is never at the top.

**Colophon element order** (industry standard — identity → rights → permissions → provenance → contact → series):

1. `* * *` — section divider
2. `## License and Attribution` / `## Lizenz und Impressum` — heading
3. Copyright notice — `© 2025–2026 Michel Garand | Erdpuls Müllrose…`
4. Location line — `Müllrose, Brandenburg, Germany` / `Deutschland`
5. Licence statement — linked CC licence matching the `license` YAML field
6. Permissions summary — human-readable freedoms sentence
7. Software licence — AGPL-3.0
8. Provenance / AI disclosure — `*This document and its translations were developed with assistance from Claude…*`
9. Contact — `**Contact:** erdpuls@ubec.network`
10. Series / translation note + date stamp — `*Alle Dokumente und ihre Übersetzungen…*`

**Canonical templates** (select by `lang` × `license`):

*EN — CC BY-SA 4.0:*
```markdown
* * *

## License and Attribution

© 2025–2026 Michel Garand | Erdpuls Müllrose — Center for Sustainability Literacy, Citizen Science & Reciprocal Economics
Müllrose, Brandenburg, Germany

Licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)

You are free to share and adapt this material for any purpose, including commercially, provided you give appropriate credit, provide a link to the license, indicate if changes were made, and distribute any adaptations under the same license.

All software components referenced in this document are licensed under the [GNU Affero General Public License v3.0 (AGPL-3.0)](https://www.gnu.org/licenses/agpl-3.0.html)

*This document and its translations were developed with assistance from Claude (Anthropic PBC). All strategic decisions, philosophical positions, and project commitments are those of the author.*

**Contact:** erdpuls@ubec.network · [https://erdpuls.ubec.network](https://erdpuls.ubec.network)

*Alle Dokumente und ihre Übersetzungen / All documents and their translations.*
*Müllrose, Brandenburg — {Month YYYY}*
```

*EN — CC BY-NC-SA 4.0:* identical but with `Attribution-NonCommercial-ShareAlike` licence link and `for non-commercial purposes` in the permissions line.

*DE — CC BY-SA 4.0:*
```markdown
* * *

## Lizenz und Impressum

© 2025–2026 Michel Garand | Erdpuls Müllrose — Center for Sustainability Literacy, Citizen Science & Reciprocal Economics
Müllrose, Brandenburg, Deutschland

Lizenziert unter [Creative Commons Namensnennung – Weitergabe unter gleichen Bedingungen 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.de)

Sie dürfen dieses Material für beliebige Zwecke, auch kommerziell, teilen und anpassen, sofern Sie angemessene Namensnennung angeben, einen Link zur Lizenz beifügen, angeben ob Änderungen vorgenommen wurden, und etwaige Anpassungen unter derselben Lizenz verbreiten.

Alle in diesem Dokument genannten Softwarekomponenten sind lizenziert unter der [GNU Affero General Public License v3.0 (AGPL-3.0)](https://www.gnu.org/licenses/agpl-3.0.html)

*Dieses Dokument und seine Übersetzungen wurden mit Unterstützung von Claude (Anthropic PBC) entwickelt. Alle strategischen Entscheidungen, philosophischen Positionen und Projektverpflichtungen liegen beim Autor.*

**Kontakt:** erdpuls@ubec.network · [https://erdpuls.ubec.network](https://erdpuls.ubec.network)

*Alle Dokumente und ihre Übersetzungen / All documents and their translations.*
*Müllrose, Brandenburg — {Monat JJJJ}*
```

*DE — CC BY-NC-SA 4.0:* identical but with `Namensnennung – Nicht kommerziell – Weitergabe` licence link and `für nicht-kommerzielle Zwecke` in the permissions line.

**Important:** The `00_METADATA_PACKAGE` files use a specialised compilation provenance note in place of a colophon — they are excluded from this requirement.

---

*This standard is maintained by Erdpuls Müllrose. Questions: erdpuls@ubec.network*
*Licensed under CC BY-SA 4.0*
