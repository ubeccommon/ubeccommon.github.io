---
title: "Carpathian OER Commons — Pathway to the Complete Guide"
subtitle: "How the Complete Guide Gets Built, and How It Travels"
author: "Michel Garand"
date: "2026-09-27"
version: "v0.4"
lang: "en"
license: "CC BY-SA 4.0"
project: "Carpathian OER Commons"
status: "released 2026-09-27 as a working draft — open to co-creation"
---

*Working paper of the Carpathian OER Commons, published as a working draft
and open to co-creation. The project's child-protection rules apply in
full: no child is named, dated, counted, or placed; the site is not named.
Section 11 sets the rules that govern everything this pathway would
publish.*

*Published 2026-09-27, beside the foundations paper. For publication,
references to other writing about the place were made general, and the
project's internal terms made plain; the content is unchanged.*

*This paper sits above the technical guides rather than beside them. It
says what the complete guide consists of, how each part reaches the
standard at which it can be published, and how it travels to other valleys
— in Ukraine and across the borders the mountains do not recognise.*

*v0.4, 2026-09-27: the settlement group, the adult strand, and the
pattern layer added from the open hamlet working paper,
concept_open_hamlet_EN_v0_1.md. The map grows from thirty-four modules
to forty.*

* * *

## 1. What is being built

Two things are being built at once, and confusing them wastes both.

The first is a place: buildings, water, power, sanitation, a forest, a
programme. It exists to serve the children who come and the household that
hosts them, and it would be worth doing if no one ever copied it.

The second is a description of the place, accurate enough that people
fifty or five hundred kilometres away can build their own version without
repeating the expensive mistakes. That description is the guide.

The guide is not a by-product of the first thing. It is its own work, with
its own standard, its own labour, and its own cost — and if it is treated
as something to write up afterwards, it will not be written. What follows
is the pathway to producing it deliberately.

The place is also becoming a settlement. The forest school serves adults
too — retreat and continuing education — and around it a small hamlet is
planned: households living there, with work, learning, and land held
together. The hamlet is part of the place, and its description is part
of the guide: the place's own pattern language, discovered and not
imposed, and the modules that implement it. The reasoning is in the
open hamlet working paper.

**A model, not a template.** Other initiatives in the Carpathians —
Ukrainian, Romanian, Polish, Slovak, Hungarian — work in different
regulations, currencies, soils, and histories. What travels is the method,
the sizing, the order of decisions, and the record of what failed. What
does not travel is the answer. A guide that pretends otherwise is an
export, and this work is not for export; it is with.

* * *

## 2. What is taken from Open Source Ecology, and what is not

Open Source Ecology, founded by Marcin Jakubowski, set out to publish open
blueprints for the fifty industrial machines it takes to run a small
civilisation — the Global Village Construction Set — built and tested on
its own farm, designed to be modular, repairable, and made locally at a
fraction of commercial cost. Four of its habits are worth taking whole.

- **Documentation is the deliverable.** A thing built and not documented
  has not been finished. OSE treats a demonstrated, replicable production
  model as the completion metric, not a working prototype.
- **Modularity.** Independent parts that interoperate, so that a reader
  takes the two modules they need without swallowing the whole.
- **Lifetime design and serviceability.** Built to be repaired by the
  people who use it, with the documentation that makes repair possible.
- **Replication is the measure of success.** Not how good the original is,
  but how quickly others can build and improve on it.

Four things are not taken.

- **The machines.** This is not a fabrication project. The technologies
  here are a cistern, a reed bed, a wood stove, a battery, a nursery —
  mostly older than industry and mostly built by local trades.
- **The completeness claim.** No set of fifty anything. The guide covers
  what this site actually does, and says plainly where it stops.
- **The rhetoric.** No post-scarcity, no new economy, no
  civilisation-building language. The register here is a household in a
  war, describing what it built and what it cost.
- **Open by default, everywhere.** A hardware project can publish
  everything. This one cannot: children, a wartime location, and knowledge
  that is not ours to license all set limits. Section 11.

* * *

## 3. The unit: the module

Everything in the guide is a module with the same shape, so that a reader
who has read one can navigate any other, and so that translation and
revision stay tractable.

**Every module carries:**

- **Purpose** — what problem it solves, in two sentences, and one line
  of connections: what the module depends on and what it feeds.
- **Context of validity** — the conditions under which the design holds:
  climate, altitude, group size, season of use. The most important
  section, and the one usually missing from published projects.
