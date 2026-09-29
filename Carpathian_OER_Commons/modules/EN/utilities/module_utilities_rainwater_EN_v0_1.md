---
title: "Rainwater and Nursery Irrigation"
subtitle: "Carpathian OER Commons — Utilities Module"
author: "Michel Garand"
date: "2026-09-29"
version: "v0.1"
lang: "en"
license: "CC BY-SA 4.0"
project: "Carpathian OER Commons"
status: "L1 — designed, costed from estimates, untested"
---

*Maturity: **L1** — designed and costed, untested. Every cost line is
an estimate or a listed price, labelled as such in Section 6; the
rainfall, the roof, and the nursery's need are assumed or set until
the station record, the walk, and the tree nursery module replace
them. Nothing has been built. Read every figure below at this level
and no higher.*

*Governed by Section 2 of the compendium. No child appears in this
module in any form. The site is not named; site plans are schematic;
photographs show structures and systems only. Design loads are site
capacity, used for sizing only.*

*Converted from the water working paper, EN v0.1, Sections 6 and 8.5,
the last part of that paper still unconverted. Four things change
from the paper, decided on 2026-09-29: the runoff factor and the
rainfall are now quoted from sources; the nursery's weekly need is
read against forestry nursery guidance, which asks more at sowing; the
hand pump is priced from a listing; and the case the water module hands
over — rainwater taking non-drinking uses when the spring falls between
its thresholds — is sized here, not costed.*

*Permits and local rules. This module is a guide, used in different
regions and countries under different laws and guidelines. Depending on
where it is built, at what scale, and for whom, permits, registrations,
or approvals may be required — for building, water, sanitation, fire,
waste, food, or the use of forest and land. Section 10 records what was
found for Ukraine, dated, and unchecked until signed; a reader
elsewhere checks their own rules with the competent authorities before
building, and nothing here replaces that.*

* * *

## 1. Purpose

Water for the tree nursery from a roof: gutters and downpipes, a
first-flush diverter on each, a buried cistern near the seedbeds, and a
hand pump — no electricity, no treatment, and nothing taken from the
spring.

**Five rules.** Two waters, kept apart: roof water for plants, spring
water for people; no pipe, valve, or hose joins them. The first water
is thrown away: every downpipe passes a first-flush diverter before the
cistern. Never topped up from the spring: in a drought longer than the
cistern, water is carried from the market garden's pond, which the
stream refills. Covered and locked: the cistern's one manhole is locked,
and the pump is the only way in. Close to the beds: the cistern sits
low, beside the seedbeds, so the water is carried a few steps, not
across the site.

**Connections.** Depends on: a roof of about 100 m² near the nursery,
from the buildings modules; the tree nursery module, whose beds and
watering it serves; the Phase 1 walk, with the roof, its downpipes, the
fall, and the cistern site; the rainfall record of the nearest
hydrometeorological station; the written enquiries in Section 10.
Feeds: the tree nursery. Takes from: the market garden's pond, in a
long drought only. Hands back to the water module: the non-drinking
uses, sized in Section 3.3, only if the spring measures between its
thresholds.

**Patterns.** Grows from: not yet named. How the valley's households
caught the water off their roofs, and what they watered with it, are
questions for the elders. Feeds: not yet named. Resonates with: 104
Site Repair — the cistern on poorer ground beside the seedbeds; 25
Access to Water — roof water open to every hand at the pump, where the
spring's is fenced; 172 Garden Growing Wild — the nursery raising the
trees the regeneration strand plants. In tension with: 64 Pools and
Streams — a buried cistern takes the roof's water out of sight; the
downpipes, the diverters, and the overflow are where it stays visible.

* * *

## 2. Context of validity

| Condition | Range this design holds for |
|---|---|
| Climate | [set] — mountain; watering in the warm months |
| Rainfall | 800–1,000 mm a year, [assumed] |
| Roof | about 100 m², hard and sloped, [set] |
| Nursery | about 50 m² of seedbeds, [set] |
| Group size | none: the nursery sets the size, not the people |
| Fall | roof above the cistern; the cistern beside the beds |
| Frost | the cistern below the frost line, as the potable one |

Where the roof is small, the rain light, or the nursery larger, the
cistern empties sooner and the pond carries more; Section 3 shows how
to read it.

* * *

## 3. Sizing method

**What you must measure yourself before using this module:**

- **Your rainfall** — the annual and monthly record of the nearest
  hydrometeorological station, and the warm months' share of it.
