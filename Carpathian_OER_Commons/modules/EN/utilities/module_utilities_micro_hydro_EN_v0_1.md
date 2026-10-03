---
title: "Micro-Hydro, If the Stream Allows"
subtitle: "Carpathian OER Commons — Utilities Module"
author: "Michel Garand"
date: "2026-10-03"
version: "v0.1"
lang: "en"
license: "CC BY-SA 4.0"
project: "Carpathian OER Commons"
status: "L0 — marked draft: sized and designed, partly costed, nothing measured or asked"
---

*Maturity: **L0**, a marked draft — a sizing method and a design,
published so that they can be read and changed in the open. No stream
has been measured, no enquiry sent, and nothing priced beyond the
working paper's estimates; the intake screen, the powerhouse, the
environmental impact assessment, and the fence are not priced. Read
every figure below at this level and no higher. The module moves to L1
when the stream is measured in its driest and its coldest month, the
enquiries in Section 10 are answered in writing, and every line in
Section 6 carries a dated cost and its basis.*

*Governed by Section 2 of the compendium. No child appears in this
module in any form. The site is not named; site plans are schematic;
photographs show structures and systems only. Design loads are site
capacity, used for sizing only.*

*Converted from the energy working paper, EN v0.1, Sections 5 and 7.6.
Three things change from the paper, decided on 2026-10-03: the turbine
is sized against the energy module's loads at 34 people; the law is
set out as found — a special water-use permit, a probable
environmental impact assessment, fish protection, and a residual flow,
for a turbine of any size; and the public debate on small hydropower
in the Carpathians is stated, because a reader should know it before
touching a stream.*

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

Winter electricity from a stream, if the site has one and the law and
the stream allow it: an intake, a buried pipe, a small turbine, and a
controller that sends what the site does not use into hot water. It
answers the one weakness of the energy module — the darkest month,
when the sun is lowest and a mountain stream often runs strongest —
and lets the generator rest.

**Five rules.** The stream first: the turbine takes only what the
stream gives above the residual flow agreed in writing, and the reach
it pipes keeps running. Measure before anything is priced: head with a
level, flow in the driest and the coldest month. Ask before anything
is built: the permit, the impact assessment, and the fish come before
the turbine. Never stop the water in frost: a pipe that stands still
in winter freezes. Nothing taken away: the battery and the generator
stay as they are; the turbine adds a source and takes away only part
of the array.

**Connections.** Depends on: a stream within reach; the stream's head
and flow, measured; the written answers in Section 10; the energy
module, whose circuits it feeds and whose battery and generator it
keeps; the market garden's pond, which shares the stream's dry-month
flow; the Phase 1 walk, with the Water Code's strip measured. Feeds:
the energy module's essential and general circuits; the wood heat
module's buffer tank, through the dump load, as an option.

**Patterns.** Grows from: not yet named. Whether the valley's streams
were ever set to work, and how a stream is held here — who may take
from it and what is owed to it — are questions for the elders before
any intake is built. Feeds: not yet named. Resonates with: 104 Site
Repair — the powerhouse outside the strip, on poorer ground; 230
Radiant Heat — a turbine's surplus, through its dump load and the
buffer tank, warming rooms rather than wasted. In tension with: 64
Pools and Streams — a turbine takes a reach of the stream into a pipe;
the residual flow is what keeps that reach running and in view. 25
Access to Water — an intake and a powerhouse set structures in the
belt the pattern keeps open. 71 Still Water — the intake pool is
fenced, never a place to swim. The walk status of each is set after
the Phase 1 walk, on a later date; until then, unknown (compendium
Section 26).

* * *

## 2. Context of validity

| Condition | Range this design holds for |
|---|---|
| Stream | within reach, flowing in its driest and coldest month |
| Head | about 10 m or more over the pipe's length, [set] |
| Flow | above the residual flow and the pond's share, [set] |
| Output | about 0.25 to 1 kW, continuous |
| Climate | mountain; frost and ice in the intake, Section 3.4 |
| Law | a permit and the enquiries answered, Section 10 |
| Group size | capacity: 34 people, through the energy module |

Where the stream is a brook too small to spare a residual flow, or the
answers refuse it, there is no turbine, and the energy module stands
alone.

* * *

## 3. Sizing method

**What you must measure yourself before using this module:**

- **Your head** — the height from the intake to the turbine, with a
  surveyor's level and staff, or a water-filled hose and a pressure
  gauge, about 0.1 bar a metre. Not with a cheap altimeter, which is
  commonly out by 46 m or more (Kindberg, Micro-Hydro Power, NCAT,
  2011).