- **Sizing method** — the arithmetic, with the input a reader must measure
  themselves, not our result.
- **Bill of materials** — quantities, with substitutions that are known to
  work.
- **Build** — sequence, trades needed, time, what happens if it is done in
  the wrong order.
- **Cost** — with currency, month, and place of the quotation. A cost
  without a date is a rumour.
- **Operation and maintenance** — daily, seasonal, annual; who is
  responsible.
- **Failure modes** — what breaks, what it looks like when it is going
  wrong, what it costs to fix.
- **What we got wrong** — the section that makes the guide worth reading.
- **Regulatory notes** — by country, as a table, each entry dated and
  attributed to whoever checked it.
- **Adaptation notes** — what a reader must change for a drier valley, a
  colder one, a smaller group.
- **Provenance and licence** — who wrote it, from whose knowledge, under
  what terms.
- **What to check** — every figure marked [set] or [assumed], and how it
  will be replaced.

Figures that more than one module sizes from — capacity, litres per
person, the exchange rate — are declared once, in a site parameters file
in standards/, and cited by name. A change there is carried through
every module that cites it in the same commit.

The three technical guides already drafted — water, energy, sanitation —
feed eleven rows of the component map between them, not three. The map's
source column shows which. Converting them is the first task of the
pathway, not a later tidy-up.

**Patterns.** Under its Connections line every module carries a pattern
line: what it grows from and feeds among the place's own patterns, once
their cards exist; which of Alexander's patterns it resonates with, as
prompts and never as specification; and what it is in tension with.
Three kinds of pattern are kept apart — the place's, named by the
household, the co-creators, and the elders; Alexander's, used as
prompts; and a module's own design rules, which stay inside the module.

* * *

## 4. Maturity: what may be claimed

Every module carries a level, stated at the top. Readers act on the level,
not on the confidence of the prose.

| Level | Meaning | May publish |
|---|---|---|
| L0 | Idea, discussed | nothing |
| L1 | Designed and costed, basis per line | design, marked untested |
| L2 | Built here | build record, real cost |
| L3 | Measured through a full season | performance numbers |
| L4 | Built by someone else, elsewhere | their figures beside ours |
| L5 | Improved by others, merged back | the improved version |

Whether a cost is quoted, estimated, or assumed is a label on each cost
line, not a level. A module at L1 may be costed entirely from estimates,
and says so line by line.

The three existing guides sit at L1. Nothing in them should be read as
tested, and the modules must say so on their face. The temptation the
pathway has to resist is publishing L1 work in L3 language.

* * *

## 5. The component map

Source says where existing material lies: W, E, S for the water, energy,
and sanitation guides with their section numbers; P for the programme
proposal, published beside the foundations paper; 7a for the project's
child-protection rules, held in its working knowledge; I for the
infrastructure proposal, not yet located.

### 5.1 Ground and safety

| Module | Status | Source |
|---|---|---|
| Shelter: standard, siting, certification | L0 | E 9, W 2 |
| Warning, communications, evacuation | L0 | — |
| Fire protection and night lighting | L0 | — |
| Medical room and quiet room | L0 | — |

### 5.2 Utilities

| Module | Status | Source |
|---|---|---|
| Water: spring, cistern, treatment | L1 | W 1–5, 8–9 |
| Rainwater and nursery irrigation | L1 | W 6, 8.5 |
| Energy: PV, storage, generator | L1 | E 1–4, 6–7, 9 |
| Micro-hydro, if the stream allows | L0 | E 5, 7.6 |
| Sanitation: terra preta toilets | L1 | S 1–3, 8.1, 9–10 |
| Greywater, reed bed, pond | L1 | S 6–7, 8.5–8.6 |
| Wood heat and hot water | L0 | E 8, S 8.7 |

### 5.3 Buildings

| Module | Status | Source |
|---|---|---|
| Sleeping accommodation, winter-capable | L0 | — |
| Kitchen and dining to institutional standard | L0 | — |
| Washroom block | L1 | S 8.7–8.8 |
| Covered gathering place and hearth | L0 | — |
| Workshop and tool store | L0 | — |
| Insulation and mountain building practice | L0 | — |

### 5.4 Land, forest, food