- **Your roof** — its plan area, its material, and where its downpipes
  can fall, from the walk.
- **Your nursery** — its bed area and its watering, from the tree
  nursery module and, once it runs, from the watering record.
- **Your cistern site** — the soil and the fall, from the walk.

**Our example:** rainfall, 800 to 1,000 mm a year, [assumed];
roof_area, 100 m², [set]; runoff_factor, 0.8; nursery_area, 50 m²,
[set]; nursery_watering, 10 L a m² a week, [assumed]; first_flush, 0.5
L a m² of roof, [assumed]. Values from the site parameters file, held
in the workshop.

### 3.1 The yield

One millimetre of rain on one square metre of roof is one litre.

| Quantity | Calculation | Our example |
|---|---|---|
| A year | 100 m² × 0.8 × 800–1,000 mm | 64,000–80,000 L |
| A warm month | 70–80 percent over six months | 7,500–10,700 L |
| Rain to fill the cistern | 4,160 L ÷ (100 m² × 0.8) | about 52 mm |

**The rainfall.** The paper's 800 to 1,000 mm is kept, [assumed]. A
regional geography of the Ukrainian Carpathians gives 800 to 1,000 mm
in the foothills and 800 to 1,200 mm at 800 to 1,000 m, rising to 1,400
to 1,600 mm on the highest peaks, with 70 to 80 percent of it in the
warm season, mostly as downpours (Voropai and Kunytsia, Українські
Карпати); the Encyclopedia of Modern Ukraine gives 500 to 800 mm in the
foothills. At 500 mm the year's yield would be 40,000 L. The warm month
above spreads the warm-season share over six months, April to
September, [assumed]; the station record replaces it.

**The runoff factor.** 0.8, as the paper has it, now quoted: DIN
1989-1 gives a yield coefficient of 0.8 for a sloped hard roof, as
reported by a German supplier's handbook (Amres); the Texas Manual on
Rainwater Harvesting, 2005, p. 29, says most installers assume 75 to 90
percent, and notes that clay or concrete tile may lose up to 10 percent
(p. 6).

### 3.2 The nursery and the cistern

| Quantity | Calculation | Our example |
|---|---|---|
| A dry week, the paper's rate | 50 m² × 10 L | 500 L |
| A dry week, at sowing | 50 m² × 14–17.5 L | 700–875 L |
| A month, the paper's rate | 500 L × 4.3 | about 2,150 L |
| Cistern, internal | 2.0 × 1.6 m × 1.3 m water | about 4.2 m³ |
| Dry weeks carried | 4,160 L ÷ the week | about 4.8 to 8.3 |
| First flush, whole roof | 100 m² × 0.5 L | 50 L |

**The nursery's need.** The paper's 5 L a m² twice a week is kept,
[assumed], for the season. It is below what forestry nursery guidance
asks at sowing: the Ukrainian recommendations for growing seedlings of
the main forest species give 10 L a m² for birch in open ground right
after sowing, then every four to five days, about 14 to 17.5 L a m² a
week (State Forestry Committee and the Ukrainian Research Institute of
Forestry and Agroforestry, Kharkiv, 2010); the US Forest Nursery Manual
gives 6.4 to 12.7 mm a day during germination on sandy soils (McDonald,
in Duryea and Landis, 1984, ch. 12). The tree nursery module sets the
rate, and the watering record replaces it.

**The cistern.** The paper's 4.2 m³, single chamber, the same
construction as the potable cistern: 2.0 × 1.6 m inside, 1.3 m of water,
below the frost line. It carries the nursery through about eight dry
weeks at the paper's rate and about five at the sowing rate; the paper's
six lies between. Over a year the roof gives several times what the
nursery asks; the cistern, not the roof, is the limit, and about 52 mm
of rain fills it from empty.

**The first flush.** The Texas Manual, p. 8, diverts at least 10
gallons for every 1,000 square feet of roof, about 0.41 L a m², and
reports an Australian study giving 0.53 to 2.0 L a m². 0.5 L a m² is
used, [assumed]: 50 L for the roof, shared among its downpipes. For two
downpipes, [set], each diverter holds about 25 L — a standpipe of 160
mm pipe, with a bore of about 150 mm, [assumed], holding about 17.7 L a
metre, some 1.4 m long, closed below by a cap with a small drip hole
so that it empties itself between rains.

### 3.3 When the spring falls between its thresholds

