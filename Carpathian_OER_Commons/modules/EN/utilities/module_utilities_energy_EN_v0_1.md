---
title: "Energy: PV, Storage, Generator"
subtitle: "Carpathian OER Commons — Utilities Module"
author: "Michel Garand"
date: "2026-10-03"
version: "v0.1"
lang: "en"
license: "CC BY-SA 4.0"
project: "Carpathian OER Commons"
status: "L1 — designed, costed from estimates, untested"
---

*Maturity: **L1** — designed and costed, untested. Every cost line is
the working paper's estimate for autumn 2026, labelled as such in
Section 6; the loads are the paper's, recalculated at capacity, until
the appliances are chosen. Nothing has been built. Read every figure
below at this level and no higher.*

*Governed by Section 2 of the compendium. No child appears in this
module in any form. The site is not named; site plans are schematic;
photographs show structures and systems only. Design loads are site
capacity, used for sizing only.*

*What keeps people safe is described in standing format. The shelter,
the safety link, the battery, the generator, and the fuel store appear
here as what each must do and how it is sized — never where it stands,
what fuel is held, or when anything is run. The shelter's own supply
is given as a principle and a method, without its figures.*

*Converted from the energy working paper, EN v0.1, Sections 1 to 4, 6,
7, and 9. Its Section 5 and 7.6 become the micro-hydro module; its
Section 8 becomes the wood heat and hot water module. Five things
change from the paper, decided on 2026-10-03: every load is
recalculated at 34 people, not 25, and the loads the published modules
add are carried; the December sun is taken from the building-climate
standard, about half the paper's; the battery is four modules, not
three, so that four days of the essential circuit still hold; the
generator stands outdoors and its fuel apart, as the fire rules have
held since 2024; and the second circuit is the general circuit.*

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

Electricity for light, cold, communications, water treatment, and the
safety of the site, through the winter and through the outages the
country lives with, whether or not a grid connection exists. Panels, a
battery, and a generator held in reserve, in standard parts that local
trades sell, fit, and repair.

**Five rules.** Two circuits: an essential circuit — light,
communications, the safety link, medical cold, the shelter, water
treatment, the toilets' fans — sized to run for days without sun or
fuel, and a general circuit that may go dark without harm. Storage
before generation: four days of the essential circuit in the battery
are worth more than more panels. Generation ranked by season: the sun
carries the site from March to October; in winter the general circuit
leans on the generator, or on a stream if one is ever developed. No
heat from electricity: heat and hot water come from wood and the sun,
in the wood heat module. Nothing critical waits on fuel: the essential
circuit runs on the battery and the sun alone; the generator only
shortens the winter deficit of the general circuit.

**Connections.** Depends on: the appliance list, once the kitchen,
medical room, and workshop are equipped; the Phase 1 walk, with the
December horizon, the roof or ground for the array, the battery room,
and the poorer ground; whether a grid connection exists; the
electrician who will certify the installation, chosen before the design
is fixed; the written enquiries in Section 10. Feeds: the water module,
with its UV unit; the toilets module, with its fans; the market garden,
with its pump, on the general circuit; the rainwater module, with its
pump, if its Section 3.3 is ever built; the wood heat module, with any
circulation or solar pump; the shelter, the warning and communications
module, and the medical room. Takes from: the micro-hydro module, if a
stream is developed.

**Patterns.** Grows from: not yet named. Which ground the valley keeps
for hay and which may carry an array, and how a household here met the
dark months before the grid, are questions for the elders. Feeds: not
yet named. Resonates with: 104 Site Repair — the array, the generator,
and the fuel store on poorer ground, never on the best; 252 Pools of
Light — light set low and apart where people gather, dark between,
which is also what the essential circuit can carry; 18 Network of
Learning — the battery's record through December kept in the open, as
the site's own series; 83 Master and Apprentices — paid hands learning
the wiring beside the electrician who certifies it. In tension with:
105 South Facing Outdoors and 161 Sunny Place — a ground array wants
the same south-facing ground as the places people sit; a roof array
leaves it to them. 4 Agricultural Valleys — an array on the hayfield
takes the ground the valley may hold for hay. The walk status of each
is set after the Phase 1 walk, on a later date; until then, unknown
(compendium Section 26).