| Module | Status | Source |
|---|---|---|
| Tree nursery: beds, shade, watering | L1 | I |
| Biochar: kiln, quality, storage | L1 | S 2, 8.2 |
| Terra preta: fermentation to soil | L1 | S 4–5, 8.3 |
| Planting, succession, the mountain calendar | L0 | P 4.2 |
| Compost and site nutrient cycle | L1 | S 5, 8.4 |
| Kitchen garden and food storage | L0 | — |

### 5.5 Programme

| Module | Status | Source |
|---|---|---|
| Pedagogy: the pathway and its stages | L1 | P 3, 5 |
| Rhythm: the day, the session, the year | L1 | P 4, 5 |
| Pattern cards and the record | L1 | P 3.1 |
| Elders' strand and its consent practice | L1 | P 4.4 |
| Safeguarding: the two tiers and the gates | L2 | 7a, P 6 |
| Mentor preparation | L0 | — |
| Adult strand: retreat and continuing education | L0 | — |

### 5.6 Organisation

| Module | Status | Source |
|---|---|---|
| Legal form and ownership | L0 | — |
| Budgeting: capital and running | L1 | W 8, E 7, S 8, I |
| Funder fit and application practice | L1 | P, I |
| Cross-border partnership | L0 | — |
| Documentation toolchain and standards | L2 | standards/ |

### 5.7 Settlement

| Module | Status | Source |
|---|---|---|
| Settlement form and siting, schematic | L0 | — |
| Dwellings for resident households | L0 | — |
| Paths, gateway, and access | L0 | — |
| Common land and shared work | L0 | — |
| Membership and self-governance | L0 | — |

Self-governance is designed threefold: those who teach decide pedagogy;
all members decide the standing rules, each with one voice; the
associations of those who produce and use decide the economy.
Safeguarding sits in the rights sphere, beyond the reach of the other
two.

Forty modules. Two at a level where the site's own experience backs
them, sixteen at design stage, twenty-two untouched. Naming the empty
rows is more useful than filling them with prose.

Across all seven groups runs a pattern layer — the place's own patterns,
discovered, not imposed — carried in the pattern record and in each
module's pattern line. It is a second way of reading the map, not a
group in it.

Two L0 rows already have costed material in the guides — micro-hydro and
wood heat — held at L0 because each waits on a measurement or a choice
not yet made: the stream's head and flow, and the buildings the heat
serves.

* * *

## 6. The pathway, in five phases

**Phase 0 — Standards and repository.** Fix the module template, the file
naming, the versioning, the units and currency conventions, the image
rules, and where the repository lives. Convert the three existing guides
to module shape. Nothing is published yet. Weeks, not months, and it is
the phase most often skipped.

**Phase 1 — Document what exists.** Before any new building: measure and
write up what the site already has. The spring's yield. The existing flush
toilets and where they discharge. The buildings, their construction, their
heat loss. This is the baseline every later figure is read against, and it
can only be captured once.

**Phase 2 — Build and measure.** Each module moves L1 to L2 as it is
built, with the build recorded as it happens — dated photographs, real
invoices, the day the mason said the wall needed to be thicker. Then a
full season of measurement before any performance claim: water in the dry
month, battery through December, the reed bed under snow.

**Phase 3 — Publish.** English settles first; the Ukrainian sibling
follows and is corrected over time rather than held back. Publication is
module by module as each reaches L2, not a single release at the end. A
module that is honest about being L1 can be published early and marked.

**Phase 4 — Invite replication.** One or two sites first, not a launch. A
site that is already building something and needs two of our modules is
worth more than fifty readers. Their figures come back into the module
beside ours, which is what L4 means.

**Phase 5 — Commons governance.** Once other people's work is in the
guide, it needs a way of deciding what gets merged, who holds the
repository, and what happens if the original site stops. Deferred
deliberately — do not build governance for a commons that has one member.

* * *

## 7. Toolchain

The guide is written in the same markdown standard as everything else in
this project, checked by the same script, and stored in a
version-controlled repository — git, hosted somewhere the household can
reach and does not pay for. Other writing about the place stays where it
is; the guide is a separate thing with a separate rhythm, because
testimony and technical documentation age differently.

- **Text:** markdown, ERDPULS standard, one file per module, checker
  before commit.
- **Drawings:** SVG or FreeCAD, source files committed beside the exports.
  A PDF of a drawing is not a drawing.
- **Measurements:** plain CSV, one series per file, with a header stating
  instrument, place at valley resolution, and who took it.
- **Photographs:** metadata stripped, filenames neutral, reviewed against
  Section 11 before they go anywhere near a server.
