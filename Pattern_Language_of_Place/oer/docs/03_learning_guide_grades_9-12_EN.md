# Erdpuls Learning Guide 03 — Grades 9–12
## Place as Laboratory: Research Methods for the Living World
### For Students Ages 15–18 | Upper Secondary

**Institution:** Erdpuls Müllrose - Center for Sustainability Literacy, Citizen Science and Reciprocal Economics  
**Location:** Müllrose, Brandenburg, Germany

**Version:** 1.1  
**Date:** February 2026  
**Status:** Draft v1.1 — OER Publication Ready (EN)  
**Translation Status:** 🇩🇪 DE — *pending Phase 3* | 🇵🇱 PL — *pending Phase 3*

---

## Changelog
| Version | Date          | Changes                                      |
|---------|---------------|----------------------------------------------|
| 1.1     | February 2026 | Initial generation for OER publication; institution name and license applied |
| 1.0     | —             | Not released                                 |

---

## Overview Table

| Element | Detail |
|---|---|
| **Target Group** | School classes, Grades 9–12, ages 15–18; advanced Gymnasium / Oberschule |
| **Session Length** | 3.5–5 hours (half-day to full-day) |
| **Group Size** | 10–25 students; works well with smaller specialized groups (Projekttage, Facharbeiten) |
| **Setting** | Full Erdpuls campus including Rings 0–4; sensor lab; GIS workstation; makerspace |
| **Season** | All seasons; winter creates unique and underexplored datasets |
| **Core Method** | Full phenomenological protocol; independent sensor operation; open data contribution; research question design |
| **Toolkit Links** | Full Appendix A (13 Questions + data analysis); Appendix B (full token economy including UBECrc design); Appendix C (bioregion mapping with GIS); Appendix D (BNE Quality Framework) |
| **Developmental Stage** | Third seven-year period emergence: awakening individual judgment, capacity for systemic and ethical reasoning, the question "Who am I in the world and what do I owe it?" |
| **Citizen Science Output** | Complete dataset entered into Erdpuls longitudinal record; iNaturalist species uploads; openSenseMap data contribution; optional: independent research question with follow-up protocol |
| **Token Economy Level** | Advanced — full UBECrc engagement; optional: design exercise for an alternative token economy applied to a problem the student identifies |
| **Languages Available** | EN ✓ &nbsp;&nbsp; DE pending &nbsp;&nbsp; PL pending |

---

## Five Competency Clusters at This Level

| Competency Cluster | Expression for Ages 15–18 |
|---|---|
| **Environmental Literacy** | Full landscape systems literacy: soil, hydrology, land use history, biodiversity, bioregional thinking; connecting local observation to global environmental datasets; reading landscape as a record of human decisions |
| **Scientific Inquiry** | Independent research question design from own data; multi-variable analysis; distinguishing between correlation and causation; data ethics and open science principles |
| **Technology Competence** | Independent senseBox MCU deployment and configuration; openSenseMap station management; basic QGIS orientation; understanding the sensor network as distributed environmental intelligence |
| **Economic Understanding** | Full four-element UBECrc token economy; critical analysis of what conventional economics fails to measure; optional design exercise: apply token principles to a real problem |
| **Social-Emotional Learning** | The Action stage of the 4A-Pathway: what does knowing this require of me? Systemic thinking about personal agency; the question of intergenerational responsibility |

---

## Pedagogical Rationale

### The Developmental Stage

Students in Grades 9–12 are entering the third developmental phase: the emergence of **individual judgment**. This is the age at which abstract thinking is fully available, but — and this is pedagogically crucial — it is most powerfully activated when it is grounded in concrete experience. A student who has knelt in soil, measured its temperature, counted its organisms, and formulated a question from their own data is in a completely different epistemic position from a student who has only encountered soil ecology as text on a page.

The research-level session at Erdpuls is designed for this exact developmental moment. It does not *simplify* environmental science for young people. It offers the genuine article: a real place, real instruments, real open datasets, and real unanswered questions. The student's role is not to receive pre-packaged knowledge but to generate new knowledge — knowledge that did not exist before they arrived.