- **Your flow** — with a bucket and a stopwatch where all the water can
  be caught, with a temporary weir where it cannot; monthly for a year
  if you can, and at least in the driest month and the coldest. A float
  gives a rough figure only; the sources' correction factors differ,
  0.60 to 0.85 in ESHA's guide (2004) and lower in NCAT's.
- **Your pipe's route** — its length and fall, from the walk.
- **Your loads** — from the energy module, Section 3.

**Our example:** turbine_efficiency, 0.5 to 0.6, water to wire;
december_sun and the energy module's loads at capacity, 34 people;
exchange_rate, 52 UAH to the euro. Values from the site parameters
file, held in the workshop.

### 3.1 The power

Power in kilowatts is head in metres × flow in litres a second × 9.81
÷ 1,000 × the efficiency; at 0.5, about head × flow × 0.005, as the
paper has it.

| Head | Flow | At 0.5 | At 0.6 | A day, at 0.5 |
|---|---|---|---|---|
| 10 m | 10 L/s | 0.49 kW | 0.59 kW | 11.8 kWh |
| 20 m | 10 L/s | 0.98 kW | 1.18 kW | 23.5 kWh |
| 20 m | 5 L/s | 0.49 kW | 0.59 kW | 11.8 kWh |
| 30 m | 15 L/s | 2.21 kW | 2.65 kW | 53.0 kWh |

The efficiency is the whole chain, water to wire. Pelton and Turgo
wheels are 80 to 95 percent efficient on their own, crossflows 65 to
85, generators about 80; whole systems 50 to 70 percent (Kindberg,
NCAT, 2011); about 60 percent below 50 kW (GTZ, Micro Hydro Power Scout
Guide, 2009). Pelton and Turgo hold their efficiency at part flow
better than most (Paish, Renewable and Sustainable Energy Reviews 6,
2002).

### 3.2 What the site needs

| Quantity | Calculation | Our example |
|---|---|---|
| Darkest-month deficit | 5.5–6.0 kWh ÷ 24 h | about 0.25 kW |
| Both circuits, winter, all day | 9.33 kWh ÷ 24 h | about 0.39 kW |
| Head × flow for 0.4 kW, at 0.5 | 0.4 ÷ 0.0049 | about 82 m·L/s |
| For example | 20 m × 4.1 L/s | 0.4 kW |
| Water through it, a day | 4.1 L/s × 86,400 s | about 354 m³ |

A set of about 0.4 to 0.5 kW, running all day, carries both circuits
through the winter. Anything above that goes to the dump load. A
turbine of 1 kW at 30 m of head needs about 6.8 L a second, about 590
m³ a day.

**What it lets the array give up.** The paper cuts the array from 6 to
about 4 kWp when a stream is developed, returning about 30,000 UAH;
four fewer 550 W modules at the paper's 8,800 UAH are 35,200 UAH
before their share of the mounting. The stream's own driest month is
often in late summer, when the sun is strongest, so the smaller array
still carries the summer. The battery keeps its four days, because a
turbine stops for ice, for drought, and for repair; the generator
stays, as a reserve that hardly runs.

### 3.3 The stream's share

| Share | Who decides | Our example |
|---|---|---|
| Residual flow, left in the stream | the enquiry, in writing | [set] |
| The market garden's pond | the market garden module | about 0.08 L/s |
| The turbine | what is left, in the month it runs | [set] |

**The residual flow.** Ukraine has no approved method for the flow a
diversion must leave in a stream; practice follows an older norm, the
lowest average monthly flow at 95 percent probability (Huliaieva and
Khorev, WWF-Ukraine, 2024). The European reference is the Common
Implementation Strategy's Guidance No. 31 on ecological flows (European
Commission, 2015). A site cannot compute the norm from a year of
bucket readings; the enquiry asks the water agency to set it, and the
turbine is sized from what is left.

**The pond.** The market garden's pond needs about 5 L a minute in a
dry week, about 0.08 L a second, from the same stream.

### 3.4 The intake, the pipe, and winter

**The intake.** A Coanda screen — a fine-slotted plate the water runs
over, which drops the water through and sheds leaves and stones —
with slots of about 1 to 1.5 mm, needs no power and clears itself; at
one site where basket screens clogged with autumn leaves in hours,
Coanda screens raised the year's output by 15 percent (Palmer,
International Water Power and Dam Construction, 2004). A screen of
this kind passes about 8 to 17 L a second for a 360 mm width
(PowerSpout, product data). A screen that fine is also how, on our
reading, the intake meets the law's call for a fish-protection device
(Section 10).