- **Translation:** English canonical; other languages as siblings with a
  stated revision date, never blocking publication.
- **Releases:** a dated snapshot when a group of modules reaches L2, so
  that a replicating site can cite a fixed version.

* * *

## 8. Licensing, and what cannot be licensed

**Documents:** CC BY-SA 4.0, as everything else in this project. Share,
adapt, attribute, keep it open.

**Designs and drawings:** a hardware-appropriate licence rather than a
document licence — CERN-OHL-S is the usual choice for open hardware that
must stay open. The distinction matters the first time someone builds from
a drawing and improves it.

**Measurement data:** released openly, ideally with no conditions beyond
attribution, since data that comes with restrictions stops being compared.

**Attribution is joint.** The philosophy document already carries two
hands. The technical modules will carry more: the household, the mason,
the electrician, the elders. An open licence that quietly attributes
shared work to one author is a theft dressed as generosity.

**Not ours to license.** Hutsul practice — forms, songs, craft, the
knowledge of a particular valley — is not automatically open because we
wrote it down. Anything of that kind enters the guide only with the
consent of the people whose knowledge it is, on the terms they set, and
some of it will not enter at all. The right default is to describe our own
use of a practice and point to its holders, rather than publish the
practice as if it were ours to give.

* * *

## 9. Across the borders

The Carpathians run through Ukraine, Romania, Poland, Slovakia, Hungary,
Serbia, and Czechia, and a cross-border frame for the range already exists
in the Carpathian Convention. That frame is worth understanding before
inventing a network: it has working groups, funded programmes, and a habit
of cooperation that predates this project. Check its current standing
before citing it in any application.

What travels well across those borders: sizing methods, the order of
decisions, failure modes, the maturity discipline, the safeguarding
architecture.

What does not travel and must be localised by whoever is there: regulation
— sanitary, building, water, child protection, all national; prices and
trades; species and planting calendars; the language of the programme; the
relationship with a local authority, which is always personal.

**Practical consequence for the module template:** the regulatory note is
a table with one row per country, each row dated and signed by whoever
checked it, and empty rows stay visibly empty. A Romanian reader must be
able to see at a glance that nobody has checked Romania.

**Translation policy:** English canonical, Ukrainian close behind. Polish,
Romanian, Slovak, and Hungarian only when a partner in that country takes
on the translation as their own work — a machine-translated Romanian
module with no Romanian reader is worse than none, because it looks
checked.

* * *

## 10. How another site would use this

The replication protocol, written from the reader's side:

1. **Self-assessment.** Group size, season of use, altitude, water source,
   grid, legal status. Half a page, which decides which modules apply.
2. **Measure first.** Each module names what must be measured before it
   can be used. A site that skips the spring measurement and builds our
   cistern has not replicated anything.
3. **Take modules, not the model.** A site that needs only sanitation
   takes sanitation.
   **Walk your own settlement** with Alexander's patterns as prompts,
   and begin your own pattern record, as in Section 4 of the open
   hamlet paper. Your knowledge-holders name your patterns; ours are
   not yours.
4. **Localise the regulation.** Their row in the table, checked by them,
   sent back.
5. **Build, record, return figures.** Real costs in their currency and
   month; what they changed and why.
6. **Twinning, if wanted.** A working relationship between two households
   beats any amount of documentation, and the documentation exists mostly
   to make the first conversation shorter.

A failure log is part of the offer: sites that tried something from the
guide and abandoned it, with the reason. The absence of such a log in most
published projects is why most published projects cannot be trusted.

* * *

## 11. Safeguarding governs everything here

The guide is a published artefact, so the project's child-protection rules
apply to every line of it, and the aggregation test applies across
modules: a drawing in one, a photograph in another, and a date elsewhere
can together place a site that no single document placed.

- **No child in any module.** Not in a photograph, not in a caption, not
  in an example, not in a headcount, not as texture. Programme modules
  describe standing format only.
- **Publish the method, not the place.** Site plans in a published module
  are schematic — relationships only, without distances or the terrain
  that identifies a valley, until the decision on naming the site. The
  site is the hamlet: dispersed homesteads on a slope, drawn with
  distances, place a valley. Construction drawings of a single
  structure keep their dimensions.
- **Photographs** show structures and systems, no faces, no signage, no
  distinctive ridgelines, no metadata.
- **Regulatory and application material** that names an entity travels to
  funders, not to the repository.