This is also the age at which the question *"What do I owe the world?"* becomes personal rather than abstract. The 4A-Pathway completes its arc at the Action stage: not "do something nice for the environment" but "this is what I found; this is what it means; this is what I am going to do." The token economy at this level invites students not just to earn tokens but to design systems — to think about how value flows in the communities they inhabit and what would change if different things were recognized and rewarded.

### Why Open Data and Not Just Field Data

Every dataset that Erdpuls generates enters a permanent open record. Every student who contributes to that record is practicing **open science** — the principle that knowledge generated with public resources (including the intellectual resources of a school education) should be freely available to all. When an Erdpuls student uploads a soil temperature reading to openSenseMap, that reading becomes available to researchers, policymakers, students in other countries, and future generations investigating climate change at this specific location.

This is not theoretical. The Erdpuls longitudinal soil dataset accumulates meaning over time: a single day's reading is one data point; a decade of readings at the same coordinates becomes a climate record. Students at this level are not just learning environmental science — they are actively contributing to it.

---

## Preparation and Materials

### Facilitator Preparation (72 Hours Before)

- Read full Appendix A, C, and D in the Pattern Discovery Toolkit Appendices
- Prepare 5–6 diverse observation patches across the full ring structure (campus interior through near landscape)
- Update the QGIS project with current data layers (see Appendix C.4 for layer list)
- Charge and configure senseBox MCU units (1 per team of 3–4 students if available; minimum 1 shared)
- Export openSenseMap historical data for the campus station(s) for comparison display
- Prepare the **Research Question Design Sheet** (A4, blank template with prompts: *Observation / Pattern / Question / What data would answer this? / What methods would collect that data?*)
- Print full Field Sheets (A4, double-sided; extended version with data analysis prompts)
- If GIS session is included: set up QGIS workstation with Brandenburg datasets pre-loaded (see Appendix C.4)

### Materials List

**Per team (3–4 students):**
- Full Field Sheets (extended version)
- Pencils and pens
- Hand lens (10× minimum; 20× preferred)
- Observation frame (30×30 cm, pre-placed at diverse locations)
- White tray + collection tools
- Water dropper + measuring cup (100 ml)
- pH strips + distilled water
- Soil thermometer
- Measuring tape (for transect distances if Appendix C work included)
- GPS device or phone GPS app (for coordinate recording)
- Camera or phone for species photography (iNaturalist upload)
- Research Question Design Sheet

**Shared/facilitator equipment:**
- senseBox MCU with full sensor suite (temperature, humidity, UV, particle matter if available)
- Tablet/laptop for dashboard and openSenseMap
- QGIS workstation (if mapping session included)
- Token cards (all four elements) + token ledger

---

## Session Structure

This guide offers three modular tracks that can be run independently or combined for a full-day program.

---

### Track A — The Full Research Protocol (3.5 hours)

#### Opening — From Curiosity to Question (20 minutes)

Students do not receive a worksheet at the start. They receive one instruction only:

*"Spend five minutes in the garden — anywhere. Touch something, smell something, look at something carefully. Come back with one thing that surprised you, confused you, or that you don't know the explanation for."*

Students disperse. Return after five minutes. Each shares their observation. The facilitator writes every response on a visible surface. No evaluation — only reception.

*"These are your starting points. Everything we do today should move us toward understanding one or more of these observations better. Not all the way — better. That's science."*

#### Phase 1 — Full Soil Protocol (60 minutes)

Students run the complete 13-Question protocol independently in teams. The facilitator circulates but does not instruct — only asks: *"What do you think explains that?" / "Have you measured it yet?" / "What would change your interpretation?"*

All 13 Questions are completed. Crucially, Questions 11–12 (History and Relationships) receive full written treatment: students construct an evidence-based narrative of their patch's history and draw a spatial relationship diagram placing their patch in its landscape context.