**Ice.** Frazil — ice crystals that form in supercooled, fast water —
clings to screens and racks and can block an intake; mountain sites,
cold and swift and hard to reach, favour it (Ettema, Kirkil, and Daly,
Cold Regions Science and Technology 55, 2009). A stable ice cover over
the intake pool helps, and so does a submerged intake.

**The pipe.** Buried below the frost line, polyethylene rather than
PVC, and never stopped in frost: if the turbine must be cleared, a
purge valve is opened first, and if the pressure falls in a hard frost
of about −7 °C, the intake is closed and the pipe drained (PowerSpout,
Cold weather hydro, 2015; Montana Consumer Guide to Micro-hydro, 2016).
The paper's pipe is polyethylene, 110 mm, about 100 m, [set] from the
route.

**The dump load.** An electronic load controller holds the turbine's
speed by sending what the site does not use into a resistive load,
usually rated at the generator's output (Raja Singh and colleagues,
Engineering Science and Technology 21, 2018); a water or space heater
is the usual load (Montana Guide, 2016). Here, as an option, an
immersion element in the wood heat module's buffer tank: the surplus
heats water instead of air.

* * *

## 4. Bill of materials

Quantities for the example. Alternatives are named in the design; none
is yet known to work here.

| Item | Quantity | Alternatives in the design |
|---|---|---|
| Turbine set, about 1 kW, controller | 1 | Turgo or crossflow |
| Intake weir and settling basin | 1 | none named |
| Coanda screen, 1–1.5 mm slots | 1 | none named |
| Penstock, PE 110 mm | about 100 m, [set] | none named |
| Purge valve, pressure gauge | 1 each | none named |
| Dump load, immersion element | 1 | an air heater |
| Powerhouse, small, lockable | 1 | none named |
| Fence and gate at the intake pool | 1 | none named |
| Cable to the energy module | [set] | none named |

**The siting, as designed.** None measured yet; every rule below is
checked on the ground and with the authorities before anything is dug.

| What | Rule |
|---|---|
| The diverted reach | as short as the head allows |
| The residual flow | left at the intake, in every month |
| The intake | screened, fenced, reachable in winter |
| The pipe | buried below the frost line |
| The powerhouse | outside the strip, if the enquiry asks it |
| The outflow | back into the same stream |
| Every part | out of the spring's catchment |

The Water Code's protective strip is 25 m along a small stream, 50 m on
a slope, and building in it is not allowed except for hydrotechnical
and some other structures; whether a powerhouse counts as one is asked
(Section 10).

**The layout, as designed.** Intake and screen, settling basin, buried
pipe down the fall, powerhouse, outflow to the same stream; cable to
the energy module's board; the dump load in the buffer tank. Drawn as
relationships only; the walk sets the rest.

* * *

## 5. Build

| Step | Trade | Time | If done out of order |
|---|---|---|---|
| The elders asked | household | [from L2] | [from L2] |
| Head and flow measured, a year | household | [from L2] | mis-sized |
| Enquiries answered, permit | household | [from L2] | unlawful intake |
| Impact assessment, if asked | assessor | [from L2] | permit refused |
| Intake and settling basin | builder | [from L2] | [from L2] |
| Pipe laid and buried | excavator | [from L2] | frozen pipe |
| Powerhouse | builder | [from L2] | [from L2] |
| Turbine, controller, dump load | electrician | [from L2] | overspeed |
| Connected to the energy module | electrician | [from L2] | [from L2] |
| Fence and gate | builder | [from L2] | an open pool |

* * *

## 6. Cost

Estimates, not quotations: every priced line is the energy paper's own
estimate for autumn 2026, marked "paper"; re-pricing from dated
listings was tried on 2026-10-03 and could not be done. Place: not a
quotation. Exchange rate: exchange_rate, 52 UAH to the euro, the
National Bank's mid-September 2026 rate, rounded.

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Turbine, generator, controller, 1 kW | 90,000 | 1,731 | paper |
| Intake and settling basin | 40,000 | 769 | paper |
| Penstock, PE 110 mm, about 100 m | 25,000 | 481 | paper |
| Dump load and wiring | 10,000 | 192 | paper |
| Coanda screen | [set] | [set] | not priced |
| Powerhouse | [set] | [set] | not priced |
| Fence and gate | [set] | [set] | not priced |
| Environmental impact assessment | [set] | [set] | not priced |
| Special water-use permit | 0 | 0 | quoted, Diia |
| Subtotal, priced lines | 165,000 | 3,173 | |
| Less the array cut to about 4 kWp | −30,000 | −577 | paper |

