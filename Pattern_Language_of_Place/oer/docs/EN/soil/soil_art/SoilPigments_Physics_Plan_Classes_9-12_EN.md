---
title: "Soil Colour as Physics — Detailed Lesson Plan: Classes 9–12"
subtitle: "Earth Pigments from the Soils of Müllrose"
author: "Michel Garand"
date: "February 2026"
version: "1.0"
lang: en
license: "CC BY-NC-SA 4.0"
project: "Erdpuls Müllrose OER Collection"
---

# Soil Colour as Physics — Detailed Lesson Plan: Classes 9–12

## Earth Pigments from the Soils of Müllrose

**Erdpuls Müllrose — Living Laboratory & Makerspace Garden**

*Part of the "Brücken bauen durch Boden — 13 Questions to the Soil" project*

* * *

## Overview

| | |
|---|---|
| **Target group** | Classes 9–12 (ages 14–18) |
| **Number of units** | 7 × 45 minutes |
| **Total time** | 315 minutes (~5.25 hours) |
| **Location** | Unit 1 outdoors / farm sites; Units 2–5 in Erdpuls Zone B; Unit 6 Zone B + Zone C (IoT sensor dashboard); Unit 7 presentation space |
| **4A focus** | Full pathway; Attitude and Action as the primary cognitive challenge |
| **Cognitive mode** | Hypothetical-deductive: independent research design, quantitative analysis, scientific communication |
| **Core question** | *"What does the colour of a soil tell us — and can we measure it well enough to find out?"* |
| **Key methods** | Quantitative spectroscopy (Spectroid / smartphone), CIELAB colour space, Δ*E* values, grain size distribution, senseBox sensor correlation |
| **Safety** | FFP2 masks and goggles required during dry grinding and sieving |
| **Output** | Correlation dataset; research poster or report; pigment contribution to WP4 colour library |

* * *

## Teacher Notes for This Grade Band

Students at this level are capable of genuine research. The most powerful thing you can do in this unit is to hand them a real, open question — not a pre-determined outcome to confirm — and give them the tools and time to investigate it.

The central project thesis (*"A farmer's inner attitude toward the soil is reflected in measurable soil quality"*) is deliberately not provable by any single experiment. This is a feature, not a flaw. Students who investigate honestly will find evidence that is suggestive but not conclusive. That is the reality of scientific inquiry in complex systems. Learning to sit with provisional findings and express appropriate uncertainty is a research competency at least as important as the physics content itself.

**Full physics concepts introduced at this level:**
- Mie scattering (qualitative and semi-quantitative: particle size and wavelength interaction)
- Ligand field theory (d-orbital splitting in Fe³⁺ as the cause of iron oxide colour)
- CIELAB colour space (L*, a*, b* coordinates; Δ*E* as a metric for colour difference)
- Spectroscopy: reflection spectra, absorption maxima, identification against RRUFF database
- Colloid physics: colloidal suspension stability, film formation mechanisms
- IoT data integration: correlating senseBox moisture/temperature data with spectral measurements

**Senior thesis potential:** The Unit 7 research presentation can be extended into a formal *Facharbeit* or pre-scientific paper for students in Classes 11–12. The question *"What does iron oxide mineralogy tell us about past soil management and future soil quality under different regimes?"* is genuinely viable as a research question at this level.

**Cross-curricular connections:** Physics (optics, spectroscopy), Chemistry (coordination chemistry, crystal chemistry), Biology (soil ecology, decomposition, humus formation), Earth Science (pedogenesis, mineralogy), Mathematics (statistics, regression, matrix algebra for colour space transformation), Research methods (hypothesis design, experimental protocol, scientific writing).

* * *

## Theoretical Background for the Teacher (Summary)

### Why Iron Oxides Are Coloured — Ligand Field Theory

Iron in soil exists primarily as Fe³⁺ (ferric iron). The Fe³⁺ ion has five unpaired d-electrons. When surrounded by oxygen ligands (as in all iron oxide minerals), these d-electrons are split into two energy levels by the ligand field. Light with the right energy can excite an electron from the lower to the higher level — this removes that wavelength from the reflected spectrum.

