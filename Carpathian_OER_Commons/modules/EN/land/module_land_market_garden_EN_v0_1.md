---
title: "Market Garden: Beds, Rotation, the Season"
subtitle: "Carpathian OER Commons — Land, Forest, Food Module"
author: "Michel Garand"
date: "2026-09-28"
version: "v0.1"
lang: "en"
license: "CC BY-SA 4.0"
project: "Carpathian OER Commons"
status: "L0 — marked draft: sized and designed, not fully costed"
---

*Maturity: **L0**, a marked draft — sized and designed, not yet fully
costed, and published so that it can be read and changed in the open. The
establishment compost and the seed are not priced, and nothing has been
grown. Read every figure below at this level and no higher. The module
moves to L1 when every line in Section 6 carries a dated cost and its
basis.*

*Governed by Section 2 of the compendium. No child appears in this
module in any form. The site is not named; site plans are schematic;
photographs show structures and systems only. Design loads are site
capacity, used for sizing only. No market, town, buyer, route, or day
of distribution is named, and no list of those who eat from the garden
enters the repository.*

*"Market garden" names the method — intensive vegetable growing on
permanent beds — and not a sale. The garden serves the hamlet's table
first; what leaves the hamlet, once the hamlet is fed, goes through the
growers' and eaters' association, a module of its own in Settlement.*

* * *

## 1. Purpose

Fresh vegetables for the hamlet's kitchen and table at capacity, grown
on permanent beds by a paid grower, on ground fed from the garden's own
nutrient stream. What the kitchen cannot use fresh goes to the food
storage module; what the hamlet does not need, once it is fed, goes to
the association.

**Four rules.** The hamlet eats first: the region receives only a
measured surplus. Two nutrient streams kept apart: the toilet stream
feeds trees; only the garden's own stream reaches the beds. The grower
is paid: the garden's work is a cost line, never a contribution, and
toloka is not the name for work the garden depends on. Nothing is
called organic: the methods are described, the produce is not
labelled.

**Connections.** Depends on: the Phase 1 walk of the ground, a soil
analysis, and the season measured or taken from the nearest station;
the compost and site nutrient cycle module for the garden's own stream,
kept apart from the toilet stream, and the biochar module for char
charged in that stream; the rainwater and nursery irrigation module,
whose sizing grows by the garden's demand; the water module for washing
produce in spring water; the legal form decision, since the garden is a
registered capacity of the operator that runs the kitchen. Feeds: the
kitchen and dining module; the food storage module; the growers' and
eaters' association, with its measured surplus only. The terra preta
module does not feed the beds; its product goes to trees, as the
sanitation working paper holds.

**Patterns.** Grows from: not yet named. Where vegetables were grown in
this valley relative to the house, the hayfield, and the slope; how that
ground was fed; and who kept the seed, are questions for the elders
before the first bed is dug. Feeds: not yet named. Resonates with: 177
Vegetable Garden — ground set aside for vegetables, sunny, fenced, with
its tool store beside it; 169 Terraced Slope — permanent beds on the
contour; 104 Site Repair — beds on the best ground, the tunnel, cellar,
and compost bays on the poorer; 147 Communal Eating — the garden serves
one table first; 170 Fruit Trees — where the toilet stream goes, beside
the beds and never in them. In tension with: 178 Compost — Alexander
joins toilets and kitchen waste into one fertiliser; here the two
streams are kept apart, and only the garden's own stream reaches the
beds. 172 Garden Growing Wild — permanent beds are formal ground; the
tension is held at the edges, and by keeping no earth bare. 4
Agricultural Valleys — the best ground here may be hayfield, and a bed
there is taken from winter fodder. 46 Market of Many Shops — the region
is reached through an association of growers and eaters, not a market.

* * *

## 2. Context of validity

| Condition | Range this design holds for |
|---|---|
| Climate | [set] — mountain; frost into May and from late September |
| Frost-free period | frost_free_days, [set] — sources: 60 to 160 days |
| Altitude | [set] |
| Group size | capacity: 34 people, the example below |
| Days of demand | use_days_per_year: 120, the example below |
| Soil | acidic; limed to the analysis before the first bed |
| Slope | beds on the contour; terraced where the ground needs it, [set] |
| Ground | [set] — about 1,600 m² fenced, from the Phase 1 walk |