* * *

## 2. Context of validity

| Condition | Range this design holds for |
|---|---|
| Climate | mountain; December sun as in Section 3.2 |
| Altitude | [set] |
| Group size | capacity: 34 people, the example below |
| Season of use | all seasons; the darkest month sizes it |
| Grid | none, or one that fails; Section 10 |
| Shade | none on the array at December midday, [set] |
| Battery room | above 0 °C whenever the battery charges |
| Heat | none from electricity; the wood heat module |

Where the December horizon takes the low sun, every winter figure below
falls with it; the walk records the horizon before the array is placed.

* * *

## 3. Sizing method

**What you must measure yourself before using this module:**

- **Your loads** — the appliance list, with each appliance's power and
  hours, from datasheets, and the safety link's average draw, measured
  over a week with a plug-in meter, not taken from a datasheet.
- **Your sun** — the monthly figures for your region from a published
  source, and your December horizon, walked and recorded.
- **Your battery room** — its lowest temperature in the coldest week,
  with a thermometer left in it.
- **Your grid** — whether a connection exists, and what it costs to
  keep.

**Our example:** capacity, 34 people; december_sun, 0.65 to 0.74 kWh a
m² a day; performance_ratio, 0.86; battery_usable, 0.90; battery_days,
4; generator_fuel, 1.0 to 1.5 L an hour; exchange_rate, 52 UAH to the
euro. Values from the site parameters file, held in the workshop.

### 3.1 The loads

The paper's loads at 25 people, recalculated at 34: lines that grow
with people are scaled by 34/25, [assumed]; fixed lines keep the
paper's figure.

| Load | kWh a day | Basis |
|---|---|---|
| Lighting, 34 points × 8 W × 5 h | 1.36 | scaled, [assumed] |
| Communications, router and phones | 0.30 | paper |
| The safety link and the shelter, together | 1.50 | paper |
| Medical refrigerator | 0.50 | paper |
| UV unit, water module | 0.20 | paper |
| Toilet fans, six, continuous | [set] | toilets module |
| **Essential circuit** | **3.86 + fans** | |
| Kitchen refrigeration | 2.18 | scaled, [assumed] |
| Kitchen small appliances | 0.54 | scaled, [assumed] |
| Laundry | 0.95 | scaled, [assumed] |
| Laptops, documentation | 0.60 | paper |
| Workshop tools | 0.50 | paper |
| Heating circulation pump, winter | 0.70 | paper; 0 by gravity |
| **General circuit, winter** | **5.47** | |
| **Both, winter** | **9.33 + fans** | paper: 8, sized at 9 |

**Loads the paper did not carry.** On the essential circuit: the six
toilet fans of the toilets module, 12 V, each running continuously, so
that every watt a fan draws adds 0.024 kWh a day; fire detection and
night lighting, and the warning receivers, when their modules are
designed. On the general circuit: the market garden's pump, in the sun
months, moving about 7 m³ a day in a dry week; the food store's cold
room; the washroom's ventilation; the solar loop's pump in the wood
heat module; and the rainwater module's pump, only if its Section 3.3
is ever built. Each is [set] until its appliance is chosen; none of
the general circuit's additions runs in the darkest month but the cold
room.

The heating circulation pump is zero if the wood heat module's gravity
layout is built, and the winter total falls to 8.63 kWh a day.

### 3.2 The sun

| Quantity | Calculation | Our example |
|---|---|---|
| Array | 11 × 550 W | 6.05 kWp |
| December, a kWp a day | 0.65–0.74 × 0.86 | 0.56–0.64 kWh |
| December, the array a day | × 6.05 kWp | 3.4–3.9 kWh |
| A year, the array | 6.05 × 1,000–1,180 | 6,050–7,140 kWh |