The precise energy of the splitting depends on the geometry and spacing of the oxygen ligands — which varies between goethite, haematite, lepidocrocite, and ferrihydrite. This is why each iron oxide mineral has a characteristic colour:
- Goethite (octahedral Fe³⁺ with OH ligands): absorbs violet-blue -> yellow
- Haematite (corundum structure, edge-sharing octahedra): absorbs blue-green -> red
- Lepidocrocite (different layer structure): absorbs blue -> orange

### CIELAB Colour Space

CIELAB is an international standard for measuring colour independently of the observer or device. Three coordinates:
- **L*** : lightness (0 = black, 100 = white)
- **a*** : red-green axis (positive = red, negative = green)
- **b*** : yellow-blue axis (positive = yellow, negative = blue)

**Δ*E*** (Delta E) is the Euclidean distance between two colours in CIELAB space:
$$\Delta E = \sqrt{(\Delta L^*)^2 + (\Delta a^*)^2 + (\Delta b^*)^2}$$

A Δ*E* < 1 is imperceptible to the human eye. A Δ*E* of 2–3 is just noticeable. A Δ*E* > 5 is clearly different. Students can use this to quantify colour differences between farm soils, between grinding time fractions, and between wet and dry states.

### Mie Scattering and Particle Size

Mie scattering theory (Gustav Mie, 1908) describes how light interacts with spherical particles of size comparable to the wavelength of light (~400–700 nm for visible light). The key relationships for this unit:
- Particles much larger than the wavelength: diffuse (geometric) scattering — bright, whitish appearance.
- Particles comparable in size to the wavelength (roughly 0.1–10 μm): strong Mie scattering — high covering power, rich colour.
- Particles much smaller than the wavelength (below ~100 nm): Rayleigh scattering — semi-transparent, blue tint.

This is why optimal pigment particle size (5–50 μm) falls in the Mie range — strong scattering at all visible wavelengths, combined with the specific absorption of the iron oxide.

* * *

## Unit 1 — Fieldwork: Systematic Sampling and Goethean Observation

**Duration:** 45 minutes (recommended as 90 minutes with farm visit)
**Location:** Partner farm sites
**4A-Pathway stage:** Awareness
**Materials needed:** Sample bags (200–500 g each), site description form, Munsell Soil Color Chart, pH strips, EC meter (if available), spade, camera, GPS, senseBox sensor location map

### Learning Objectives

By the end of this unit, students will be able to:
- Design and implement a systematic sampling protocol across three farming systems
- Record quantitative site parameters (colour by Munsell, pH, texture, depth)
- Practice Goethean observation: sustained attention to the phenomenon before any explanation is attempted
- Identify the GPS locations for sensor cross-correlation in Unit 6

### Unit Plan

**Opening (7 min):**
Before arriving at the first site, introduce the Goethean observation protocol: *"We will spend three minutes at each site doing nothing but looking and noticing — no labels, no explanations, no Instagram. Just describe what you observe."* This practice — slowing down before categorising — is a formal research approach developed by Goethe and still used in plant science and ecology.

Introduce the project thesis: *"The project proposes that a farmer's inner relationship with the land shows up in measurable properties of the soil. By the end of this unit, we will have formed our own initial hypothesis about this."*

**Direct Experience (8 min per site × 3 sites = 24 min):**
At each farm site:
1. Silent observation period (3 min): What colour? What smell? What texture visible from the surface? What organisms visible?
2. Profile exposure (spade, 30 cm): photograph with scale bar.
3. Systematic data collection per student pair:
   - Munsell colour wet and dry at three depths (0–5 cm, 10–15 cm, 25–30 cm)
   - pH at each depth
   - Texture by finger test and recorded estimation
   - GPS coordinates
   - Proximity to senseBox sensor location (note distance)

**Synthesis (10 min):**
At the end of the field session, students compare their initial observations from all three sites. Each student writes a one-paragraph hypothesis: *"I predict that the soil from [farm name] will show [colour characteristic] in the spectroscopy data because…"*

Hypotheses are collected (ungraded) — they will be returned in Unit 6 for students to evaluate against their own findings.

**Closing (4 min):**
Samples labelled and secured. Preview: *"In the lab we will characterise these samples physically and measure their colour objectively — then compare the measurements to your hypothesis."*

* * *

## Unit 2 — Laboratory Processing: Precision Grain Size Analysis