No percentages are taken on a subtotal this incomplete. The permit is
issued without charge (Diia, the state's service guide).

**Contribution, not in the total.** None. The labour is in the cost,
paid.

**Running cost.** Rent for the water passed through the turbine, under
the Tax Code, Art. 255: at the rate shown on a secondary copy, 12.95
UAH for 10,000 m³, which may be out of date, 354 m³ a day for a year
would be about 170 UAH. The intake cleared, the screen checked, and
the bearings serviced: [set] hours, paid.

* * *

## 7. Operation and maintenance

Responsible: one named adult, paid, with a deputy — [from L2].

- **Daily, in frost:** the pipe's pressure read at the gauge; the
  intake looked at for ice.
- **Weekly:** the screen and the settling basin cleared; the residual
  flow seen to pass.
- **Autumn:** leaves cleared from the intake more often while they
  fall.
- **Yearly:** the turbine and controller serviced; the permit's terms
  checked against what was taken.

How the programme relates to this work is described in the programme
modules, in standing format.

* * *

## 8. Failure modes

From the design, not from experience.

| Failure | Early sign | Repair and cost |
|---|---|---|
| Screen clogged with leaves | output falls | clear it; [from L2] |
| Frazil on the screen | output falls in frost | clear; a cover of ice |
| Pipe frozen | pressure falls | drain it; never stop it |
| Stream below its share | turbine starves | stop it; the residual first |
| Controller fails | turbine overspeeds | shut the valve |
| Flood at the intake | stones, debris | clear; [from L2] |

* * *

## 9. What we got wrong

Nothing yet: this module has not been built.

* * *

## 10. Regulatory notes

| Country | Instrument, number, date | Checked by, date |
|---|---|---|
| Ukraine | found 2026-10-03, not checked — see below | — |
| Romania | not checked | — |
| Poland | not checked | — |
| Slovakia | not checked | — |
| Hungary | not checked | — |
| Serbia | not checked | — |
| Czechia | not checked | — |

**Ukraine, found and not checked.** Read on 2026-10-03 on secondary
copies — protocol.ua, kodeksy.com.ua, and the state's service guide —
because the statute site could not be reached; each is read on
zakon.rada.gov.ua and signed before this row counts as checked.

- **Water Code, No. 213/95-ВР,** Art. 48: special water use is taking
  or using water from water bodies with structures or devices, energy
  among its purposes; passing water through hydro structures is
  excluded from it, except hydropower — so a turbine is special water
  use. Taking up to 5 m³ a day is excluded, and a turbine takes far
  more. The state's service guide reads the hydropower exclusion the
  other way; the Code's own wording is followed until the enquiry
  answers. Art. 49: special water use needs a permit, issued by the
  territorial bodies of the state water agency within thirty days. Art.
  66: hydropower users keep to the operating rules and provide passage
  for fish to their spawning grounds. Art. 80: on small rivers, no
  channel is blocked without passages. Art. 87: water protection zones,
  set by projects. Arts. 88 and 89: a protective strip of 25 m along a
  small stream, doubled where the slope is over 3°, in which building
  is not allowed except for hydrotechnical and some other structures.
- **Cabinet Resolution No. 321 of 13.03.2002,** the permit procedure for
  special water use, amended by No. 648 of 04.06.2025, not read: a
  first permit for three years; applications in person, by post, or
  online; no fee (Diia).
- **Law No. 2059-VIII of 23.05.2017, on environmental impact
  assessment,** Art. 3, part 3, item 4: hydroelectric power plants on
  rivers, regardless of capacity, are in the second category, which
  needs an assessment. Whether a brook counts as a river is asked.
- **Law No. 3677-VI of 08.07.2011, on fisheries,** Art. 17: no water
  intake may be operated without a fish-protection device.
- **Tax Code,** Art. 255: rent on the water passed through turbines.
- **Order No. 26 of the Ministry of Ecology, 26.01.2017,** on water
  balances, defines a minimum ecological flow, as reported by
  WWF-Ukraine; not read.

**The fish.** Grayling is listed as vulnerable in the Red Data Book of
Ukraine, threatened in Carpathian rivers by hydropower and the
breaking of rivers into pieces (Mruk and colleagues, Journal for
Nature Conservation 81, 2024); campaigners name stream trout and the
huchen beside it.

**The public debate.** Small hydropower is contested in the Ukrainian
Carpathians. In 2011 an oblast council approved sites for 360 small
plants, about 700 MW; a court annulled the decision in 2012, and two
other oblast administrations imposed moratoria that spring
(Stankevych-Volosianchuk and Luksha, Ekosphera, 2013); a third planned
one in 2015. Conservation groups — Ekosphera, WWF-Ukraine, the
Ukrainian Nature Conservation Group — oppose new plants for what they
do to a river's water and fish and for how little they add to the
country's energy, small hydropower being about 2 percent of its
renewable supply (Stankevych-Volosianchuk, 2025). Those who build them
point to power without emissions, income for a village budget, and
the country's renewable targets (Divnych, Zbruč, 2013; Mudra, 2018).
A set of one kilowatt for one site is not a plant for the grid; it
still takes a reach of a stream, and this module holds it to the same
law and the same questions.

The written enquiries: to the territorial body of the state water
agency, whether the turbine is special water use, what residual flow
it must leave, and on what terms a permit is given; to the regional
environmental authority, whether the stream counts as a river under
the impact assessment law; to the regional fish protection body, what
device the intake needs; to the council, the strip, the water
protection zone, and whether a powerhouse may stand in the strip. No
intake is built before they are answered.

* * *

## 11. Adaptation notes

The design is a seed, not a copy: a different place grows a different
form from it.

- **A steeper stream:** more head, less water; a Pelton wheel, a longer
  pipe, a smaller share of the stream.
- **A flatter stream:** less head, more water; a crossflow, and a
  larger residual question.
- **A colder valley:** the intake below a stable ice cover, the pipe
  deeper, the purge valve and gauge watched daily.
- **A smaller site:** a few hundred watts carries an essential circuit;
  the dump load may heat one tank.
- **No stream, or no answer:** no turbine; the energy module's
  generator carries the winter.

* * *

## 12. Provenance and licence

- **Written by:** Michel Garand. [set — others as they choose to be
  named]
- **From whose knowledge:** the energy working paper, EN v0.1; Paish,
  2002; Kindberg, NCAT, 2011; ESHA, 2004; GTZ, 2009; the Montana
  Consumer Guide to Micro-hydro, 2016; European Commission, Guidance No.
  31, 2015; Huliaieva and Khorev, WWF-Ukraine, 2024; Palmer, 2004;
  PowerSpout's product data and guidance; Ettema, Kirkil, and Daly,
  2009; Raja Singh and colleagues, 2018; Mruk and colleagues, 2024;
  Ekosphera, 2013 and 2025; Zbruč, 2013; the Ukrainian instruments in
  Section 10, as read on secondary copies.
- **Traditional knowledge:** none. How the valley held its streams is
  for the elders.
- **Text:** CC BY-SA 4.0
- **Drawings and designs:** [hardware licence — open decision]
- **Measurement data:** none yet
- **Gate 1:** household decision, 2026-10-03, recorded by Michel Garand —
  v0.1 may be published as it stands, at L0 as a marked draft, in English,
  Ukrainian, and German
- **Wartime review:** 2026-10-03, Michel Garand — v0.1 read against
  compendium Section 2; nothing places the site; the shelter, the safety
  link, the battery, the generator, and the fuel store in standing format;
  accepted

* * *

## 13. What to check

- **The stream** — whether there is one in reach; its head; its flow,
  monthly for a year, at least in the driest and the coldest month.
- **The enquiries** — the permit, the residual flow, the impact
  assessment, the fish-protection device, the strip.
- **The elders** — how the valley holds its streams.
- **The route** — the pipe's length and fall, the powerhouse's place.
- **The efficiency** — the set's own figure, from its maker, against
  0.5 to 0.6.
- **Quotations** — every line in Section 6, and the unpriced ones.
- **The rent** — the current rate in the Tax Code.
- **The Ukrainian row** — every instrument read and signed.
- **From L2, once built:** build times and out-of-order consequences in
  Section 5; the maintenance record in Section 7; early signs and repair
  costs in Section 8; Section 9.

* * *

© 2026 Michel Garand | Carpathian OER Commons | CC BY-SA 4.0
stewardship@ubec.network