**The December sun.** The building-climate standard gives the month's
sunlight on a south-facing vertical surface at three Carpathian oblast
centres as 20 to 23 kWh a m², and on a horizontal one as 14 to 17,
under average cloud (ДСТУ-Н Б В.1.1-27:2010, Table 8, converted from
MJ; read from a scanned copy and checked against an official one
before it is relied on). An array tilted at 60° receives a little more
than the vertical, so the vertical is taken as its floor. That is
about half the paper's 1.0 kWh a kWp a day. The stations are in the
lowlands and foothills; a mountain horizon takes more.

**A year.** The paper's 1,000 to 1,100 kWh a kWp, and about 1,178
full-load hours for the mountain climate of the Carpathians, the
lowest in Ukraine (Winkler and colleagues, Energy Conversion and
Management: X 28, 2025). From March to October the array covers both
circuits with a wide margin, as the paper holds; the summer surplus
has no use here but the garden pump.

**Not more panels.** Doubling the array to chase December would still
leave a deficit in the dark weeks and waste most of the summer; the
battery and the generator are cheaper per December kWh. A ridge that
takes the sun at two in the afternoon costs more than two panels.

**Tilt and snow.** About 60°, as the paper has it: near the winter
optimum for 48° north, about 61° (Landau, 2017); snow barely holds on
an array that steep (Andrews, Pollard, and Pearce, Solar Energy 92,
2013). The array's lower edge stands clear of the ground's snow: where
shed snow piled up against it, an array lost 29 to 34 percent of its
year, against 5 to 12 percent where it fell clear (Heidari and
colleagues, IEEE Journal of Photovoltaics 5, 2015). The clearance is
[set] from the depth of snow at the site.

### 3.3 The battery

| Quantity | Calculation | Our example |
|---|---|---|
| Four days, essential | 4 × 3.86 kWh | 15.4 kWh, before fans |
| Modules, 5.12 kWh, usable | 4 × 5.12 × 0.90 | 18.4 kWh |
| Days, essential alone | 18.4 ÷ 3.86 | 4.8, before fans |
| Days, both circuits | 18.4 ÷ 9.33 | 2.0 |
| Fans the four days allow | (4.6 − 3.86) ÷ 0.024 | about 31 W in all |

Three modules, as in the paper, give 13.8 kWh usable, 3.6 days of the
essential circuit at 34 people; the four-day rule needs four. The six
fans together may draw about 31 W before a fifth module is needed:
about 5 W each.

**In the cold.** The 48 V LiFePO4 modules sold in Ukraine charge only
between 0 and 50 to 55 °C, and discharge down to −10 or −20 °C (Deye
SE-G5.1 Pro-B datasheet V2.1; Pylontech US5000 manual V1.0, 2024;
Dyness BX51100). Charging below zero plates lithium in the cells:
graphite and LiFePO4 cells cycled at −18 °C lasted 185 equivalent
cycles to 80 percent of their capacity, against about 2,000 at room
temperature (Rauhala and colleagues, Journal of Energy Storage, 2018).
The battery management of the Deye module stops charging below 0 °C.
So the battery lives in an insulated room that stays above freezing,
not in the shelter and not in an unheated outbuilding; where the room
cannot be held above zero, modules with their own heating are chosen,
[set].

### 3.4 The darkest month and the generator

| Quantity | Calculation | Our example |
|---|---|---|
| Deficit, both circuits | 9.33 − 3.4 to 3.9 kWh | 5.5–6.0 kWh a day |
| Deficit, essential alone | 3.86 − 3.4 to 3.9 kWh | 0 to 0.5 kWh a day |
| Charge an hour, 5 kW set | the paper's figure | about 3 kWh |
| Running, a day | 5.5–6.0 ÷ 3 | about 1.8–2.0 h |
| Fuel, a day | 1.8–2.0 h × 1.0–1.5 L | about 1.8–3.0 L |
| Days the fire rules' 40 L allows | 40 ÷ 1.8–3.0 | about 13–22 |