**Duration:** 45 minutes
**Location:** Erdpuls Zone B
**4A-Pathway stage:** Acknowledgment
**Materials needed:** Dried soil samples, oven (50°C, 24 h pre-dried by teacher if time is tight), sieves (500/250/100/63 μm), precision balance (1 mg), mortar and pestle, dishes, FFP2 masks, safety goggles, lab book

### Learning Objectives

By the end of this unit, students will be able to:
- Conduct a precise sieve analysis and calculate grain size distribution as percentage fractions
- Plot a cumulative grain size distribution curve
- Connect grain size distribution to soil texture and to pigment potential
- Operate the dust safety protocol and explain its scientific rationale

### Unit Plan

**Opening (8 min):**
Review the safety protocol — masks and goggles on before any dry processing begins. Then: *"A sieve analysis does not just give us particle sizes — it gives us the starting point for understanding how this soil will behave as a pigment. Let us find out what fraction of each sample is potentially useful for paint."*

**Investigation (30 min):**
Working in pairs, one sample per pair:

1. Weigh total sample (record as M_total).
2. Stack sieves: 500 μm (top) -> 250 μm -> 100 μm -> 63 μm -> receiver dish (bottom).
3. Grind sample for 10 minutes in mortar. FFP2 masks on throughout.
4. Pour ground sample into top sieve. Shake for 5 minutes (mechanical or hand).
5. Weigh each fraction. Record.
6. Calculate percentage retained on each sieve:
   % = (mass of fraction / M_total) × 100
7. Plot cumulative distribution: x-axis = sieve aperture, y-axis = % passing.

Compare curves across the three farm samples: which farm produces the finest fraction? Which the coarsest?

**Synthesis (5 min):**
*"Which farm's soil has the highest proportion of material in the 63–250 μm range — the optimal pigment range we discussed? Does this match your field observation of colour intensity?"*

Introduce the concept: beyond grain size distribution, the *shape* of the cumulative curve tells us about the soil's formation history. A steep, narrow curve suggests a well-sorted sand (like a beach or dune). A flat, spread curve suggests a mixed-origin soil with many grain sizes (like a loamy agricultural field). What do our curves say about Müllrose's glacial geology?

**Closing (2 min):**
Lab book: cumulative grain size distribution curves for all three farm samples. Note the d₅₀ value (median grain size) for each.

* * *

## Unit 3 — Reflection Spectroscopy: Measuring Colour Objectively

**Duration:** 45 minutes
**Location:** Erdpuls Zone B
**4A-Pathway stage:** Acknowledgment
**Materials needed:** Ground pigment samples (from Unit 2), smartphones with Spectroid app (or DIY spectrometer from DVD diffraction grating and cardboard), white reference paper, GIMP on laptop for RGB->CIELAB conversion, RRUFF Project database (online), watercolour paper for sample patches

### Learning Objectives

By the end of this unit, students will be able to:
- Record a reflection spectrum using a smartphone spectrometer
- Identify the absorption maximum of a pigment from the spectrum
- Calculate or estimate the L*, a*, b* CIELAB coordinates from RGB values
- Compute Δ*E* between two pigment samples
- Compare the spectrum of a Müllrose sample with a reference mineral spectrum from the RRUFF database

### Unit Plan

**Opening (8 min):**
Introduce the concept of the reflection spectrum: *"Your eye perceives colour by integrating the reflected spectrum across three types of photoreceptors (cones). A spectrometer does the same thing mathematically but measures each wavelength separately. The spectrum contains more information than colour — it tells us which minerals are present."*

Demonstrate the Spectroid setup: cardboard shield to block ambient light, white paper for reference measurement (white reference = 100% reflectance baseline), pigment patch on white paper for sample measurement.

**Investigation (30 min):**

Part 1 — Spectral acquisition (15 min):
Each pair records reflection spectra of:
- A sample from each of the three farms (same grinding time/fraction for comparability)
- A wet version and a dry version of one sample
- A raw vs. 30-minute-ground version of one sample

Note the wavelength of the absorption maximum (where reflected light is lowest = most absorbed).