**Question 13 (Action)** at this level becomes: *"If you were responsible for this landscape — not just this patch, but the kilometer of landscape around this campus — what policy, practice, or intervention would you propose? What evidence from today's observation supports it?"*

#### Phase 2 — Sensor Dialogue and Data Analysis (30 minutes)

Students operate the senseBox independently (with initial facilitator demonstration of first 2 minutes maximum). They record all sensor readings on their Field Sheet alongside body-sensing readings.

Full data comparison across teams on the Comparative Data Board. At this level, the analysis goes further: students identify **the single most interesting cross-variable correlation in the dataset** and propose a causal mechanism. These proposals are presented briefly: *"Team 3 noticed that the three patches with the lowest life count also had the highest infiltration times. We think this is because..."*

Discussion of the limits of a single-session dataset: *"What would you need to rule out your alternative explanation? What additional data would you collect? Over what time period?"* This is the core scientific thinking exercise: distinguishing between what the data supports and what it merely suggests.

#### Phase 3 — Research Question Design (30 minutes)

Each student (individually) completes the Research Question Design Sheet:

1. **Observation:** What specific thing did you observe today that you didn't expect, or that you can't fully explain?
2. **Pattern:** Is this observation part of a pattern — something that might appear elsewhere, or that might repeat over time?
3. **Question:** State your research question as precisely as possible. Not "Why is the soil different?" but "What is the relationship between soil compaction (measured by water infiltration time) and surface biodiversity (measured by Life Count) across different microclimates within a 500m radius of the Erdpuls campus?"
4. **Data required:** What measurements would answer your question?
5. **Method:** How would you collect them? With what instruments? Over what time period?

These sheets are collected by the facilitator and added to the Erdpuls research question register. Questions that can be addressed with subsequent visits or the continuous sensor data stream are flagged for follow-up.

#### Closing — Action and Open Science (20 minutes)

**Citizen Science commitment:**