In the darkest month the sun covers the essential circuit, or nearly
so, and the battery carries the dark spells; the generator serves the
general circuit. That is the paper's rule, kept: nothing critical
waits on fuel. The fuel the generator burns in the darkest month is
about twice the paper's, because the sun is about half. The fire rules
limit what may be stored at a site to 40 L (Section 10), so fuel is
bought through the winter; how much is held at any time is not
published.

**The generator.** A 5 kW-class inverter generator, petrol, run
deliberately to top the battery and held as a reserve for a long
failure. A set of this class burns about 1.0 L an hour at half load
and 1.5 L at three-quarters (Sakura SG6500i-A, manufacturer's figures).
Petrol begins to age within about a month without a stabiliser (Honda,
owner's manual); the store is turned over, and stabilised.

### 3.5 The inverter

A 5 kW hybrid inverter at 48 V, as the paper has it, so that a
workshop tool or a washing machine starting does not trip the site; the
paper's peak of about 3 kW at 25 people is [set] at 34 from the
appliance list, and the garden pump's starting current is checked
against the inverter before the pump is chosen. Whether the inverter
is grid-tied or off-grid follows the grid question in Section 10. The
rack takes a fifth and sixth module without rewiring.

* * *

## 4. Bill of materials

Quantities for the example. Alternatives are named in the design; none
is yet known to work here.

| Item | Quantity | Alternatives in the design |
|---|---|---|
| PV module, 550 W | 11 | other sizes to 6 kWp |
| Mounting, 60°, lower edge clear of snow | 1 set | roof frame |
| DC cabling, breakers, surge protection | 1 set | none named |
| Hybrid inverter, 5 kW, 48 V | 1 | off-grid inverter |
| LiFePO4 module, 5.12 kWh, 48 V | 4 | self-heating modules |
| Rack, BMS cabling, fusing | 1 set | none named |
| Distribution board, two circuits | 1 | none named |
| The shelter's own supply | 1 set | none named |
| Earthing and lightning protection | 1 set | none named |
| Monitoring and metering | 1 set | none named |
| Inverter generator, 5 kW class, petrol | 1 | LPG or dual fuel |
| Changeover or transfer switch | 1 | automatic transfer switch |
| Fuel cans, spill tray, stabiliser | 1 set | none named |

**The array, as designed.** South-facing, at about 60°, on a roof or on
poorer ground; out of the December shade; its lower edge clear of the
depth of snow; reachable for brushing off after a heavy fall. On the
ground it is fenced; on a roof the structure is checked for snow and
wind by a builder before it is fixed.

**The battery room, as designed.** Insulated, above 0 °C whenever the
battery charges, dry, ventilated as the datasheet asks, locked, and
reachable for the electrician; not in the shelter, not in an unheated
outbuilding, and never warmed by an electric heater on the battery's
own charge.

**The shelter's own supply.** The shelter keeps a small supply of its
own — a battery charged from the essential circuit, with light,
ventilation, and a point to charge phones — so that it works if the
main system fails at the moment it is needed. It is sized from the
shelter's own loads and the hours the shelter must hold; neither is
published.

**The generator and its fuel, as the rules ask.** The generator stands
outdoors, on level ground of non-combustible material, never inside a
building, on a roof, on a balcony, or on an evacuation route, with its
exhaust clear of doors and windows. Its fuel and oil are kept apart
from it, in containers made for them, in a separate outbuilding at the
distance the rules set, locked. It is wired to the building only
through a changeover or transfer switch that cuts the building off
from any grid. None of these is placed in any published plan.

**The layout, as designed.** Array, inverter and battery, distribution
board, then the essential circuit and the general circuit, each on its
own breakers; the shelter's supply charged from the essential circuit;
the generator through its switch to the inverter. Drawn as
relationships only.

* * *

## 5. Build

| Step | Trade | Time | If done out of order |
|---|---|---|---|
| Appliances chosen, loads listed | household | [from L2] | mis-sized |
| Electrician chosen | household | [from L2] | no certificate |
| Walk: horizon, ground, room | household | [from L2] | array shaded |
| Enquiries answered | household | [from L2] | [from L2] |
| Battery room readied | builder | [from L2] | cells charged cold |
| Earthing, lightning protection | electrician | [from L2] | [from L2] |
| Mounting and array | electrician | [from L2] | [from L2] |
| Inverter, battery, board | electrician | [from L2] | [from L2] |
| Two circuits wired | electrician | [from L2] | one circuit for all |
| Shelter supply | electrician | [from L2] | [from L2] |
| Generator, switch, fuel store | electrician | [from L2] | backfeed |
| Measurements and certificate | electrician | [from L2] | no record |

* * *

## 6. Cost

Estimates, not quotations: every line is the energy paper's own
estimate for autumn 2026, marked "paper", scaled where the design
changed. Re-pricing from dated listings was tried on 2026-10-03 and
could not be done: the retail sites refused automated reading. Place:
not a quotation; the paper's anchors are national. Exchange rate:
exchange_rate, 52 UAH to the euro, the National Bank's mid-September
2026 rate, rounded.

The paper's anchors: a 550 W module at about 8,800 UAH; a single-phase
5 kW hybrid inverter at about 43,000 to 51,000 UAH, budget units from
about 30,000; a 5.12 kWh LiFePO4 module at about 33,000 to 42,000 UAH.

### 6.1 Generation

| Item | UAH | EUR | Basis |
|---|---|---|---|
| PV modules, 11 × 550 W | 96,800 | 1,862 | paper |
| Mounting frames | 25,000 | 481 | paper |
| DC cabling, breakers, surge protection | 20,000 | 385 | paper |
| Subtotal | 141,800 | 2,727 | |

The mounting is the paper's; raising the array's lower edge clear of
the snow may add to it, [set].

### 6.2 Storage and conversion

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Hybrid inverter, 5 kW, 48 V | 48,000 | 923 | paper |
| LiFePO4, 4 × 5.12 kWh | 144,000 | 2,769 | paper, scaled |
| Rack, BMS cabling, fusing | 8,000 | 154 | paper |
| Subtotal | 200,000 | 3,846 | |

The battery is the paper's 108,000 UAH for three modules, 36,000 each,
for four.

### 6.3 Distribution and protection

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Distribution board, with the shelter's supply | 25,000 | 481 | paper |
| Earthing and lightning protection | 15,000 | 288 | paper |
| Installation, wiring, commissioning | 40,000 | 769 | paper |
| Monitoring and metering | 5,000 | 96 | paper |
| Subtotal | 85,000 | 1,635 | |

### 6.4 Generator

| Item | UAH | EUR | Basis |
|---|---|---|---|
| Inverter generator, 5 kW class | 45,000 | 865 | paper |
| Changeover or transfer switch | 9,000 | 173 | paper |
| Fuel cans, spill tray | 5,000 | 96 | paper |
| Subtotal | 59,000 | 1,135 | |

The separate outbuilding for the fuel, and any canopy over the
generator that the enquiry allows, are not priced, [set].

### 6.5 Summary

| Section | UAH | EUR |
|---|---|---|
| Generation | 141,800 | 2,727 |
| Storage and conversion | 200,000 | 3,846 |
| Distribution and protection | 85,000 | 1,635 |
| Generator | 59,000 | 1,135 |
| Construction subtotal | 485,800 | 9,342 |
| Design and electrician's check, 8 percent | 38,900 | 748 |
| Contingency, 20 percent | 104,900 | 2,017 |
| **Total external cost** | **629,600** | **12,108** |

Against the paper's 583,000 UAH, the difference is the fourth battery
module. The percentages are the paper's own, with the contingency
taken on the subtotal and the design together, as the paper does.

**Contribution, not in the total.** None. The labour is in the cost,
paid.

**Running cost.**

- Generator fuel and service: the paper's 6,000 UAH a year was costed
  at about half the darkest month's duty found here, [set] from a dated
  fuel price and the first winter's log.
- Inverter: replaced at ten to fifteen years, about 50,000 UAH, paper.
- Battery: fifteen years at this cycling, then about 144,000 UAH at
  today's estimate, paper, scaled.
- Panels: forty years, with a slow decline in output, paper.
- Insulation and protection measured every two years, under the fire
  rules (Section 10), [set] from a quotation.

* * *

## 7. Operation and maintenance

Responsible: one named adult, paid, with a deputy, and the electrician
for everything behind the board — [from L2].

- **Daily:** the battery's state read at the monitor and written down;
  in the darkest weeks, the general circuit shed when the battery falls
  to the level the household sets, [set].
- **After a heavy snowfall:** the array brushed clear from the ground,
  never by climbing on it.
- **Monthly:** the generator started and run under load; the fuel's
  date checked and the store turned over.
- **Seasonal:** before winter, the battery room's lowest temperature
  read; the array's shade checked against the December horizon.
- **Every two years:** insulation and protection measured by the
  electrician, and the record filed where inspections will ask for it.

How the programme relates to this work is described in the programme
modules, in standing format.

* * *

## 8. Failure modes

From the design, not from experience.

| Failure | Early sign | Repair and cost |
|---|---|---|
| Battery charged below 0 °C | capacity falls | warm room; [from L2] |
| Dark spell over four days | battery low | shed general; generator |
| Snow on the array | output near zero | brush clear from ground |
| Snow piled at the lower edge | array never clears | raise the array |
| Fuel aged | hard start | fresh fuel, stabiliser |
| Generator back-fed into the grid | — | switch fitted first |
| Fan load above 31 W | battery days fall | fifth module |
| Inverter tripped at a start | site goes dark | stagger the loads |

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
copies — LIGA:ZAKON, a university copy of the fire rules without their
later amendments, and the State Energy Supervision Inspectorate's own
pages — because the statute site could not be reached; each is read on
zakon.rada.gov.ua and signed before this row counts as checked.

- **Fire Safety Rules of Ukraine, Order No. 1417 of the Ministry of
  Internal Affairs, 30.12.2014,** amended last by Order No. 67 of
  27.01.2026. Section IV, chapter 1, point 1.20: insulation resistance
  and short-circuit protection measured at least every two years,
  unless the technical operating rules set another interval. Section
  III, chapter 2, points 2.14 and 2.18: no store of flammable or
  combustible liquids in residential, public, or administrative
  buildings.
- **Order No. 474 of the Ministry of Internal Affairs, 11.07.2024,** in
  force 14.08.2024, adding to the fire rules a chapter on generators of
  up to 20 kW with a tank of up to 100 L: outdoors, on level ground of
  non-combustible material; never in a building, on a roof, a balcony,
  or an evacuation route; fuel and oil of at most 40 L and 10 kg, in a
  separate outbuilding at least 7 m from buildings; no generator
  plugged into a socket. Order No. 67, 27.01.2026, in force 27.02.2026,
  adds rules for groups of generators.
- **Rules for the Technical Operation of Consumers' Electrical
  Installations, Order No. 258 of the Ministry of Fuel and Energy,
  25.07.2006:** for a private owner of an installation up to 1 kV, they
  apply only to measuring the wiring's insulation; results are kept in
  protocols. The intervals sit in СОУ-Н ЕЕ 20.302:2007, not read.
- **Fire Safety Rules for the Education System, Order No. 974 of the
  Ministry of Education and Science, 15.08.2016,** Section V, points 9
  and 11: measurements as the general fire rules ask; hand torches on
  batteries for every member of the night duty where people stay round
  the clock. Whether the site falls under these rules depends on its
  legal form.
- **Law No. 2019-VIII, on the electricity market,** amended last by Law
  No. 4963-IX of 02.09.2026, and **Law No. 3220-IX of 30.06.2023:** an
  active consumer may produce, store, and sell surplus; self-generation
  is open to household solar of up to 30 kW and small non-household
  consumers of up to 50 kW. No duty was found to register an
  installation with no grid connection at all.
- **The Distribution System Code, NEURC Resolution No. 310 of
  14.03.2018,** amended last by No. 1355 of 11.08.2026: governs the
  connection of a consumer's generation; not read.
- **The State Energy Supervision Inspectorate,** guidance of 2023 and
  2024: a generator reaches the building's wiring only through a
  changeover or automatic transfer switch after the meter and the main
  breaker, so that the building is cut off from the grid, and the
  connection is made by a specialist. The State Emergency Service's
  guidance of 2025 and 2026, as reported, keeps a generator at least 6
  m from doors and windows and asks for a carbon monoxide detector in
  living rooms.
- **Not reached:** the Rules for the Arrangement of Electrical
  Installations, 2017; ДСТУ HD 60364-6; the standard for lightning
  protection; the standard for emergency lighting.

**One correction to the paper.** The paper expects an annual electrical
inspection of an establishment that receives children. No instrument
found asks for one; the fire rules ask every two years. The enquiry
asks.

The written enquiries: to the regional emergency service, the
generator's place, the fuel store, and the interval of measurements
for this establishment; to the distribution operator, if a grid
connection exists, the inverter, the changeover, and whether any
notice is due; to the electrician, which standards the certificate
will be signed against.

* * *

## 11. Adaptation notes

The design is a seed, not a copy: a different place grows a different
form from it.

- **A sunnier valley:** the December figure rises, the generator runs
  less; keep the four days.
- **A darker valley, or a deep horizon:** the generator runs more, or
  a stream carries the winter; never more panels first.
- **A colder valley:** the battery room is the hard part; self-heating
  modules, or the battery inside the heated envelope.
- **A smaller group:** recalculate Section 3.1; the battery keeps four
  days of the essential circuit.
- **A larger group:** above about 31 W of fans, or more essential load,
  a fifth module before more panels.
- **A reliable grid:** the battery may shrink to the outages the grid
  has; the essential circuit and its four days stay for an
  establishment that receives children.
- **A stream:** the micro-hydro module.

* * *

## 12. Provenance and licence

- **Written by:** Michel Garand. [set — others as they choose to be
  named]
- **From whose knowledge:** the energy working paper, EN v0.1;
  ДСТУ-Н Б В.1.1-27:2010; Winkler and colleagues, 2025; PVGIS 5;
  Landau, 2017; Andrews, Pollard, and Pearce, 2013; Heidari and
  colleagues, 2015; the Deye, Pylontech, and Dyness datasheets; Rauhala
  and colleagues, 2018; Sakura and Honda manufacturer data; the fire
  rules and the other instruments in Section 10, as read on secondary
  copies.
- **Traditional knowledge:** none. How the valley met the dark months
  is for the elders.
- **Text:** CC BY-SA 4.0
- **Drawings and designs:** [hardware licence — open decision]
- **Measurement data:** none yet
- **Gate 1:** household decision, 2026-10-03, recorded by Michel Garand —
  v0.1 may be published as it stands, at L1, in English, Ukrainian, and
  German
- **Wartime review:** 2026-10-03, Michel Garand — v0.1 read against
  compendium Section 2; nothing places the site; the shelter, the safety
  link, the battery, the generator, and the fuel store in standing format;
  accepted

* * *

## 13. What to check

- **The appliance list** — every load in Section 3.1, replacing the
  scaled lines.
- **The safety link** — its average draw, measured over a week.
- **The fans** — their power, against the 31 W the battery allows.
- **The December sun** — the standard's Table 8 read in an official
  copy; the site's December horizon walked.
- **The grid** — whether a connection exists, and the Distribution
  System Code read for it.
- **The battery room** — its lowest temperature in the coldest week;
  whether self-heating modules are needed.
- **The snow** — its depth at the site, which sets the array's
  clearance.
- **The enquiries** — the generator's place, the fuel store, the
  interval of measurements.
- **Quotations** — every line in Section 6, dated, to replace the
  paper's estimates; a dated fuel price for the running cost.
- **The Ukrainian row** — every instrument read and signed.
- **From L2, once built:** build times and out-of-order consequences in
  Section 5; the maintenance record in Section 7; early signs and repair
  costs in Section 8; Section 9.

* * *

© 2026 Michel Garand | Carpathian OER Commons | CC BY-SA 4.0
stewardship@ubec.network