Part 2 — CIELAB conversion and Δ*E* (10 min):
Photograph each pigment patch with a calibrated phone camera. Import into GIMP. Read RGB values (Color -> Color Balance tool, or use the Color Picker). Convert RGB to CIELAB using the GIMP Color Picker report, or manually using the standard transformation matrix (teacher provides the conversion table or spreadsheet).

Calculate Δ*E* between:
- Farm A vs. Farm B
- Farm A vs. Farm C
- Farm B vs. Farm C
- Wet vs. dry (same sample)

Part 3 — RRUFF comparison (5 min):
Open rruff.info. Search for "goethite" and "haematite." Compare the reference spectra with the Müllrose sample spectra. Which mineral does the absorption maximum suggest is dominant in each farm's soil?

**Synthesis (5 min):**
Class comparison of Δ*E* values. Key question: *"Is the colour difference between the three farms scientifically significant? (Δ*E* > 3 is perceptible to the trained eye.) Does the spectral data support or challenge your Unit 1 hypothesis?"*

**Closing (2 min):**
Lab book: spectra plotted or photographed, Δ*E* values recorded, RRUFF comparison noted.

* * *

## Unit 4 — Binder Physics: Colloidal Suspension and Film Formation

**Duration:** 45 minutes
**Location:** Erdpuls Zone B
**4A-Pathway stage:** Acknowledgment -> Attitude
**Materials needed:** Ground pigment, five binders (water, linseed oil, gum arabic solution, egg yolk, casein), watercolour paper, brushes, balance, timer, GIMP or colour app for Δ*E* measurement on drying; optional: polarising filters for refractive index demonstration

### Learning Objectives

By the end of this unit, students will be able to:
- Describe paint as a colloidal suspension and explain what "colloidal" means
- Explain the film formation mechanism of at least two binders (oxidative polymerisation vs. solvent evaporation)
- Measure Δ*E* between wet and dry states for each binder
- Correlate binder refractive index with colour shift magnitude

### Unit Plan

**Opening (7 min):**
Introduce colloid physics: *"A colloid is a mixture where small particles are distributed throughout another substance — but not dissolved. Milk is a colloid (fat droplets in water). Fog is a colloid (water droplets in air). Paint is a colloid: pigment particles suspended in binder."*

What makes a colloid stable? The particles must be small enough not to settle out immediately, and they must carry enough surface charge (or be coated with a stabilising molecule) to repel each other. In paint, the binder molecules adsorb onto the pigment surface and prevent clumping.

**Investigation (28 min):**
Students prepare the five-binder comparison from the Classes 5–8 unit, but with an additional quantitative layer: measuring Δ*E* for the wet-to-dry transition for each binder.

For each binder:
1. Mix pigment to a consistent paste (use the balance: 1 g pigment + binder quantity per standard recipe).
2. Apply 1 cm × 5 cm stripe to watercolour paper. Photograph immediately.
3. Photograph again after 10 min, 20 min, 30 min, and once fully dry.
4. Read RGB values from each photograph. Convert to CIELAB. Calculate Δ*E* (wet -> dry).

Also note:
- Visual crack formation (crack width in mm if visible)
- Water resistance (droplet test after 24 h)
- Adhesion (tape peel test after 48 h — report back next session)

Discussion during work: *"Why does linseed oil actually gain mass as it dries? (Oxygen crosslinks the fatty acid chains.) Why does egg tempera dry faster than watercolour? (The protein in the yolk coagulates, setting the film quickly.)"*

**Synthesis (8 min):**
Compare Δ*E* values for the wet-dry transition across the five binders. Plot as a bar chart.
Key question: *"Which binder shows the smallest Δ*E* (least lightening)? What does the refractive index of the binder have to do with it?"*

Theory: the colour-shift on drying is approximately proportional to the difference in refractive index between the binder and air. Linseed oil has a relatively high refractive index (n ≈ 1.48); water n ≈ 1.33; air n = 1.0. A higher-index binder resists the light-scattering increase on replacement by air -> less lightening.

**Closing (2 min):**
Lab book: Δ*E* table and bar chart. One-paragraph recommendation: which binder for the WP4 exhibition paintings and why.

* * *

## Unit 5 — Pigment Production: From Data to Material

**Duration:** 45 minutes
**Location:** Erdpuls Zone B
**4A-Pathway stage:** Action
**Materials needed:** Final ground pigment from best fraction, chosen binder (class decision from Unit 4), glass jars (50 ml), precision balance, labels, watercolour paper for final artwork, brushes, colour library archive form

