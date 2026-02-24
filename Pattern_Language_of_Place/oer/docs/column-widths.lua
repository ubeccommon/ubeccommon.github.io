-- column-widths.lua
-- Erdpuls OER Collection — Quarto/pandoc Lua filter
-- Version 1.7 | February 2026
--
-- What this filter does:
--   1. Sets column widths based on column count and first-column header text.
--   2. Wraps wide tables in landscape using \newgeometry / \restoregeometry.
--   3. Pulls the immediately preceding heading or labelling paragraph into the
--      landscape block so it always appears on the same page as its table.
--      (Without this, \newgeometry's forced \clearpage strands the heading on
--      the previous page.)
--
-- Operates at the Blocks level (not the Table level) so it can inspect and
-- modify the block that precedes each landscape-triggering table.
--
-- Landscape is triggered for:
--   • All tables with 5+ columns  (SDG Tier 3, Audience table)
-- Portrait for all 3-col tables including File/Title/Audience ToC table
--   • The 3-column table whose first header is "File"  (TOC filename table)
--
-- Column width sets (fractions of \textwidth; landscape \textwidth ≈ 247 mm):
--   2-col  Field / Value                                   0.28 / 0.72
--   3-col  default (Code/Sub-Competency/Guides etc.)       0.15 / 0.25 / 0.60
--   3-col  File / Title (EN) / Audience  [landscape]       0.30 / 0.40 / 0.30
--   4-col  SDG / Title / Integration level / Evidence      0.06 / 0.16 / 0.10 / 0.68
--   5-col  SDG / Title / Level / Evidence / Author action  0.06 / 0.13 / 0.10 / 0.46 / 0.25
--   5-col  Guide / Role / Level / Age Range / Grade        0.14 / 0.26 / 0.22 / 0.13 / 0.25
--
-- Requires in _quarto.yml include-in-header: geometry, pdflscape, longtable

-- ---------------------------------------------------------------------------
-- Return the plain text of the Nth header cell (1-based).
-- ---------------------------------------------------------------------------
local function header_text(tbl, col)
  if tbl.head and tbl.head.rows and tbl.head.rows[1]
     and tbl.head.rows[1].cells[col] then
    return pandoc.utils.stringify(tbl.head.rows[1].cells[col].contents)
  end
  return ""
end

-- ---------------------------------------------------------------------------
-- Set column widths in place.
-- ---------------------------------------------------------------------------
local function set_widths(tbl, ncols, first_h)
  if ncols == 2 then
    tbl.colspecs[1][2] = 0.28
    tbl.colspecs[2][2] = 0.72

  elseif ncols == 3 then
    if first_h == "File" then
      -- TOC filename table: portrait, monospace filenames wrap gracefully
      tbl.colspecs[1][2] = 0.35
      tbl.colspecs[2][2] = 0.40
      tbl.colspecs[3][2] = 0.25
    else
      -- Code/Sub-Competency/Guides, Format/MIME/Notes, Version/Date/Changes
      tbl.colspecs[1][2] = 0.15
      tbl.colspecs[2][2] = 0.25
      tbl.colspecs[3][2] = 0.60
    end

  elseif ncols == 4 then
    -- SDG Tier 1 & 2: SDG / Title / Integration level / Specific evidence
    -- Portrait layout: col 3 at 14% so "Secondary" fits without hyphenation
    -- on a 160 mm portrait text width (2.5cm margins on A4).
    tbl.colspecs[1][2] = 0.06
    tbl.colspecs[2][2] = 0.14
    tbl.colspecs[3][2] = 0.14
    tbl.colspecs[4][2] = 0.66

  elseif ncols == 5 then
    if first_h == "SDG" then
      -- SDG Tier 3 adds Author action column
      tbl.colspecs[1][2] = 0.06
      tbl.colspecs[2][2] = 0.13
      tbl.colspecs[3][2] = 0.10
      tbl.colspecs[4][2] = 0.46
      tbl.colspecs[5][2] = 0.25
    else
      -- Audience table: Guide / Intended Audience / Educational Level /
      --                 Age Range / Grade Range (Klassenstufe)
      tbl.colspecs[1][2] = 0.14
      tbl.colspecs[2][2] = 0.26
      tbl.colspecs[3][2] = 0.22
      tbl.colspecs[4][2] = 0.13
      tbl.colspecs[5][2] = 0.25
    end

  else
    -- 6+ columns: distribute evenly
    local w = 1.0 / ncols
    for i = 1, ncols do tbl.colspecs[i][2] = w end
  end
end

-- ---------------------------------------------------------------------------
-- Decide whether a preceding block should travel with its landscape table.
-- We pull: Header blocks, and Para blocks (bold tier-label paragraphs).
-- We leave HorizontalRule, RawBlock, etc. in place — they are decorative and
-- read naturally at the foot of the preceding portrait page.
-- ---------------------------------------------------------------------------
local function is_pullable(block)
  return block ~= nil and (block.t == "Header" or block.t == "Para")
end

-- ---------------------------------------------------------------------------
-- Blocks-level filter: the only entry point.  No separate Table function
-- is defined so tables are not processed twice.
-- ---------------------------------------------------------------------------
function Blocks(blocks)
  local result = {}

  for i = 1, #blocks do
    local block = blocks[i]

    if block.t == "Table" then
      local ncols  = #block.colspecs
      local first_h = header_text(block, 1)
      set_widths(block, ncols, first_h)

      local use_landscape = (ncols >= 5)

      if use_landscape then
        -- Pull the preceding heading or labelling paragraph into the landscape
        -- block so \newgeometry's forced page-break doesn't orphan it.
        local pulled = nil
        if is_pullable(result[#result]) then
          pulled = table.remove(result)
        end

        table.insert(result, pandoc.RawBlock("latex",
          "\\newgeometry{a4paper, landscape, margin=2.5cm}"))
        if pulled then
          table.insert(result, pulled)
        end
        table.insert(result, block)
        table.insert(result, pandoc.RawBlock("latex", "\\restoregeometry"))

      else
        table.insert(result, block)
      end

    else
      table.insert(result, block)
    end
  end

  return result
end