- **Pattern cards** stay in the workshop. Only the yearly narrative of
  the place's pattern language is published, at valley resolution.
- **Wartime review before every release**, not once at the start. What was
  safe to publish in one season may not be in the next.
- **Gate 1 throughout.** The household decides what of its own life is
  described, module by module.
- **A line held beyond the rules.** Children, wartime, a named doorstep, a
  fixed week, and family circumstance, in one piece, are never published,
  whatever the rules at the time allow.

The guide is publishable because infrastructure is publishable. The
programme modules are the difficult ones, and the right instinct there is
to publish the architecture of the safeguarding and very little of the
programme's daily life.

**For a replicating site,** which will not see the project's working
rules: Tier 1 — no child named, dated, counted, or placed, ever; Tier 2 —
anything more only through consent gates; Gate 1 — each household decides
what of its own life is described.

* * *

## 12. Who pays for the documentation

Documentation time is real work — roughly a day per module to draft, and
more to check, draw, and translate. It is invisible in most budgets, which
is why most projects do not have documentation.

Three routes, not exclusive:

- **Inside the infrastructure budget.** A documentation line of five to
  eight percent of capital, justified as open educational resources, which
  several funders fund willingly.
- **As its own small grant.** Open knowledge, digital commons, and
  educational resource programmes fund exactly this, and the deliverable
  is unusually easy to verify.
- **In kind.** The household's time, counted as contribution at the same
  rate as toloka labour, so its value appears rather than vanishing.

The guide is not sold and is not a product. If someone wants more than the
guide gives — a person on site, a design for their valley — that is a
separate arrangement and does not close the guide.

* * *

## 13. The metric of completion

Borrowed from OSE and narrowed: **the guide is complete when another site
has built from it, in another valley, and their figures are in it beside
ours.**

Not when every module is written. Not when it is translated into six
languages. Not when it is published. A guide with six modules and one
honest replication is further along than thirty modules read by nobody.

* * *

## 14. The first twelve months

A sequence, not a schedule. Each step assumes the one before.

1. Fix the module template, the repository, and the site parameters.
   Convert the three guides into the eleven rows they feed.
2. Baseline the site: spring yield in the dry month, existing sanitation
   and its outfall, buildings and their condition, the stream if there is
   one. Walk the settlement with Alexander's patterns as prompts, and
   begin the pattern record.
3. Send the written enquiries: establishment category, the spring's
   protection zone, discharge to ground, a fire-fighting reserve, a
   water-use permit for the stream. File each answer against the
   regulatory row of the module it governs.
4. Write the safeguarding module first among the programme modules — it is
   at L2 already and it governs the rest.
5. Publish the utility modules at L1, marked as untested, in English and
   Ukrainian.
6. Build the safety and utility layers; record as built, not after.
7. Measure one full season, including one winter.
8. Move the built modules to L2, then L3 where a season supports it.
9. Find one other site. Not a network, not a launch. One.

* * *

## 15. What has to be decided

- Whether the guide names the site at all, ever — and if so, at what point
  in the war.
- Decided 2026-09-27: the repository. A private workshop on GitHub under
  ubeccommon, publication as a collection in ubeccommon.github.io; every
  clone is a full local copy for when the connection fails.
- Which hardware licence, decided before the first drawing rather than
  after.
- Who the co-authors are, named on each module, and how the elders'
  material is handled.
- Whether documentation is funded inside the infrastructure budget or
  separately.
- Which country a partner might come from first, since that decides the
  second language after Ukrainian.
- Decided 2026-09-27: the programme proposal and the philosophy are
  published as working drafts, in standing format, beside the
  foundations paper.
- Legal form and ownership, before anyone lives on the site. One option
  to weigh, not decided: land held in trust, out of the market.
- Each resident household's own Gate 1, before its life is described.
- How safeguarding supervision extends to retreat guests and residents.
- How much of the adult strand is published.
- Decided 2026-09-27: released modules carry the author's name and the
  initiative's name.
- Decided 2026-09-27: capacity, session length, and use days may be
  published, as standing format and never beside a date.

* * *

## Release record

- **Gate 1:** 2026-09-27, recorded by Michel Garand — published beside the
  foundations paper as a working draft, open to co-creation and to change.
- **Wartime review:** 2026-09-27, Michel Garand — names no place;
  references to other writing about the place made general; accepted.

* * *

© 2026 Michel Garand | Carpathian OER Commons | CC BY-SA 4.0
stewardship@ubec.network