The frost-free period is read from the literature and not from the
site. A general source gives the Carpathians up to 160 frost-free days,
with mountain valleys shorter by a further 30 to 40; a weaker source
gives 60 to 100 for the mountain zone. At the upper limit of grain
growing, 80 to 100 days stay above 10 °C. The site's own figure comes
from the nearest hydrometeorological station, then from the site's own
record.

* * *

## 3. Sizing method

**What you must measure yourself before using this module:**

- **Your season** — the last spring and first autumn frost, from the
  nearest station for as many years as it holds, then from your own
  thermometer at bed height.
- **Your soil** — a laboratory analysis of pH, humus, and N, P, K, one
  sample for each kind of ground you mean to use. The lime and the
  first compost are set from it.
- **Your ground** — the area of deep, sunny ground that is not needed
  as hayfield, and the length of bed the contour allows.
- **Your demand** — the kitchen's vegetables per person per day, and
  the days of demand in a year, residents included.

**Choose a daily figure per person.** vegetables_per_person: 0.44 kg a
day, net, potatoes excluded, [assumed]. Basis: the rational norm of 161
kg of vegetables and melons per person per year, attributed to the
Ministry of Health, divided by 365. The children's catering norms of
Cabinet Resolution No. 305 of 24 March 2021 give about 0.40 to 0.46 kg
of vegetables a day for a seven-day stay, on our reading of its tables;
the two agree. Potatoes are a field crop here and are left out of the
beds; if the garden grows them, add them with their own yield.

**Choose a yield.** bed_yield: 2 kg per m² of bed per season,
[assumed]. Basis: guide values of 1 to 4 kg per m² for common
vegetables in a Ukrainian agricultural guide of 2025 — cucumbers 1,
tomatoes 1.5, courgettes 2, carrots and beets 3, cabbage 4. The figure
is taken near the low end, for a short mountain season and a garden in
its first seasons. It is replaced by the garden's own record, bed by
bed.

**Choose a bed.** Width 0.75 m and paths 0.45 m, [set], after Fortier's
30-inch beds and 18-inch paths, quoted secondhand. Length 20 m, [set],
as the contour allows. One bed is 15 m².

**Our example:** capacity, 34 people; use_days_per_year, 120;
vegetables_per_person, 0.44 kg; garden_share, 1.0, [set] — the garden
grows every vegetable the kitchen serves on use days, fresh or from
storage; bed_yield, 2 kg per m². Values from the site parameters file,
held in the workshop. Resident households add their own days of demand
to the first line; they are not in the example.

| Quantity | Calculation | Our example |
|---|---|---|
| Demand, a year | people × days × kg × share | 1,795 kg |
| Bed area | demand ÷ yield | 1,795 ÷ 2 = 898 m² |
| Beds | bed area ÷ 15 m², rounded up | 60 beds |
| Ground in beds and paths | beds × 1.2 m × 20 m | 1,440 m² |
| Tunnel, bays, store, turning | [assumed] | about 180 m² |
| Fenced area | sum, as a square | about 40 × 40 m, 160 m of fence |
| Compost, first year | bed area × 5 cm | about 45 m³ |
| Compost, each year after | bed area × 3 cm | about 27 m³ |
| Dolomite, first year | bed area × 0.4 kg, [assumed] | about 360 kg |

The compost figures are Charles Dowding's: from 5 cm to start a bed on
ground that is not weedy, 7 to 12 cm where it is, and about 3 cm a
year after. They are the largest input in this module and the one most
easily forgotten. The garden's own residues and the kitchen's scraps
will not make 45 m³ in the first year; the difference is bought in or
built up over seasons, and the compost module says how.

The dolomite rate is 400 g per m², from a retailer's guide for loam at
pH 4.5 to 5.0; an agronomic table gives 4 to 5.5 t of lime a hectare,
as CaO, for loam at the same pH, once in six to eight years. The
analysis replaces both.

**Read the result against three others.** The example gives about 80 m²
of bed a person for a year of demand. Alexander's Vegetable Garden gives
one-tenth of an acre for a family of four, about 100 m² a person.
Jeavons gives about 4,000 sq ft, about 372 m², for one person's whole
diet, of which vegetables are a small part. The comparison says the
example is not far out; it does not say it is right.

* * *

## 4. Bill of materials

Quantities for the 60-bed example. Alternatives are named in the
design; none is yet known to work here.