Each student selects one action from the following:
- Upload their team's species observations to iNaturalist (completing accounts if needed)
- Write a brief annotation to the Erdpuls open dataset (context for their day's readings)
- Commit to one observable action at home or in their school informed by what they found today

**Token Economy Reflection:**

Rather than earning individual tokens for specific activities, upper secondary students engage in a brief **system design exercise**: *"Your town has decided to introduce a system that makes visible and rewards non-monetary contributions to the local community — care work, ecological action, knowledge sharing, cooperative labor. Design the four elements of your system. What would Cooperation, Reciprocity, Mutualism, and Regeneration look like in your specific community? What would they reward that currently goes unrecognized?"*

Groups share designs. Facilitator draws connections to the UBECrc system and the broader literature on complementary currencies, care economies, and commons governance.

---

### Track B — GIS and Bioregion Mapping (2 hours, standalone or following Track A)

This track adapts Appendix C (Bioregion Mapping) for upper secondary students with a GIS literacy component.

#### Phase 1 — Walking Transect (60 minutes)

Teams take a walking transect from the Erdpuls campus outward along a chosen bearing, recording at 200-meter intervals:
- GPS coordinates
- Soil type (by texture)
- Dominant vegetation
- Land use
- Any visible transition or boundary
- Sensory Closure data (which senses are active? which have faded?)

This is Ring 2–3 field work: moving from campus through settlement and near landscape, noting where the character of the place changes.

#### Phase 2 — GIS Exploration (45 minutes)

At the QGIS workstation, teams overlay their transect data with pre-loaded layers:
- Hydrology (watershed boundaries, Schlaube catchment)
- Geology (glacial deposits, sand vs. clay transitions)
- Land cover (forest, agricultural, urban)
- Historical maps (Prussian Urmesstischblätter, 1850s)
- Their own GPS transect

Key questions: *"Where does your felt sense of 'leaving Müllrose' coincide with a geological or hydrological boundary? Where does it not? What does the historical map show that the current map doesn't? What has changed, and what has remained constant?"*

#### Phase 3 — Bioregional Boundary Proposal (15 minutes)

Each team proposes a bioregional boundary for the Naturpark Schlaubetal sub-region as they experienced it — where does this place begin and end, based on what they observed? The boundary is drawn on the map (digitally or on a large print) with an annotated rationale.

*"The official nature park boundary is an administrative line. Your boundary is based on what your senses told you as you walked. They don't have to agree — in fact, the places where they disagree are the most interesting."*

---

### Track C — Quality Framework Reflection (1 hour, standalone)

This track adapts Appendix D (BNE Quality Framework) for upper secondary — particularly useful for students studying education, social science, or planning Facharbeiten on sustainability topics.

Students receive the abbreviated version of the Brandenburg BNE Quality Catalog (7 evaluation areas). They evaluate the Erdpuls session they just completed against these criteria: *"According to the official quality standards for sustainability education — did what you just experienced meet those standards? Exceed them? Fall short anywhere?"*

This exercise produces two outcomes:
1. Students engage critically with institutional quality frameworks (meta-cognitive learning)
2. Erdpuls receives genuine evaluation data from the most rigorous evaluators available: students who have direct experience of the session and the ability to apply an external framework

Student evaluations are collected and added to the Erdpuls quality evidence record (BNE Area 5.2.2).

---

## Curriculum Alignment (Brandenburg)

| Subject | Curriculum Element | Erdpuls Track Connection |
|---|---|---|
| Biology (Oberstufe) | Ecosystem analysis, biodiversity, soil science | Track A: full protocol + data analysis |
| Geografie (Oberstufe) | Landscape systems, land use change, climate | Track A + B: sensor data + GIS transect |
| Chemie (Gr. 9–10) | pH, chemical properties of soil | Track A: measurement round |
| Informatik | IoT systems, open data, data ethics | Track A: senseBox + openSenseMap |
| Wirtschaft/Soziales | Alternative economics, commons theory | Track A: UBECrc design exercise |
| Ethik/Philosophie | Environmental ethics, intergenerational responsibility | Track A: Q13 + Action stage |
| Projekttage / Facharbeit | Independent research design | Research Question Design Sheet → potential Facharbeit topic |

---

## Facilitator Notes

**The critical facilitation principle for this age group:** Maximum independence, minimum instruction. Upper secondary students who are over-facilitated produce surface-level responses. Those given genuine open time, genuine instruments, and genuine open questions produce remarkable work. The facilitator's primary role is to resist the impulse to explain, and instead to ask: *"What do you think?"* and wait.

**On the Research Question Design Sheet:** Some students will produce genuinely original research questions that the Erdpuls program cannot answer from existing data. These should be recorded and, where possible, initiated: a follow-up sensor deployment, a return visit, or a connection to a university research group. The student who generates a question worth investigating has done something more valuable than the student who correctly answers a question already known.

**On UBECrc:** Do not oversell the blockchain dimension. Students at this age are often skeptical of blockchain claims (appropriately so). The token economy's value is in the economic philosophy it expresses — the four elements — not in the technical implementation. The blockchain is simply the transparency mechanism. The design exercise is more valuable than a lecture on distributed ledger technology.

---

## Risk and Safety

- Upper secondary students are generally capable of unsupervised outdoor work within defined parameters; trust them with this
- Brief on soil safety (wash hands; no eating during soil phases)
- GPS device protocol for transect work: pairs minimum, agreed return point, phone charged
- GIS workstation: student data should be saved to a designated folder, not system-wide

---

## License & Attribution

© 2025–2026 Erdpuls Müllrose - Center for Sustainability Literacy, Citizen Science and Reciprocal Economics  
Licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)

All software components referenced in this document are licensed under the  
[GNU Affero General Public License v3.0 (AGPL-3.0)](https://www.gnu.org/licenses/agpl-3.0.html)

*This project uses the services of Claude and Anthropic PBC to inform our decisions and recommendations. This document and its translations were developed with assistance from Claude (Anthropic PBC). All strategic decisions, philosophical positions, and project commitments are those of the author.*