### Learning Objectives

By the end of this unit, students will be able to:
- Produce a quantity of exhibition-grade pigment using the optimal parameters identified in Units 2–4
- Document the production with full provenance data (site, farm, depth, grinding parameters, binder ratio)
- Relate the scientific findings to the artistic output within the WP4 context

### Unit Plan

**Opening (5 min):**
Review the optimal grinding parameters identified in Unit 2–3 (optimal sieve fraction for colour intensity). Confirm the binder recommendation from Unit 4. Set the task: *"Today we move from experiments to production. We are making the actual pigments for the exhibition."*

**Making (30 min):**

Production sequence per student or pair:
1. Weigh out 5–10 g of the 63–250 μm fraction of the strongest-coloured farm sample.
2. Grind to the determined optimal time (from Unit 3 data).
3. Mix with binder to the standard recipe ratios determined in Unit 4.
4. Fill glass jar. Seal.
5. Label: **[Mineral dominant / Munsell code] / [Farm name] / [Depth] / [Grinding time] / [Binder] / [Date] / [Class] / [Student name]**
6. Photograph jar on white background.
7. Complete colour library archive form.

If time allows: make a final painting using all three farm pigments on watercolour paper, with the intention of showing the three colours in dialogue with each other.

**Synthesis (7 min):**
Display all jars. Look at the collection as a whole.
*"We started with a question: does farming method affect soil colour? What does your data say? What does the jar collection in front of you say?"*

Allow a genuine discussion — contradictory results are welcome. The thesis is a hypothesis. The science is not finished.

**Closing (3 min):**
Lab book: record the final production parameters. Note the quantity and CIELAB coordinates of your pigment. Hand in the labelled jar for inclusion in the Müllrose Earth Colour Library.

* * *

## Unit 6 — Correlation Study: Sensor Data Meets Spectroscopy

**Duration:** 45 minutes
**Location:** Erdpuls Zone C (IoT sensor dashboard) + Zone B
**4A-Pathway stage:** Attitude
**Materials needed:** senseBox sensor data download (teacher or Erdpuls team prepares prior to session), spectral data from Unit 3, spreadsheet software (LibreOffice Calc or Python), graph paper or computer for plotting, statistical correlation formula reference sheet

### Learning Objectives

By the end of this unit, students will be able to:
- Download and interpret senseBox sensor data (soil moisture, temperature)
- Plot the relationship between soil moisture at the time of sampling and CIELAB L* value
- Calculate a Pearson correlation coefficient between sensor data and spectral measurements
- Interpret the result in the context of the project thesis

### Unit Plan

**Opening (8 min):**
Introduce the IoT connection: *"The senseBox sensors at each farm have been recording soil moisture and surface temperature continuously. We have our spectral measurements of the same soils. Now we can ask: do the sensor readings correlate with our colour measurements?"*

The underlying physics: soil moisture affects colour (L*, lightness, decreases with moisture) through the Mie scattering mechanism we studied. Temperature affects soil chemistry over time — warm, wet conditions favour haematite formation; cool, wet conditions favour goethite. If the senseBox data from the three farms differs systematically, the colour data should too.

**Investigation (30 min):**

Part 1 — Download and inspect sensor data (10 min):
Using the senseBox interface or a pre-downloaded CSV, display the moisture and temperature data from the three farms over the sampling period. Identify the time point of each soil sample collection. Note the sensor reading at that time.

Part 2 — Plot the correlation (10 min):
For each of the samples in the dataset (at minimum, one per farm per depth = 9 data points):
- x-axis: senseBox moisture reading at time of sampling (%)
- y-axis: CIELAB L* value from Unit 3

Plot as a scatter diagram. Fit a trend line (by eye or using spreadsheet).