| Item | Quantity | Alternatives in the design |
|---|---|---|
| Soil analysis | 2 samples, [set] | none named |
| Dolomite flour | 15 bags of 25 kg | lime to the analysis |
| Compost or manure | about 45 m³, first year | built up over seasons |
| Drip tape, 20 cm emitters | 2,400 m, two lines a bed | hand watering |
| Main line, PE 32 mm | about 80 m, [assumed] | none named |
| Start connectors | 120 | none named |
| Filter and pressure regulator | 1 set | none named |
| Film tunnel | 1, 6 × 20 m, double film | none; covered beds only |
| Welded mesh, 2 m high | 7 rolls of 25 m | none named |
| Fence posts, 2.5 m | 65, 2.5 m apart, [assumed] | timber from the site |
| Wicket and double gate | 1 each | none named |
| Row cover, 30 g/m² | 400 m, a third of the beds, [set] | none named |
| Insect net | 7 rolls of 1.2 × 30 m, ten beds, [set] | none named |
| Hand tools | cultivator, seeder, 2 hoes, ripper, 2 barrows | broadfork |
| Compost bays | 3 bays, 1.5 × 1.5 × 1.0 m, [set] | none named |
| Tool store | 1, metal | timber, from the site |

**The layout, as designed.** Beds run along the contour in blocks,
paths between them, the tunnel and the store on the poorer ground at
one side, the compost bays beside the store and away from the kitchen
door, the wicket toward the kitchen and the double gate toward the
track for deliveries. Drawn as relationships only; the walk sets the
rest.

* * *

## 5. Build

The soil analysis and the liming come first; the fence and the tunnel
before the first beds; the beds in the order the compost allows.

| Step | Trade | Time | If done out of order |
|---|---|---|---|
| Walk, take samples | grower | [from L2] | beds on the wrong ground |
| Soil analysis | laboratory | [from L2] | lime and compost guessed |
| Lime the bed ground | grower | [from L2] | acid-sensitive crops fail |
| Fence and gates | fencer | [from L2] | first crops browsed |
| Tunnel frame and film | fitter | [from L2] | [from L2] |
| Main line, filter, drip | grower | [from L2] | [from L2] |
| Beds: compost laid, no dig | grower | [from L2] | [from L2] |
| Compost bays and store | carpenter | [from L2] | [from L2] |

* * *

## 6. Cost

Estimates, not quotations: each line is a price listed by a Ukrainian
retailer or service platform, seen on 2026-09-28. Place: not a
quotation; national listings, and one platform in western Ukraine for
the tunnel frame. "Listing" below means that listed price.
Exchange rate: exchange_rate, 52 UAH to the euro, the National Bank's
mid-September 2026 rate, rounded.

### 6.1 Ground

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Soil analysis, 2 samples | 1,993 | 38 | estimated, institute's list |
| Dolomite flour, 15 bags of 25 kg | 3,750 | 72 | estimated, listing |
| Compost or rotted manure, about 45 m³ | [set] | [set] | not priced |
| Subtotal, priced lines | 5,743 | 110 | |

### 6.2 Irrigation

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Drip tape, 3 rolls of 1,000 m | 7,629 | 147 | estimated, listing |
| Main line, PE 32 mm, 80 m | 2,960 | 57 | estimated; length [assumed] |
| Start connectors, 120 | 1,200 | 23 | estimated, listing |
| Filter and pressure regulator | 2,322 | 45 | estimated, listing |
| Subtotal | 14,111 | 271 | |

The rainwater cistern and its pump belong to the rainwater module.

### 6.3 Tunnel

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Film tunnel, 6 × 20 m | 100,000 | 1,923 | estimated, listing |
| Frame assembly | 4,500 | 87 | estimated, lower bound of a listed rate |
| Subtotal | 104,500 | 2,010 | |

### 6.4 Fence

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Welded mesh, 2 m, 7 rolls of 25 m | 16,176 | 311 | estimated, listing |
| Posts, 2.5 m, 65 | 28,275 | 544 | estimated; spacing assumed |
| Wicket, 1.0 × 2.0 m | 10,801 | 208 | estimated, listing |
| Double gate, 3 × 2.0 m | 17,135 | 330 | estimated, listing |
| Installation, about 160 m | 28,800 | 554 | estimated, listed rate |
| Wicket and gate installation | 3,600 | 69 | estimated, listed rate |
| Subtotal | 104,787 | 2,015 | |