The water module reads the spring against the demand: between 1.8 and
4 L a minute, the spring carries the people only if rainwater takes
every non-drinking use it can. On this site that use is the flushing
of the two existing flush toilets.

| Quantity | Calculation | Our example |
|---|---|---|
| Flush water, a day | the greywater module, 3.1 | about 283 L |
| Spring demand without it | 2.55 m³ − 0.28 m³ | about 2.27 m³ |
| As a flow | 2.27 m³ ÷ 1,440 min | about 1.6 L/min |
| One session's flushing | 283 L × 20 days | about 5.7 m³ |
| Rain to refill it, 100 m² | 5,660 L ÷ (100 m² × 0.8) | about 71 mm |

A session is session_length, 20 days, [assumed]. It takes its own roof
and cistern, of about 6 m³, beside the flush toilets; a small pump from
the energy module; and its own pipe to the toilets' cisterns, marked
along its length, with no connection to the potable system. Frozen
gutters and snow give little in winter, so a winter session's flushing
falls back on the spring. It is sized here and not costed; it is
designed only if the spring measures between the thresholds, and asked
of the sanitary service first (Section 10).

* * *

## 4. Bill of materials

Quantities for the example. Alternatives are named in the design; none
is yet known to work here.

| Item | Quantity | Alternatives in the design |
|---|---|---|
| Gutters, downpipes, brackets | one 100 m² roof | PVC; coated steel |
| First-flush diverter, 25 L | 2 | a bought downpipe filter |
| Cistern, masonry, 4.2 m³ | 1 | a 5,000 L plastic tank |
| Lockable manhole cover | 1 | none named |
| Inlet, overflow, washout, vent | 1 set | none named |
| Hand pump, piston | 1 | a tap at the base of a tank |
| Watering cans and a short hose | [set] | a drip line |

**The cistern, as designed.** As the potable cistern in the water
module, Section 4, at about half its volume: one chamber, 2.0 × 1.6 m
inside, 1.3 m of water and 0.3 m of freeboard; rubble stone walls in
cement mortar; a reinforced floor and roof slab; at least 1 m of earth
cover; one lockable manhole; an inlet through the diverters, an
overflow led away downslope, a washout, and a screened vent.

**The plastic tank, as the alternative.** A 5,000 L tank above ground,
opaque, on a level gravel base, drawn by gravity from a tap at its
base, so that no pump is needed; emptied before the frost and left
open to drain, [set]. It costs about half the masonry cistern and lasts
[set]; a tank rated for burial was not found priced.

**The siting, as designed.** None has been measured yet; every rule
below is checked on the ground before anything is dug.

| From | To | Rule |
|---|---|---|
| The cistern and its pipes | the potable system | no connection |
| The overflow | any foundation | led away, [set] |
| The overflow | the spring's catchment | never into it |
| The cistern | septic tank, bed, soakaway | upslope of them |
| The seedbeds | the stream and a pond | 25 m; 50 m on a slope |
| The cistern | the seedbeds | beside them, [set] |

The seedbeds keep out of the Water Code's protective strip along the
stream and around the pond, as the market garden's beds do (Section
10). No distance was found between a rainwater cistern and a septic
tank or soakaway; the cistern stands above them on the fall, and the
walk sets the rest.

**The layout, as designed.** Roof, gutters, downpipes, diverters,
cistern, pump, seedbeds, in that order down the fall; the overflow away
from every foundation and from the spring. Drawn as relationships only;
the walk sets the rest.

* * *

## 5. Build

| Step | Trade | Time | If done out of order |
|---|---|---|---|
| Enquiries answered | household | [from L2] | [from L2] |
| Walk: roof, fall, site | household | [from L2] | cistern misplaced |
| Excavation | excavator | [from L2] | [from L2] |
| Cistern walls, slabs, render | mason | [from L2] | [from L2] |
| Gutters, downpipes, diverters | roofer | [from L2] | first water in |
| Pump, overflow laid | plumber | [from L2] | overflow at footings |
| Backfill, earth cover | excavator | [from L2] | frost in the cistern |
| Filled by rain, pump tried | household | [from L2] | [from L2] |

Built with the nursery, after the potable system, as the paper orders
it.

* * *

## 6. Cost

Estimates, not quotations: each line is either a price listed by a
Ukrainian retailer, seen on 2026-09-29, or the water paper's own
estimate for autumn 2026, marked "paper". Place: not a quotation;
western Ukrainian listings where found, national otherwise. Exchange
rate: exchange_rate, 52 UAH to the euro, the National Bank's
mid-September 2026 rate, rounded.