Part 3 — Pearson correlation coefficient (10 min):
Using the formula provided (or a spreadsheet function), calculate r (Pearson's r) for the moisture-L* relationship.
Interpret: r close to -1 means strong negative correlation (wetter -> darker, as expected). r close to 0 means no correlation. r close to +1 means wetter -> lighter (unexpected, but possible for some soil types).

Discuss: *"Is our result statistically meaningful with only 9 data points? What would we need to increase the confidence of this finding?"*

**Synthesis (5 min):**
Return to the hypotheses written in Unit 1. How well did each student's prediction match the data? Ask students to write one sentence modifying or confirming their original hypothesis.

Introduce the concept of provisional science: *"In real research, 9 data points is a pilot study, not a conclusion. What we have done is identify whether a larger study is worth doing. That is a real and valuable scientific output."*

**Closing (2 min):**
Lab book: scatter diagram, r value, revised hypothesis statement.

* * *

## Unit 7 — Research Communication: Presenting Findings

**Duration:** 45 minutes
**Location:** Presentation space or classroom
**4A-Pathway stage:** Action
**Materials needed:** Lab books, pigment jars, final paintings, poster paper or digital presentation tool, all datasets from Units 1–6

### Learning Objectives

By the end of this unit, students will be able to:
- Present a research finding to a non-specialist audience clearly and accurately
- Structure a scientific argument: question -> method -> data -> interpretation -> conclusion
- Distinguish between what the data shows and what it suggests
- Identify the limitations of their investigation and propose future directions

### Unit Plan

**Opening (5 min):**
Set the context: *"You have conducted a real investigation. Now you will communicate it — as a researcher would, at a conference or in a paper. Your audience today is [partner farmers / other class / teachers / exhibition visitors]. They have not done this work with you. Your task is to tell them what you found — and what you think it means."*

**Preparation (15 min):**
In groups of 2–3, students prepare a 5-minute presentation or a research poster. Structure required:
1. **Question** — What did we ask?
2. **Method** — How did we investigate it? (briefly)
3. **Findings** — What did the data show? (specific values, graphs)
4. **Interpretation** — What do we think this means for the project thesis?
5. **Limitations** — What could be better or larger in a follow-up study?
6. **Open question** — What does your work not yet answer?

**Presentations (20 min):**
Each group presents (5 min each, 3–4 groups depending on class size). Encourage the audience to ask one genuine question after each presentation.

**Synthesis (5 min):**
Full class debrief:
- *"Which finding surprised you most across all the groups?"*
- *"Where did the data support the project thesis? Where did it challenge it?"*
- *"If you had one more semester to continue this research, what would you investigate?"*

Optional: invite a partner farmer to this session. Hearing their soil described in terms of CIELAB coordinates and Pearson correlations — and then comparing it to the actual colour on the paper — is a powerful closing moment for both students and farmers.

**Closing (5 min):**
Final journal entry (written in silence): *"One thing I now know that I did not know before. One question that this work has opened that I did not have before. One thing I want to do with what I have learned."*

* * *

## Senior Thesis Extension (Classes 11–12)

For students wishing to extend the work into a *Facharbeit* or pre-scientific thesis, the following research question is viable:

*"Is there a measurable correlation between farming management method and iron oxide mineralogy in the partner farm soils of Müllrose, as indicated by reflection spectroscopy and CIELAB colour analysis?"*

Suggested extension activities:
- Seasonal re-sampling (September deepening experiment) to build a larger dataset
- Comparison of Müllrose spectra with reference spectra from the RRUFF database for mineral identification
- Integration of SoilGrids global data for regional comparison
- Formal statistical analysis (ANOVA across farm groups, multiple regression with moisture, temperature, and management as predictors)
- Written report following scientific paper structure: Abstract, Introduction, Methods, Results, Discussion, Conclusion

The Erdpuls project team is available as a research support partner for students pursuing this track.

* * *

## Assessment for Classes 9–12

### Lab Book / Research Journal

The lab book documents the complete investigative arc from Unit 1 hypothesis through Unit 7 presentation. It should contain all data tables, graphs, spectra, and written analyses from each unit.

### Assessment Criteria

| Criterion | Indicator |
|---|---|
| Research question | Specific, testable, and connected to the project thesis |
| Experimental design | Variables identified; controls in place; fair test achieved |
| Data quality | Precise measurements; appropriate significant figures; complete tables |
| Analysis | Calculations correct; graphs appropriately labelled and interpreted |
| Interpretation | Distinguishes between what data shows and what it might suggest |
| Scientific communication | Clear structure; appropriate vocabulary; accessible to non-specialist |
| Epistemic humility | Limitations acknowledged; provisional conclusions stated with appropriate uncertainty |

### Exit Question (written)

*"Your spectral data shows a Δ*E* of 4.7 between the soil from Farm A (conventional) and Farm B (biodynamic). What does this value mean physically? What would you need to confirm that this difference is due to farming method rather than other variables?"*

A strong answer will: define Δ*E* correctly, note that 4.7 is clearly perceptible, identify confounding variables (depth, moisture at time of sampling, parent rock composition, seasonal variation), and propose a controlled study design to address them.

* * *

## Materials Summary for Classes 9–12

| Unit | Key materials |
|---|---|
| 1 | Sample bags, site description forms, Munsell chart, pH strips, EC meter, spade, camera, GPS |
| 2 | Soil samples, sieves, precision balance, mortar, FFP2 masks, goggles, lab book |
| 3 | Ground pigment, smartphones with Spectroid, GIMP on laptop, RRUFF access (online), watercolour paper |
| 4 | Ground pigment, 5 binders, balance, timer, GIMP, watercolour paper, polarising filters (optional) |
| 5 | Final pigment, chosen binder, glass jars, labels, archive form, watercolour paper |
| 6 | senseBox data (CSV), spectral data from Unit 3, spreadsheet software, graph paper |
| 7 | Lab books, pigment jars, final paintings, poster paper or digital presentation tool |

**FFP2 masks and safety goggles required in Units 2 and 3 during dry grinding and sieving.**

* * *

## Further Reading (for teachers)

- Toland, A., Noller, J.S. & Wessolek, G. (Eds.) (2019): *Field to Palette — Dialogues on Soil and Art in the Anthropocene.* CRC Press. 681 pp. [Essential background for Unit 7; the structure of artistic-scientific dialogue in the book mirrors the poster/presentation format students produce. Wessolek is Emeritus at TU Berlin — a natural contact for advanced student projects]
- Feller, C., Landa, E.R., Toland, A. & Wessolek, G. (2015): Case studies of soil in art. *SOIL* 1: 543–559. DOI: 10.5194/soil-1-543-2015 [Open access; students in the Facharbeit extension can cite this as a peer-reviewed precedent for the methodology of Unit 6. Free download]
- Wessolek, G. (2021): Böden in Kunst und Gesellschaft neu positionieren. *Handbuch der Bodenkunde.* Wiley. DOI: 10.1002/9783527678495.hbbk2021001 [In German; useful theoretical framework for the Facharbeit thesis on soil science and society]
- Schwertmann, U. & Cornell, R.M. (2000): *Iron Oxides in the Laboratory.* Wiley-VCH. [Foundational for Units 3 and 6; covers RRUFF-comparable iron oxide spectra]
- Blume, H.-P. et al. (2018): *Scheffer/Schachtschabel: Lehrbuch der Bodenkunde.* 17th ed. Springer Spektrum. [Full soil science background for Units 1–2]
- AG Boden / BGR (2024): *Bodenkundliche Kartieranleitung* (KA6). 6th ed. E. Schweizerbart, Stuttgart. [Students writing a Facharbeit may cite this for field sampling methodology]
- Doerner, M. / Hoppe, T. (2011): *Malmaterial und seine Verwendung im Bilde.* 24th ed. Maier, Ravensburg. [Colloidal physics of binders for Unit 4. In German]

* * *

## License and Attribution

© 2025–2026 Michel Garand | Erdpuls Müllrose — Center for Sustainability Literacy, Citizen Science & Reciprocal Economics
Müllrose, Brandenburg, Germany

Licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

You are free to share and adapt this material for non-commercial purposes, provided you give appropriate credit, provide a link to the license, indicate if changes were made, and distribute any adaptations under the same license.

All software components referenced in this document are licensed under the [GNU Affero General Public License v3.0 (AGPL-3.0)](https://www.gnu.org/licenses/agpl-3.0.html)

*This document and its translations were developed with assistance from Claude (Anthropic PBC). All strategic decisions, philosophical positions, and project commitments are those of the author.*

**Contact:** erdpuls@ubec.network · [https://erdpuls.ubec.network](https://erdpuls.ubec.network)

*Alle Dokumente und ihre Übersetzungen / All documents and their translations.*
*Müllrose, Brandenburg — February 2026*