### 6.5 Covers

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Row cover, 400 m of 1.6 m | 4,880 | 94 | estimated, listing |
| Insect net, 7 rolls of 1.2 × 30 m | 11,151 | 214 | estimated, listing |
| Subtotal | 16,031 | 308 | |

### 6.6 Tools

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Wheeled hand cultivator | 1,500 | 29 | estimated, listing |
| Precision seeder | 2,700 | 52 | estimated, listing |
| Hoes, 2 | 1,898 | 36 | estimated, listing |
| Lever ripper | 1,451 | 28 | estimated, listing |
| Wheelbarrows, 2 | 8,200 | 158 | estimated, listing |
| Subtotal | 15,749 | 303 | |

### 6.7 Bays and store

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Compost bays, about 0.4 m³ of board | 5,160 | 99 | estimated, listing |
| Metal tool store | 16,900 | 325 | estimated, listing |
| Subtotal | 22,060 | 424 | |

### 6.8 Summary

| Section | UAH | EUR |
|---|---|---|
| Ground, priced lines | 5,743 | 110 |
| Irrigation | 14,111 | 271 |
| Tunnel | 104,500 | 2,010 |
| Fence | 104,787 | 2,015 |
| Covers | 16,031 | 308 |
| Tools | 15,749 | 303 |
| Bays and store | 22,060 | 424 |
| Construction subtotal | 282,981 | 5,442 |
| Design check, 8 percent | 22,600 | 435 |
| Contingency, 20 percent | 56,600 | 1,088 |
| **Total external cost, priced lines** | **362,181** | **6,965** |

The total leaves out the first year's compost and the first year's
seed, which are not priced. It is not the garden's cost until they are.
The percentages are the working papers' own.

**Contribution, not in the total.** None counted. The grower's work is
a cost, not a contribution.

**Running cost.** The grower's pay, set each season by the association's
pledges; its floor is the legal minimum wage, 8,647 UAH a month in
2026, for the months the garden is worked, [set]. Seed, [set]. Tunnel
film, rated for six seasons: about 22 m of 12 m film at a listed 640
UAH a metre, 14,080 UAH, [assumed] length, about 2,350 UAH a season.
Soil analysis every few years; lime once in six to eight years. Drip
tape replacement, [from L2].

* * *

## 7. Operation and maintenance

Responsible: the grower, with a deputy — [from L2]. One named role,
paid; not a rota of residents.

- **Daily, in season:** [from L2]
- **Seasonal:** compost laid on each bed as it is cleared; covers on
  before a forecast frost; the tunnel closed at night in spring and
  autumn.
- **Annual:** the bed record — what was sown, when, and what each bed
  gave — kept and carried into the next season's plan and into the
  bed_yield parameter; the film checked; the fence walked.

If the programme works in the garden, that is described in the
programme modules, in standing format. No produce, photograph, or share
is tied to a child.

* * *

## 8. Failure modes

From the design, not from experience.

| Failure | Early sign | Repair and cost |
|---|---|---|
| Frost on open beds | [from L2] | covers, the tunnel; [from L2] |
| Compost short of the beds | [from L2] | fewer beds, then more |
| Acid-sensitive crops failing | [from L2] | lime to the analysis |
| Animals through the fence | [from L2] | [from L2] |
| Water short in a dry spell | [from L2] | the rainwater reserve |
| One grower, no deputy | [from L2] | the association's terms |
| Produce refused | [from L2] | registration before the harvest |

* * *

## 9. What we got wrong

Nothing yet: this module has not been built.

* * *

## 10. Regulatory notes

| Country | Instrument, number, date | Checked by, date |
|---|---|---|
| Ukraine | found 2026-09-28, not checked — see below | — |
| Romania | not checked | — |
| Poland | not checked | — |
| Slovakia | not checked | — |
| Hungary | not checked | — |
| Serbia | not checked | — |
| Czechia | not checked | — |

