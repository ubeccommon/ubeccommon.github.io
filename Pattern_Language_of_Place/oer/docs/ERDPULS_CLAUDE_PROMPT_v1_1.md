# Claude Prompt: Create or Update Erdpuls Markdown Files
## Version 1.1 | February 2026
## Copy and paste this prompt when asking Claude to write or revise any Erdpuls document

---

## HOW TO USE THIS PROMPT

Copy the block below (everything between the triple backticks) and paste it at the start of your message to Claude, followed by your specific request.

Example:
> [paste prompt block]
> 
> Please write Guide 02 for the Grades 5–8 audience in German.

---

```
You are writing a document for the Erdpuls Müllrose OER Collection. 
Follow the Erdpuls Markdown Authoring Standard (summarised below) exactly.
Do not deviate from these rules even if the content seems to call for it.

=== ERDPULS MARKDOWN AUTHORING STANDARD (SUMMARY) ===

FILE STRUCTURE
- Begin every file with a YAML front matter block, closed with ---
- YAML values that contain colons or special characters must be in double quotes
- Never use | in YAML values (use — or : instead)
- lang must be a BCP 47 code: en, de, or pl

YAML TEMPLATE:
---
title: "Full Document Title"
subtitle: "Optional Subtitle"
date: "Month YYYY"
lang: [en|de|pl]
version: "1.x"
license: "CC BY-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---

SECTION DIVIDERS
- Never use --- as a horizontal rule in the document body
- Use * * * instead (with blank lines before and after)

HEADINGS
- Use ## for major sections, ### for subsections, #### for sub-subsections
- Never use ##### or ###### (H5/H6) — use **bold text** instead
- Never put | in a heading line (use — or : instead)

TABLES
- Use standard pipe tables with plain - separators: |---|---|
- Never use em dashes (—) in separator rows
- Inside table cells, replace & with \& and avoid # and %
- Keep cell text concise (under 30 words per cell where possible)
- Use footnotes for long evidence citations rather than inline table text
- NEVER add \begin{landscape} or \end{landscape} manually — the column-widths.lua
  filter detects wide tables (4+ columns) and wraps them in landscape automatically
- NEVER add column width hints via dash counts — the filter handles all widths

LISTS
- Use - for unordered lists
- Use 1. for ordered lists
- Never use *, +, or Unicode bullet characters directly

SPECIAL CHARACTERS
- German and Polish Unicode characters are safe to use directly
- Emoji (✅ ⛔ 🇩🇪) should be replaced with text: (done), (not started), [DE]
- Box-drawing diagrams must be inside fenced code blocks

LINKS
- Always use inline format: [text](https://url.com)
- Always include https:// prefix
- Never use bare URLs in prose

CODE BLOCKS
- Always use fenced code blocks with triple backticks
- Always include a language identifier (bash, python, yaml, etc.)

FOOTNOTES
- Use pandoc footnote syntax for citations: [^label]
- Define at end of section: [^label]: Citation text here.

FILE NAMING (for reference when saving)
[two-digit-number]_[type]_[scope]_[LANG].md
Example: 02_learning_guide_grades_5-8_EN.md

ERDPULS-SPECIFIC CONVENTIONS

Overview table format (required at start of each guide):
| | |
|---|---|
| **Title** | Full guide title |
| **Target Group** | Audience |
| **Duration** | X hours |
| **Location** | Zone description |
| **Season** | Season guidance |
| **4A-Pathway Focus** | Stage |

Token economy elements (always use this exact wording and colour):
- Cooperation (Green)
- Reciprocity (Blue)
- Mutualism (Orange)
- Regeneration (Gold)

Platform name capitalisation:
- openSenseMap (lowercase o)
- iNaturalist (camelCase i and N)
- senseBox (lowercase s)
- UBECrc (exact case)
- QGIS, BNE, OER (all caps)

Trilingual terms: German / English / Polish (in that order, separated by / )

=== END OF STANDARD ===

QUALITY CHECK BEFORE FINISHING
Before completing your response, verify:
[ ] YAML front matter present and closed with ---
[ ] No --- horizontal rules in body (using * * * instead)
[ ] No H5 or H6 headings (##### or ######)
[ ] No | in heading lines
[ ] All & inside table cells written as \&
[ ] All tables use - separators (no em dashes)
[ ] No emoji — replaced with text equivalents
[ ] All code blocks use triple backtick fences with language identifier
[ ] Platform names capitalised correctly
```

---

## COMMON REQUESTS AND HOW TO PHRASE THEM

### Create a new guide
> [paste prompt block]
> 
> Create Guide 03 (Grades 9–12) in German. 
> The guide covers [topic]. 
> Target group: upper secondary students (Klassen 9–12).
> Duration: 3.5–5 hours.
> Season: all seasons.

### Update an existing file
> [paste prompt block]
> 
> Update the attached file [filename]. 
> Change [specific section] to reflect [new content].
> Preserve all other content exactly.

### Translate an existing guide
> [paste prompt block]
> 
> Translate the attached English guide into German.
> Preserve all markdown structure, table formats, and YAML front matter.
> Set lang: de in the YAML block.
> Translate all body content, headings, and table cells.
> Keep the following terms untranslated: [list any terms].

### Create a new metadata record
> [paste prompt block]
> 
> Add a per-document metadata record for [filename] to the metadata package.
> The guide is for [audience], [educational level], ages [range], grades [range].
> Language: [EN/DE/PL]. Version: [x.x]. Date: [Month YYYY].

### Fix a file for Quarto conversion
> [paste prompt block]
> 
> The attached file fails to convert with Quarto. 
> Apply the Erdpuls Markdown Authoring Standard to fix all conversion issues:
> - Replace all --- body dividers with * * *
> - Fix any H5/H6 headings
> - Fix | in heading lines
> - Escape & inside table cells
> - Replace emoji with text equivalents
> Return the complete corrected file.

---

## WHAT THE STANDARD DOES NOT COVER

The standard governs file structure and syntax. The following are content decisions that the author must provide:

- Specific learning objectives for a new guide
- Session timing and phase structure
- Seasonal variations content
- Facilitator notes specific to a location or group
- Any [TO BE COMPLETED BY AUTHOR] fields
- openSenseMap station IDs and URLs
- Zenodo DOIs (assigned post-submission)
- Polish translations (Phase 3)

---

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 1.1 | February 2026 | Updated table rules: document that landscape and column widths are handled automatically by column-widths.lua filter; authors must never add manual landscape tags or dash-count width hints |
| 1.0 | February 2026 | Initial release — derived from Quarto conversion experience with metadata package and five OER guides |

---

*This prompt document is maintained by Erdpuls Müllrose.*
*Licensed under CC BY-SA 4.0*
*Contact: erdpuls@ubec.network*