### 6.1 Collection

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Gutters and downpipes, 100 m² roof | 12,000 | 231 | paper |
| First-flush diverters, two | 2,000 | 38 | paper |
| Subtotal | 14,000 | 269 | |

A 130 mm PVC gutter is listed at 360 to 462 UAH a 3 m length, a 100 mm
downpipe at 565 UAH a 3 m length, and gutter brackets at 112 to 144 UAH
each, in western Ukrainian listings; the roof's own lengths, from the
walk, turn these into a quotation. No first-flush diverter was found in
Ukrainian retail; it is built from pipe and fittings. A downpipe
rainwater collector for a barrel, a different device, is listed at 351
to 380 UAH.

### 6.2 Storage and drawing

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Cistern, 4.2 m³, masonry | 82,300 | 1,583 | paper |
| Hand pump, piston, 8 m lift | 3,500 | 67 | estimated, listing |
| Subtotal | 85,800 | 1,650 | |

The paper costs the cistern at 55 percent of the potable cistern's
149,630 UAH: about half the volume, one chamber, one manhole. The hand
pump is a stainless piston pump listed at 3,500 UAH, against the
paper's 5,000; the seller is not in western Ukraine.

### 6.3 Summary

| Section | UAH | EUR |
|---|---|---|
| Collection | 14,000 | 269 |
| Storage and drawing | 85,800 | 1,650 |
| Construction subtotal | 99,800 | 1,919 |
| Design and engineer's check, 8 percent | 8,000 | 154 |
| Contingency, 20 percent | 20,000 | 385 |
| **Total external cost** | **127,800** | **2,458** |

Against the paper's 101,300 UAH before its percentages, the difference
is the hand pump. The percentages are the paper's; the contingency is
taken on the construction subtotal, as in the land and sanitation
modules, where the water module takes it on the subtotal and the design
together, as the paper does.

**The plastic tank instead.** A 5,000 L tank is listed at 38,000 UAH,
vertical, and 38,500 UAH, horizontal, in western Ukrainian listings;
with the horizontal tank, and a tap, not priced, in place of the pump,
the construction subtotal would be about 52,500 UAH, and the total
about 67,200 UAH. The gravel base is not priced.

**Contribution, not in the total.** Rubble stone for the cistern from
the site or the valley, with the landowner's leave, in proportion to
the potable cistern's, [set]. The labour is in the cost.

**Running cost.** None bought. The gutters and diverters cleared in
spring and autumn; the cistern inspected yearly and cleaned when silt
shows; the pump's seals replaced when worn, [set]. The work is paid,
[set] hours.

* * *

## 7. Operation and maintenance

Responsible: one named adult, paid, with a deputy — [from L2].

- **After heavy rain:** the diverters checked for draining; the
  overflow walked.
- **In the watering season:** the cistern's level read weekly and
  written down with the water drawn, so that the nursery_watering
  figure is replaced by a measured one.
- **Spring and autumn:** gutters and diverters cleared of leaves and
  needles.
- **Before the frost:** the pump drained; the diverters' caps opened;
  a plastic tank, if chosen, emptied.
- **Yearly:** the cistern inspected; cleaned when silt shows; the
  manhole's lock checked.

How the programme relates to this work is described in the programme
modules, in standing format.

* * *

## 8. Failure modes

From the design, not from experience.

| Failure | Early sign | Repair and cost |
|---|---|---|
| Cistern empty | level falls, no rain | water from the pond |
| Diverter blocked | it stays full | clear the drip hole |
| Gutter overflows | water down the wall | clear it; larger outlet |
| Pump frozen | no stroke in frost | drain it before frost |
| Overflow at footings | wet wall, soft ground | lead it further |
| Water green or smelling | colour at the pump | cover checked; clean |
| Lock or cover broken | cover loose | replace at once |

* * *

## 9. What we got wrong

Nothing yet: this module has not been built.

* * *

## 10. Regulatory notes

| Country | Instrument, number, date | Checked by, date |
|---|---|---|
| Ukraine | found 2026-09-29, not checked — see below | — |
| Romania | not checked | — |
| Poland | not checked | — |
| Slovakia | not checked | — |
| Hungary | not checked | — |
| Serbia | not checked | — |
| Czechia | not checked | — |