**Ukraine, found and not checked.** Instruments found on 2026-09-28,
read on secondary copies of the statute; each is read on
zakon.rada.gov.ua and signed before this row counts as checked. Law No.
771/97-ВР of 23.12.1997 on food safety and quality, as amended to Law
No. 4718-IX of 16.12.2025: primary production of plant products needs
no operating permit (Art. 23) but its capacity is registered, free, at
least ten days before starting (Art. 25; Minagro Order No. 431 of
15.02.2024); HACCP does not apply to primary production (Art. 21);
home-made food may be sold only at agri-food markets (Art. 37), where
plant products are tested by the market's laboratory (Art. 36). Cabinet
Resolution No. 305 of 24.03.2021: a children's establishment is supplied
by a food market operator, with documents. MOH Order No. 377 of
20.03.2026: the sanitary regulation for children's health and recreation
establishments of any ownership, catering included. Law No. 742-IV of
15.05.2003: a personal peasant household may sell its surplus, and that
is not business activity. Tax Code, subparagraph 165.1.24: income from
selling one's own produce is untaxed up to 2 ha, with a council
certificate. Law No. 2496-VIII of 10.07.2018: no produce is called
organic, bio, or eco without certification. Which of these binds this
garden depends on its legal form, an open decision. The written enquiry
to the district food-safety service, with the design drawn, comes before
the first harvest reaches the kitchen.

* * *

## 11. Adaptation notes

The design is a seed, not a copy: a different place grows a different
form from it.

- **A drier valley:** the drip line carries more of the season; size
  the rainwater cistern to the beds before the beds.
- **A colder valley:** fewer open beds and more under cover; the tunnel
  first, and crops chosen to the measured season.
- **A smaller group:** recalculate with Section 3; the fence and tunnel
  do not shrink in proportion, so the cost per bed rises.
- **A larger group:** recalculate with Section 3; the compost need grows
  with the beds, and it is the first thing to run short.
- **Neutral soil:** leave out the lime; keep the analysis.

* * *

## 12. Provenance and licence

- **Written by:** Michel Garand. [set — others as they choose to be
  named]
- **From whose knowledge:** Jean-Martin Fortier, The Market Gardener,
  for the bed and path widths, quoted secondhand; Charles Dowding, for
  the compost depths; John Jeavons and Ecology Action, and Christopher
  Alexander's Vegetable Garden, for the comparison of areas; the
  rational norm of vegetable consumption and Cabinet Resolution No. 305
  for demand; a Ukrainian agricultural guide of 2025 for yields; a
  retailer's guide and an agronomic table for liming; Ukrainian retail
  and service listings of 2026-09-28 for prices.
- **Traditional knowledge:** none. Where vegetables were grown, how the
  ground was fed, what was grown, and whose seed, are for the elders.
- **Text:** CC BY-SA 4.0
- **Drawings and designs:** [hardware licence — open decision]
- **Measurement data:** none yet
- **Gate 1:** household decision, 2026-09-28, recorded by Michel
  Garand — module may be published as it stands, as a marked draft
- **Wartime review:** 2026-09-28, Michel Garand — read against
  compendium Section 2; nothing places the site; accepted

* * *

## 13. What to check

- **Establishment compost** — a dated price for about 45 m³ of compost
  or rotted manure, or the garden stream designed to supply it over
  seasons; this line moves the module to L1.
- **Seed** — the first season's seed, priced from a crop plan.
- **The season** — frost_free_days from the nearest station, then the
  site's own record.
- **Altitude and climate** ranges for Section 2.
- **The soil** — the analysis, replacing the assumed loam and pH and
  the dolomite rate.
- **The ground** — the walk: area, aspect, contour length, and whether
  the best ground is hayfield; replaces the 180 m², the 160 m of fence,
  and the 80 m of main line.
- **vegetables_per_person** — the kitchen's own menu, replacing the
  rational norm.
- **bed_yield** — the garden's own record, bed by bed, from the first
  season.
- **garden_share** — set by the association and the kitchen.
- **Resident days of demand** — once resident households are known.
- **Fortier's bed and path widths** — checked against a copy of The
  Market Gardener, with the page.
- **Resolution No. 305** — the portion tables read on
  zakon.rada.gov.ua, confirming our reading of 0.40 to 0.46 kg a day.
- **Irrigation demand** — carried into the rainwater module and its
  cistern.
- **The Ukrainian row** — every instrument read and signed; the written
  enquiry to the district food-safety service.
- **Quotations** for the lines in Section 6, dated, to replace the
  listings.
- **From L2, once built:** build times and out-of-order consequences in
  Section 5; the grower's daily tasks in Section 7; early signs and
  repair costs in Section 8; Section 9.

* * *

© 2026 Michel Garand | Carpathian OER Commons | CC BY-SA 4.0
stewardship@ubec.network