**Ukraine, found and not checked.** Read on 2026-09-29 on secondary
copies, because the statute site could not be reached; each is read on
zakon.rada.gov.ua and signed before this row counts as checked. No rule
was found that speaks of collecting rain from one's own roof.

- **Water Code, No. 213/95-ВР,** Art. 1: a water body is a natural or
  artificial element of the environment in which water collects — a
  sea, river, lake, pond, canal, and the like. Art. 47: general water
  use, from water bodies without structures or technical devices, needs
  no permit. Art. 48: special water use is taking water from water
  bodies with structures or technical devices; as quoted on a
  secondary copy, taking up to 5 m³ a day is not special water use.
  Our reading, not a finding: a roof and a cistern are not a water
  body, so the permit regime would not apply; the enquiry below asks.
- **Water Code, Arts. 88–89:** a protective strip of 25 m along small
  streams and around ponds, 50 m on a slope, in which gardening and
  ploughing are not allowed; the seedbeds stay out of it.

The written enquiries: to the regional office of the state water
agency, whether roof water held in a cistern for watering is any kind
of water use under the Code; to the council or planning authority,
whether a buried cistern of 4.2 m³ needs notice or permission; and,
only if Section 3.3 is built, to the district sanitary service, whether
rainwater may flush toilets where children stay.

* * *

## 11. Adaptation notes

The design is a seed, not a copy: a different place grows a different
form from it.

- **A drier valley:** a larger roof or a second one; a larger cistern;
  the pond or another source for the longest droughts.
- **A wetter valley:** the cistern stays at the nursery's need; the
  overflow is sized for the downpours.
- **A colder valley:** the cistern deeper under earth; the pump inside
  a small insulated housing, or drained all winter.
- **A larger nursery:** the cistern scales with the dry weeks it must
  carry; a drip line from a header tank saves water and work.
- **No roof near the nursery:** a plastic tank under the nearest roof,
  and a hose, or the beds moved to the roof.
- **A tile roof:** runoff_factor lowered by up to a tenth.

* * *

## 12. Provenance and licence

- **Written by:** Michel Garand. [set — others as they choose to be
  named]
- **From whose knowledge:** the water working paper, EN v0.1; the Texas
  Manual on Rainwater Harvesting, 3rd ed., Texas Water Development
  Board, 2005; DIN 1989-1, as reported in a German supplier's handbook;
  Voropai and Kunytsia, Українські Карпати, on precipitation; the
  Encyclopedia of Modern Ukraine, entry Карпати; the Ukrainian
  recommendations for growing forest seedlings, Kharkiv, 2010; McDonald,
  in the Forest Nursery Manual, 1984; the Water Code of Ukraine as read
  on secondary copies; Ukrainian retail listings of 2026-09-29 for
  prices.
- **Traditional knowledge:** none. How the valley caught roof water is
  for the elders.
- **Text:** CC BY-SA 4.0
- **Drawings and designs:** [hardware licence — open decision]
- **Measurement data:** none yet
- **Gate 1:** household decision, 2026-09-29, recorded by Michel
  Garand — v0.1 may be published as it stands, at L1, in English,
  Ukrainian, and German
- **Wartime review:** 2026-09-29, Michel Garand — v0.1 read against
  compendium Section 2; nothing places the site; the rainfall is given
  at the resolution of the whole range; accepted

* * *

## 13. What to check

- **The enquiries** — water use, the cistern's standing, and, if built,
  flushing with rainwater.
- **The rainfall** — annual and monthly, from the nearest
  hydrometeorological station, replacing the assumed range and the
  warm-season spread.
- **The roof** — chosen, its plan area and material measured, its
  downpipes counted; if it is asbestos cement, a builder decides how
  the gutters are fixed without cutting or drilling it.
- **The nursery** — nursery_area and nursery_watering from the tree
  nursery module, then from the watering record.
- **The first flush** — first_flush tried against the water's colour
  after the first rains.
- **The cistern or the tank** — the household's choice; a quotation
  replacing the paper's 55 percent.
- **The gutters** — the listed prices turned into a quotation from the
  roof's lengths.
- **The hand pump** — a seller in western Ukraine.
- **The spring** — whether Section 3.3 is needed at all.
- **The Ukrainian row** — every instrument read and signed.
- **From L2, once built:** build times and out-of-order consequences in
  Section 5; the maintenance record in Section 7; early signs and repair
  costs in Section 8; Section 9.

* * *

© 2026 Michel Garand | Carpathian OER Commons | CC BY-SA 4.0
stewardship@ubec.network
