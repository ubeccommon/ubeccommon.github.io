---
title: "Bodenfarbe als Physik — Detaillierter Unterrichtsplan: Klassen 9–12"
subtitle: "Erdpigmente aus den Böden von Müllrose"
project: "Erdpuls Müllrose OER-Sammlung"
date: "Februar 2026"
lang: de
version: "1.0"
license: "CC BY-NC-SA 4.0"
---

# Bodenfarbe als Physik — Detaillierter Unterrichtsplan: Klassen 9–12

## Erdpigmente aus den Böden von Müllrose

**Erdpuls Müllrose — Living Laboratory & Makerspace Garden**

*Teil des Projekts „Brücken bauen durch Boden — 13 Fragen an den Boden"*

* * *

## Überblick

| | |
|---|---|
| **Zielgruppe** | Klassen 9–12 (Alter 14–18) |
| **Anzahl der Einheiten** | 7 × 45 Minuten |
| **Gesamtdauer** | 315 Minuten (ca. 5,25 Stunden) |
| **Lernorte** | Einheit 1 im Freien / Hofstandorte; Einheiten 2–5 in Erdpuls Zone B; Einheit 6 Zone B + Zone C (IoT-Sensor-Dashboard); Einheit 7 Präsentationsraum |
| **4A-Schwerpunkt** | Vollständiger Weg; Haltung und Handlung als primäre kognitive Herausforderung |
| **Kognitive Ebene** | Hypothetisch-deduktiv: eigenständiges Forschungsdesign, quantitative Analyse, wissenschaftliche Kommunikation |
| **Leitfrage** | *„Was sagt uns die Farbe eines Bodens — und können wir sie gut genug messen, um es herauszufinden?"* |
| **Schlüsselmethoden** | Quantitative Spektroskopie (Spectroid / Smartphone), CIELAB-Farbraum, Δ*E*-Werte, Korngrößenverteilung, senseBox-Sensorkorrelation |
| **Sicherheit** | FFP2-Masken und Schutzbrillen beim Trockenмahlen und Sieben erforderlich |
| **Ertrag** | Korrelationsdatensatz; Forschungsposter oder -bericht; Pigmentbeitrag zur WP4-Farbenbibliothek |

* * *

## Hinweise für Lehrende zu diesem Jahrgansgsband

Schülerinnen und Schüler auf diesem Niveau sind zu echter Forschung fähig. Das Wirkungsvollste, was Sie in dieser Einheit tun können, ist, ihnen eine echte, offene Frage zu geben — kein vorherbestimmtes Ergebnis zur Bestätigung — und ihnen die Werkzeuge und die Zeit zur Verfügung zu stellen, es zu untersuchen.

Die zentrale Projektthese (*„Die innere Haltung einer Landwirtin oder eines Landwirts gegenüber dem Boden spiegelt sich in messbaren Bodenqualitätsparametern wider"*) ist durch kein einzelnes Experiment beweisbar. Das ist ein Merkmal, kein Fehler. Schülerinnen und Schüler, die ehrlich forschen, werden Belege finden, die suggestiv, aber nicht schlüssig sind. Das ist die Realität wissenschaftlicher Forschung in komplexen Systemen. Lernen, mit vorläufigen Ergebnissen umzugehen und angemessene Unsicherheit auszudrücken, ist eine Forschungskompetenz, die mindestens so wichtig ist wie der physikalische Inhalt selbst.

**Vollständige Physikkonzepte auf dieser Stufe:**
- Mie-Streuung (qualitativ und halbquantitativ: Partikelgröße und Wellenlängenwechselwirkung)
- Ligandfeldtheorie (d-Orbital-Aufspaltung in Fe³⁺ als Ursache der Eisenoxidfarbe)
- CIELAB-Farbraum (L*-, a*-, b*-Koordinaten; Δ*E* als Maß für Farbdifferenz)
- Spektroskopie: Reflexionsspektren, Absorptionsmaxima, Identifikation anhand der RRUFF-Datenbank
- Kolloidphysik: Stabilität kolloidaler Suspensionen, Filmbildungsmechanismen
- IoT-Datenintegration: Korrelation von senseBox-Feuchte-/Temperaturdaten mit Spektralmessungen

**Potenzial für Facharbeit:** Die Forschungspräsentation in Einheit 7 kann für Schülerinnen und Schüler der Klassen 11–12 zu einer formellen Facharbeit oder wissenschaftlichen Vorarbeit ausgebaut werden. Die Frage *„Was sagt uns die Eisenoxid-Mineralogie über vergangene Bodenbewirtschaftung und künftige Bodenqualität unter verschiedenen Regimen?"* ist auf diesem Niveau als echte Forschungsfrage tragfähig.

**Fächerübergreifende Bezüge:** Physik (Optik, Spektroskopie), Chemie (Koordinationschemie, Kristallchemie), Biologie (Bodenökologie, Zersetzung, Humusbildung), Erdkunde (Pedogenese, Bodenkunde), Mathematik (Statistik, Regression, Matrizenalgebra für Farbraumtransformation), Wissenschaftsmethodik (Hypothesendesign, Versuchsprotokoll, wissenschaftliches Schreiben).

* * *

## Theoretischer Hintergrund für Lehrende (Zusammenfassung)

### Warum Eisenoxide farbig sind — Ligandfeldtheorie

Eisen liegt im Boden hauptsächlich als Fe³⁺ (dreiwertiges Eisen) vor. Das Fe³⁺-Ion hat fünf ungepaarte d-Elektronen. Wenn es von Sauerstoffliganden umgeben ist (wie in allen Eisenoxidmineralen), werden diese d-Elektronen durch das Ligandenfeld in zwei Energieniveaus aufgespalten. Licht mit der richtigen Energie kann ein Elektron vom unteren auf das höhere Niveau anregen — das entfernt diese Wellenlänge aus dem reflektierten Spektrum.

Die genaue Energie der Aufspaltung hängt von der Geometrie und dem Abstand der Sauerstoffliganden ab — der zwischen Goethit, Hämatit, Lepidokrokit und Ferrihydrit variiert. Deshalb hat jedes Eisenoxidmineral eine charakteristische Farbe:
- Goethit (oktaedrisches Fe³⁺ mit OH-Liganden): absorbiert Violett-Blau → gelb
- Hämatit (Korundstruktur, kantenverknüpfte Oktaeder): absorbiert Blau-Grün → rot
- Lepidokrokit (andere Schichtstruktur): absorbiert Blau → orange

### CIELAB-Farbraum

CIELAB ist ein internationaler Standard für die beobachter- und geräteunabhängige Farbmessung. Drei Koordinaten:
- **L*** : Helligkeit (0 = schwarz, 100 = weiß)
- **a*** : Rot-Grün-Achse (positiv = rot, negativ = grün)
- **b*** : Gelb-Blau-Achse (positiv = gelb, negativ = blau)

**Δ*E*** (Delta E) ist der euklidische Abstand zweier Farben im CIELAB-Raum:
$$\Delta E = \sqrt{(\Delta L^*)^2 + (\Delta a^*)^2 + (\Delta b^*)^2}$$

Ein Δ*E* < 1 ist für das menschliche Auge nicht wahrnehmbar. Ein Δ*E* von 2–3 ist gerade wahrnehmbar. Ein Δ*E* > 5 ist deutlich unterschiedlich. Schülerinnen und Schüler können damit Farbunterschiede zwischen Hofböden, zwischen Mahlzeitfraktionen und zwischen Nass- und Trockenzuständen quantifizieren.

### Mie-Streuung und Partikelgröße

Die Mie-Streuungstheorie (Gustav Mie, 1908) beschreibt, wie Licht mit kugelförmigen Partikeln einer Größe vergleichbar der Lichtwellenlänge (~400–700 nm für sichtbares Licht) wechselwirkt. Die Schlüsselbeziehungen für diese Einheit:
- Partikel viel größer als die Wellenlänge: diffuse (geometrische) Streuung — helles, weißliches Erscheinungsbild.
- Partikel vergleichbar in der Größe mit der Wellenlänge (ca. 0,1–10 μm): starke Mie-Streuung — hohe Deckkraft, kräftige Farbe.
- Partikel viel kleiner als die Wellenlänge (unter ~100 nm): Rayleigh-Streuung — halbtransparent, blauer Farbton.

Deshalb liegt die optimale Pigmentpartikelgröße (5–50 μm) im Mie-Bereich — starke Streuung bei allen sichtbaren Wellenlängen, kombiniert mit der spezifischen Absorption des Eisenoxids.

* * *

## Einheit 1 — Geländearbeit: Systematische Probenahme und Goetheanische Beobachtung

**Dauer:** 45 Minuten (als 90 Minuten mit Hofbesuch empfohlen)
**Lernort:** Partnerhofsstandorte
**4A-Weg-Stufe:** Wahrnehmung
**Benötigte Materialien:** Probenbeutel (200–500 g je Probe), Standortbeschreibungsformular, Munsell-Bodenfarbkarte, pH-Streifen, EC-Meter (wenn verfügbar), Spaten, Kamera, GPS, senseBox-Sensor-Standortkarte

### Lernziele

Am Ende dieser Einheit können die Schülerinnen und Schüler:
- Ein systematisches Probenahmeprotokoll über drei Bewirtschaftungssysteme entwerfen und umsetzen
- Quantitative Standortparameter erfassen (Farbe nach Munsell, pH, Textur, Tiefe)
- Goetheanische Beobachtung praktizieren: anhaltende Aufmerksamkeit für das Phänomen vor jeglichem Erklärungsversuch
- GPS-Standorte für die Sensorkorrelation in Einheit 6 identifizieren

### Unterrichtsplan

**Einstieg (7 Min):**
Vor dem Eintreffen am ersten Standort das goetheanische Beobachtungsprotokoll einführen: *„Wir verbringen an jedem Standort drei Minuten damit, nur zu schauen und wahrzunehmen — keine Labels, keine Erklärungen. Nur beschreiben, was ihr beobachtet."* Diese Praxis — Verlangsamen vor dem Kategorisieren — ist ein formaler Forschungsansatz, der von Goethe entwickelt wurde und in der Pflanzen- und Ökologiewissenschaft noch heute genutzt wird.

Die Projektthese vorstellen: *„Das Projekt behauptet, dass die innere Beziehung einer Landwirtin oder eines Landwirts zur Erde sich in messbaren Bodeneigenschaften niederschlägt. Am Ende dieser Einheit werden wir unsere eigene Ausgangshypothese dazu gebildet haben."*

**Direkte Erfahrung (8 Min pro Standort × 3 Standorte = 24 Min):**
An jedem Hofstandort:
1. Stille Beobachtungszeit (3 Min): Welche Farbe? Welcher Geruch? Welche Textur von der Oberfläche aus sichtbar? Welche Organismen sichtbar?
2. Profilaufschluss (Spaten, 30 cm): mit Maßstab fotografieren.
3. Systematische Datenerhebung pro Schülerpaar:
   - Munsell-Farbe nass und trocken an drei Tiefen (0–5 cm, 10–15 cm, 25–30 cm)
   - pH an jeder Tiefe
   - Textur per Fingertest und geschätzte Erfassung
   - GPS-Koordinaten
   - Nähe zum senseBox-Sensor-Standort (Abstand notieren)

**Synthese (10 Min):**
Am Ende der Geländesitzung vergleichen Schülerinnen und Schüler ihre Erstbeobachtungen von allen drei Standorten. Jede Schülerin / jeder Schüler schreibt eine Absatz-Hypothese: *„Ich vermute, dass der Boden von [Hofname] [Farbeigenschaft] in den Spektroskopiedaten zeigen wird, weil…"*

Hypothesen werden gesammelt (unbenotet) — sie werden in Einheit 6 zurückgegeben, damit Schülerinnen und Schüler sie gegen ihre eigenen Ergebnisse abwägen können.

**Abschluss (4 Min):**
Proben beschriften und sichern. Vorschau: *„Im Labor werden wir diese Proben physikalisch charakterisieren und ihre Farbe objektiv messen — dann die Messungen mit eurer Hypothese vergleichen."*

* * *

## Einheit 2 — Laborverarbeitung: Präzise Korngrößenanalyse

**Dauer:** 45 Minuten
**Lernort:** Erdpuls Zone B
**4A-Weg-Stufe:** Anerkennung
**Benötigte Materialien:** Getrocknete Bodenproben (Ofen 50 °C, 24 h von Lehrkraft vorgetrocknet wenn Zeit knapp), Siebe (500/250/100/63 μm), Präzisionswaage (1 mg), Mörser und Pistill, Schalen, FFP2-Masken, Schutzbrillen, Laborheft

### Lernziele

Am Ende dieser Einheit können die Schülerinnen und Schüler:
- Eine präzise Siebanalyse durchführen und die Korngrößenverteilung als Prozentfraktionen berechnen
- Eine kumulative Korngrößenverteilungskurve zeichnen
- Korngrößenverteilung mit Bodentextur und Pigmentpotenzial verknüpfen
- Das Staubschutzprotokoll anwenden und seine wissenschaftliche Grundlage erklären

### Unterrichtsplan

**Einstieg (8 Min):**
Sicherheitsprotokoll besprechen — Masken und Schutzbrillen anlegen, bevor die Trockenprozessierung beginnt. Dann: *„Eine Siebanalyse gibt uns nicht nur Partikelgrößen — sie gibt uns den Ausgangspunkt, um zu verstehen, wie sich dieser Boden als Pigment verhalten wird. Herausfinden, welcher Anteil jeder Probe für die Farbe potenziell nutzbar ist."*

**Untersuchung (30 Min):**
In Paaren, eine Probe pro Paar arbeitend:

1. Gesamtprobe wiegen (als M_gesamt erfassen).
2. Siebe stapeln: 500 μm (oben) → 250 μm → 100 μm → 63 μm → Auffangschale (unten).
3. Probe 10 Minuten im Mörser mahlen. FFP2-Masken durchgehend tragen.
4. Gemahlene Probe in das oberste Sieb geben. 5 Minuten schütteln (mechanisch oder von Hand).
5. Jede Fraktion wiegen. Erfassen.
6. Prozentsatz berechnen, der auf jedem Sieb zurückbleibt:
   % = (Masse der Fraktion / M_gesamt) × 100
7. Kumulative Verteilung darstellen: x-Achse = Siebmaschen-weite, y-Achse = % Durchgang.

Kurven der drei Hofproben vergleichen: welcher Hof liefert die feinste Fraktion? Welcher die gröbste?

**Synthese (5 Min):**
*„Welcher Hofboden hat den höchsten Anteil an Material im 63–250 μm-Bereich — dem optimalen Pigmentbereich? Stimmt das mit eurer Geländebeobachtung zur Farbintensität überein?"*

Konzept einführen: Über die Korngrößenverteilung hinaus sagt uns die *Form* der kumulativen Kurve etwas über die Entstehungsgeschichte des Bodens. Eine steile, enge Kurve deutet auf einen gut sortierten Sand hin (wie ein Strand oder eine Düne). Eine flache, breite Kurve deutet auf einen gemischten Boden mit vielen Korngrößen hin (wie ein lehmiger Ackerboden). Was sagen unsere Kurven über die glaziale Geologie von Müllrose?

**Abschluss (2 Min):**
Laborheft: kumulative Korngrößenverteilungskurven für alle drei Hofproben. d₅₀-Wert (mittlere Korngröße) für jede Probe notieren.

* * *

## Einheit 3 — Reflexionsspektroskopie: Farbe objektiv messen

**Dauer:** 45 Minuten
**Lernort:** Erdpuls Zone B
**4A-Weg-Stufe:** Anerkennung
**Benötigte Materialien:** Gemahlene Pigmentproben (aus Einheit 2), Smartphones mit Spectroid-App (oder DIY-Spektrometer aus DVD-Beugungsgitter und Pappe), weißes Referenzpapier, GIMP auf Laptop für RGB-zu-CIELAB-Konversion, RRUFF-Projektdatenbank (online), Aquarellpapier für Probenflecken

### Lernziele

Am Ende dieser Einheit können die Schülerinnen und Schüler:
- Ein Reflexionsspektrum mit einem Smartphone-Spektrometer aufzeichnen
- Das Absorptionsmaximum eines Pigments aus dem Spektrum identifizieren
- Die L*-, a*-, b*-CIELAB-Koordinaten aus RGB-Werten berechnen oder abschätzen
- Δ*E* zwischen zwei Pigmentproben berechnen
- Das Spektrum einer Müllroser Probe mit einem Referenz-Mineralspektrum aus der RRUFF-Datenbank vergleichen

### Unterrichtsplan

**Einstieg (8 Min):**
Das Konzept des Reflexionsspektrums einführen: *„Euer Auge nimmt Farbe wahr, indem es das reflektierte Spektrum über drei Arten von Fotorezeptoren (Zapfen) integriert. Ein Spektrometer macht dasselbe mathematisch, misst aber jede Wellenlänge einzeln. Das Spektrum enthält mehr Information als Farbe — es sagt uns, welche Minerale vorhanden sind."*

Den Spectroid-Aufbau demonstrieren: Pappabschirmung gegen Umgebungslicht, weißes Papier für die Referenzmessung (Weißreferenz = 100%-Reflexionsbasislinie), Pigmentfleck auf weißem Papier für die Probenmessung.

**Untersuchung (30 Min):**

Teil 1 — Spektralaufnahme (15 Min):
Jedes Paar zeichnet Reflexionsspektren auf von:
- Einer Probe von jedem der drei Höfe (gleiche Mahlzeit / -fraktion zur Vergleichbarkeit)
- Einer nassen und einer trockenen Version einer Probe
- Einer rohen und einer 30-Minuten-gemahlenen Version einer Probe

Wellenlänge des Absorptionsmaximums notieren (wo reflektiertes Licht am niedrigsten ist = am meisten absorbiert).

Teil 2 — CIELAB-Konversion und Δ*E* (10 Min):
Jeden Pigmentfleck mit einer kalibrierten Handykamera fotografieren. In GIMP importieren. RGB-Werte ablesen (Farbe → Farbe-Balance-Werkzeug oder Farbaufnahme-Werkzeug). RGB zu CIELAB konvertieren mithilfe des GIMP-Farbaufnahme-Berichts oder manuell über die Standard-Transformationsmatrix (Lehrkraft stellt Konversionstabelle oder Tabellenkalkulation bereit).

Δ*E* berechnen zwischen:
- Hof A vs. Hof B
- Hof A vs. Hof C
- Hof B vs. Hof C
- Nass vs. trocken (gleiche Probe)

Teil 3 — RRUFF-Vergleich (5 Min):
rruff.info öffnen. Nach „Goethit" und „Hämatit" suchen. Referenzspektren mit den Müllroser Probenspektren vergleichen. Auf welches Mineral deutet das Absorptionsmaximum für jeden Hofboden hin?

**Synthese (5 Min):**
Klassen-Vergleich der Δ*E*-Werte. Schlüsselfrage: *„Ist der Farbunterschied zwischen den drei Höfen wissenschaftlich signifikant? (Δ*E* > 3 ist für das geschulte Auge wahrnehmbar.) Unterstützt oder widerspricht das Spektraldatum eurer Hypothese aus Einheit 1?"*

**Abschluss (2 Min):**
Laborheft: Spektren gezeichnet oder fotografiert, Δ*E*-Werte erfasst, RRUFF-Vergleich notiert.

* * *

## Einheit 4 — Bindemittelphysik: Kolloidale Suspension und Filmbildung

**Dauer:** 45 Minuten
**Lernort:** Erdpuls Zone B
**4A-Weg-Stufe:** Anerkennung → Haltung
**Benötigte Materialien:** Gemahlenes Pigment, fünf Bindemittel (Wasser, Leinöl, Gummi-arabicum-Lösung, Eigelb, Kasein), Aquarellpapier, Pinsel, Waage, Timer, GIMP oder Farb-App für Δ*E*-Messung beim Trocknen; optional: Polarisationsfilter für Brechungsindex-Demonstration

### Lernziele

Am Ende dieser Einheit können die Schülerinnen und Schüler:
- Farbe als kolloidale Suspension beschreiben und erklären, was „kolloidal" bedeutet
- Den Filmbildungsmechanismus von mindestens zwei Bindemitteln erklären (oxidative Polymerisation vs. Lösungsmittelverdunstung)
- Δ*E* zwischen Nass- und Trockenzustand für jedes Bindemittel messen
- Brechungsindex des Bindemittels mit der Größe der Farbveränderung korrelieren

### Unterrichtsplan

**Einstieg (7 Min):**
Kolloidphysik einführen: *„Ein Kolloid ist ein Gemisch, bei dem kleine Partikel in einem anderen Stoff verteilt sind — aber nicht gelöst. Milch ist ein Kolloid (Fetttröpfchen in Wasser). Nebel ist ein Kolloid (Wassertröpfchen in Luft). Farbe ist ein Kolloid: Pigmentpartikel, die im Bindemittel suspendiert sind."*

Was macht ein Kolloid stabil? Die Partikel müssen klein genug sein, dass sie nicht sofort absinken, und sie müssen ausreichend Oberflächenladung tragen (oder mit einem stabilisierenden Molekül überzogen sein), um sich gegenseitig abzustoßen. In Farbe adsorbieren die Bindemittelmoleküle auf der Pigmentoberfläche und verhindern Klumpenbildung.

**Untersuchung (28 Min):**
Schülerinnen und Schüler erstellen den Fünf-Bindemittel-Vergleich aus dem Klassen 5–8-Plan, aber mit einer zusätzlichen quantitativen Ebene: Messung von Δ*E* für den Nass-zu-Trocken-Übergang für jedes Bindemittel.

Für jedes Bindemittel:
1. Pigment zu einer einheitlichen Paste mischen (Waage verwenden: 1 g Pigment + Bindemittelmenge nach Standardrezept).
2. 1 cm × 5 cm-Streifen auf Aquarellpapier auftragen. Sofort fotografieren.
3. Nach 10 Min, 20 Min, 30 Min und einmal vollständig trocken erneut fotografieren.
4. RGB-Werte aus jedem Foto ablesen. In CIELAB konvertieren. Δ*E* (nass → trocken) berechnen.

Außerdem notieren:
- Sichtbare Rissbildung (Rissbreite in mm wenn vorhanden)
- Wasserbeständigkeit (Tropfentest nach 24 h)
- Haftung (Klebetest nach 48 h — nächste Sitzung zurückmelden)

Diskussion während der Arbeit: *„Warum nimmt Leinöl beim Trocknen tatsächlich an Masse zu? (Sauerstoff vernetzt die Fettsäureketten.) Warum trocknet Eitempera schneller als Aquarellfarbe? (Das Protein im Eigelb gerinnt und setzt den Film schnell fest.)"*

**Synthese (8 Min):**
Δ*E*-Werte für den Nass-Trocken-Übergang über die fünf Bindemittel vergleichen. Als Balkendiagramm darstellen.
Schlüsselfrage: *„Welches Bindemittel zeigt das kleinste Δ*E* (geringste Aufhellung)? Was hat der Brechungsindex des Bindemittels damit zu tun?"*

Theorie: Die Farbveränderung beim Trocknen ist näherungsweise proportional zum Brechungsindexunterschied zwischen Bindemittel und Luft. Leinöl hat einen relativ hohen Brechungsindex (n ≈ 1,48); Wasser n ≈ 1,33; Luft n = 1,0. Ein höherbrechendes Bindemittel widersteht der Zunahme der Lichtstreuung beim Ersetzen durch Luft → weniger Aufhellung.

**Abschluss (2 Min):**
Laborheft: Δ*E*-Tabelle und Balkendiagramm. Ein Absatz Empfehlung: welches Bindemittel für die WP4-Ausstellungsgemälde und warum.

* * *

## Einheit 5 — Pigmentherstellung: Von den Daten zum Material

**Dauer:** 45 Minuten
**Lernort:** Erdpuls Zone B
**4A-Weg-Stufe:** Handlung
**Benötigte Materialien:** Abschließendes gemahlenes Pigment aus bester Fraktion, gewähltes Bindemittel (Klassenentscheidung aus Einheit 4), Glasgläser (50 ml), Präzisionswaage, Etiketten, Aquarellpapier für abschließendes Kunstwerk, Pinsel, Farbenbibliotheks-Archivformular

### Lernziele

Am Ende dieser Einheit können die Schülerinnen und Schüler:
- Eine ausreichende Menge ausstellungsqualitätsfähiges Pigment unter Verwendung der in Einheiten 2–4 ermittelten optimalen Parameter herstellen
- Die Produktion mit vollständigen Herkunftsdaten dokumentieren (Standort, Hof, Tiefe, Mahlparameter, Bindemittelverhältnis)
- Die wissenschaftlichen Ergebnisse mit dem künstlerischen Output im WP4-Kontext in Beziehung setzen

### Unterrichtsplan

**Einstieg (5 Min):**
Die in Einheit 2–3 ermittelten optimalen Mahlparameter besprechen (optimale Siebfraktion für Farbintensität). Bindemittelempfehlung aus Einheit 4 bestätigen. Aufgabe festlegen: *„Heute wechseln wir von Experimenten zur Produktion. Wir stellen die tatsächlichen Pigmente für die Ausstellung her."*

**Herstellung (30 Min):**

Produktionssequenz pro Schülerin / Schüler oder Paar:
1. 5–10 g der 63–250 μm-Fraktion der farbstärksten Hofprobe abwiegen.
2. Für die ermittelte optimale Zeit (aus Einheit 3-Daten) mahlen.
3. Mit Bindemittel gemäß den in Einheit 4 ermittelten Standardrezeptverhältnissen mischen.
4. Glasglas füllen. Verschließen.
5. Beschriften: **[Dominantes Mineral / Munsell-Code] / [Hofname] / [Tiefe] / [Mahlzeit] / [Bindemittel] / [Datum] / [Klasse] / [Name]**
6. Glas auf weißem Hintergrund fotografieren.
7. Farbenbibliotheks-Archivformular ausfüllen.

Wenn Zeit bleibt: ein abschließendes Gemälde mit allen drei Hofpigmenten auf Aquarellpapier anfertigen, mit der Absicht, die drei Farben im Dialog miteinander zu zeigen.

**Synthese (7 Min):**
Alle Gläser ausstellen. Die Sammlung als Ganzes betrachten.
*„Wir haben mit einer Frage begonnen: Beeinflusst die Bewirtschaftungsmethode die Bodenfarbe? Was sagen eure Daten? Was sagt die Glassammlung vor euch?"*

Eine echte Diskussion zulassen — widersprüchliche Ergebnisse sind willkommen. Die These ist eine Hypothese. Die Wissenschaft ist nicht abgeschlossen.

**Abschluss (3 Min):**
Laborheft: die endgültigen Produktionsparameter erfassen. Menge und CIELAB-Koordinaten des Pigments notieren. Das beschriftete Glas für die Aufnahme in die Müllroser Erdfarben-Bibliothek abgeben.

* * *

## Einheit 6 — Korrelationsstudie: Sensordaten trifft Spektroskopie

**Dauer:** 45 Minuten
**Lernort:** Erdpuls Zone C (IoT-Sensor-Dashboard) + Zone B
**4A-Weg-Stufe:** Haltung
**Benötigte Materialien:** senseBox-Sensor-Daten-Download (von Lehrkraft oder Erdpuls-Team vor der Sitzung vorbereitet), Spektraldaten aus Einheit 3, Tabellenkalkulationssoftware (LibreOffice Calc oder Python), Millimeterpapier oder Computer zum Zeichnen, Referenzblatt für die statistische Korrelationsformel

### Lernziele

Am Ende dieser Einheit können die Schülerinnen und Schüler:
- senseBox-Sensordaten (Bodenfeuchte, Temperatur) herunterladen und interpretieren
- Die Beziehung zwischen Bodenfeuchte zum Zeitpunkt der Probenahme und CIELAB-L*-Wert darstellen
- Einen Pearson-Korrelationskoeffizienten zwischen Sensordaten und Spektralmessungen berechnen
- Das Ergebnis im Kontext der Projektthese interpretieren

### Unterrichtsplan

**Einstieg (8 Min):**
Die IoT-Verbindung einführen: *„Die senseBox-Sensoren an jedem Hof haben Bodenfeuchte und Oberflächentemperatur kontinuierlich aufgezeichnet. Wir haben unsere Spektralmessungen derselben Böden. Jetzt können wir fragen: Korrelieren die Sensorwerte mit unseren Farbmessungen?"*

Die zugrundeliegende Physik: Bodenfeuchte beeinflusst die Farbe (L*, Helligkeit, nimmt mit Feuchte ab) durch den Mie-Streuungsmechanismus. Temperatur beeinflusst die Bodenchemie über die Zeit — warme, feuchte Bedingungen begünstigen die Hämatitbildung; kühle, feuchte Bedingungen begünstigen Goethit. Wenn sich die senseBox-Daten der drei Höfe systematisch unterscheiden, sollten es die Farbdaten ebenfalls tun.

**Untersuchung (30 Min):**

Teil 1 — Sensordaten herunterladen und prüfen (10 Min):
Über die senseBox-Oberfläche oder eine vorher heruntergeladene CSV die Feuchte- und Temperaturdaten der drei Höfe über den Probenahmezeitraum anzeigen. Den Zeitpunkt jeder Bodenprobenahme identifizieren. Den Sensorwert zu diesem Zeitpunkt notieren.

Teil 2 — Korrelation darstellen (10 Min):
Für jede der Proben im Datensatz (mindestens eine pro Hof pro Tiefe = 9 Datenpunkte):
- x-Achse: senseBox-Feuchtewert zum Zeitpunkt der Probenahme (%)
- y-Achse: CIELAB-L*-Wert aus Einheit 3

Als Streudiagramm darstellen. Trendlinie einzeichnen (per Augenmaß oder Tabellenkalkulationsfunktion).

Teil 3 — Pearson-Korrelationskoeffizient (10 Min):
Mithilfe der bereitgestellten Formel (oder einer Tabellenkalkulationsfunktion) r (Pearsons r) für die Feuchte-L*-Beziehung berechnen.
Interpretieren: r nahe -1 bedeutet starke negative Korrelation (feuchter → dunkler, wie erwartet). r nahe 0 bedeutet keine Korrelation. r nahe +1 bedeutet feuchter → heller (unerwartet, aber für einige Bodentypen möglich).

Besprechen: *„Ist unser Ergebnis mit nur 9 Datenpunkten statistisch bedeutsam? Was wäre nötig, um das Vertrauen in diesen Befund zu erhöhen?"*

**Synthese (5 Min):**
Zu den in Einheit 1 formulierten Hypothesen zurückkehren. Wie gut stimmte die Vorhersage jeder Schülerin / jedes Schülers mit den Daten überein? Schülerinnen und Schüler bitten, einen Satz zu schreiben, der ihre ursprüngliche Hypothese modifiziert oder bestätigt.

Das Konzept der vorläufigen Wissenschaft einführen: *„In der echten Forschung ist ein Datensatz von 9 Punkten eine Pilotstudie, keine Schlussfolgerung. Was wir getan haben, ist herauszufinden, ob eine größere Studie lohnenswert ist. Das ist ein echter und wertvoller wissenschaftlicher Ertrag."*

**Abschluss (2 Min):**
Laborheft: Streudiagramm, r-Wert, überarbeiteter Hypothesenaussage.

* * *

## Einheit 7 — Wissenschaftliche Kommunikation: Ergebnisse präsentieren

**Dauer:** 45 Minuten
**Lernort:** Präsentationsraum oder Klassenraum
**4A-Weg-Stufe:** Handlung
**Benötigte Materialien:** Laborhefte, Pigmentgläser, abschließende Gemälde, Posterpapier oder digitales Präsentationswerkzeug, alle Datensätze aus Einheiten 1–6

### Lernziele

Am Ende dieser Einheit können die Schülerinnen und Schüler:
- Einen Forschungsbefund klar und präzise einem nichtspezialisierten Publikum vorstellen
- Ein wissenschaftliches Argument strukturieren: Frage → Methode → Daten → Interpretation → Schlussfolgerung
- Zwischen dem, was die Daten zeigen, und dem, was sie nahelegen, unterscheiden
- Grenzen ihrer Untersuchung identifizieren und zukünftige Richtungen vorschlagen

### Unterrichtsplan

**Einstieg (5 Min):**
Kontext setzen: *„Ihr habt eine echte Untersuchung durchgeführt. Jetzt kommuniziert ihr sie — wie eine Forscherin oder ein Forscher es täte, auf einer Tagung oder in einem Aufsatz. Euer Publikum heute sind [Hofpartnerinnen und -partner / eine andere Klasse / Lehrkräfte / Ausstellungsbesucherinnen und -besucher]. Sie haben diese Arbeit nicht mit euch gemacht. Eure Aufgabe: ihnen sagen, was ihr herausgefunden habt — und was ihr denkt, was es bedeutet."*

**Vorbereitung (15 Min):**
In Gruppen von 2–3 bereiten Schülerinnen und Schüler eine 5-minütige Präsentation oder ein Forschungsposter vor. Erforderliche Struktur:
1. **Frage** — Was haben wir gefragt?
2. **Methode** — Wie haben wir es untersucht? (kurz)
3. **Befunde** — Was zeigten die Daten? (konkrete Werte, Diagramme)
4. **Interpretation** — Was denken wir, was das für die Projektthese bedeutet?
5. **Grenzen** — Was könnte in einer Folgestudie besser oder größer sein?
6. **Offene Frage** — Was beantwortet eure Arbeit noch nicht?

**Präsentationen (20 Min):**
Jede Gruppe präsentiert (5 Min je Gruppe, 3–4 Gruppen je nach Klassengröße). Das Publikum wird ermutigt, nach jeder Präsentation eine echte Frage zu stellen.

**Synthese (5 Min):**
Plenum-Debriefing:
- *„Welcher Befund hat euch gruppenübergreifend am meisten überrascht?"*
- *„Wo haben die Daten die Projektthese gestützt? Wo haben sie sie in Frage gestellt?"*
- *„Wenn ihr noch ein weiteres Semester für diese Forschung hättet — was würdet ihr untersuchen?"*

Optional: eine Hofpartnerin oder einen Hofpartner zu dieser Sitzung einladen. Wenn ihr Boden in CIELAB-Koordinaten und Pearson-Korrelationen beschrieben wird — und dann mit der tatsächlichen Farbe auf dem Papier verglichen wird — ist das ein kraftvoller Abschlussmoment für Schülerinnen, Schüler und Landwirte gleichermaßen.

**Abschluss (5 Min):**
Abschließender Journaleintrag (in Stille geschrieben): *„Eine Sache, die ich jetzt weiß und vorher nicht wusste. Eine Frage, die diese Arbeit aufgeworfen hat und die ich vorher nicht hatte. Eine Sache, die ich mit dem Gelernten tun möchte."*

* * *

## Facharbeits-Erweiterung (Klassen 11–12)

Für Schülerinnen und Schüler, die die Arbeit zu einer Facharbeit oder wissenschaftlichen Vorarbeit ausweiten möchten, ist folgende Forschungsfrage tragfähig:

*„Gibt es eine messbare Korrelation zwischen landwirtschaftlicher Bewirtschaftungsmethode und Eisenoxid-Mineralogie in den Partnerhofsböden von Müllrose, wie durch Reflexionsspektroskopie und CIELAB-Farbanalyse angezeigt?"*

Empfohlene Erweiterungsaktivitäten:
- Saisonale Nachbeprobung (Vertiefungsexperiment September) zum Aufbau eines größeren Datensatzes
- Vergleich der Müllroser Spektren mit Referenzspektren aus der RRUFF-Datenbank zur Mineralidentifikation
- Integration globaler SoilGrids-Daten für regionalen Vergleich
- Formale statistische Analyse (ANOVA über Hofgruppen, multiple Regression mit Feuchte, Temperatur und Bewirtschaftung als Prädiktoren)
- Schriftlicher Bericht in wissenschaftlicher Gliederung: Abstract, Einleitung, Methoden, Ergebnisse, Diskussion, Fazit

Das Erdpuls-Projektteam steht als Forschungsunterstützungspartner für Schülerinnen und Schüler zur Verfügung, die diesen Weg verfolgen.

* * *

## Leistungsbeurteilung für Klassen 9–12

### Laborheft / Forschungsjournal

Das Laborheft dokumentiert den vollständigen Untersuchungsbogen von der Hypothese in Einheit 1 bis zur Präsentation in Einheit 7. Es sollte alle Datentabellen, Diagramme, Spektren und schriftlichen Analysen aus jeder Einheit enthalten.

### Beurteilungskriterien

| Kriterium | Indikator |
|---|---|
| Forschungsfrage | Spezifisch, testbar und mit der Projektthese verknüpft |
| Experimentelles Design | Variablen identifiziert; Kontrollen vorhanden; fairer Versuch erreicht |
| Datenqualität | Präzise Messungen; angemessene signifikante Stellen; vollständige Tabellen |
| Analyse | Berechnungen korrekt; Diagramme angemessen beschriftet und interpretiert |
| Interpretation | Unterscheidet zwischen dem, was Daten zeigen, und dem, was sie nahelegen könnten |
| Wissenschaftliche Kommunikation | Klare Struktur; angemessenes Vokabular; zugänglich für Nichtspezialisten |
| Epistemische Bescheidenheit | Grenzen anerkannt; vorläufige Schlussfolgerungen mit angemessener Unsicherheit formuliert |

### Abschlussfrage (schriftlich)

*„Eure Spektraldaten zeigen ein Δ*E* von 4,7 zwischen dem Boden von Hof A (konventionell) und Hof B (biodynamisch). Was bedeutet dieser Wert physikalisch? Was würdet ihr benötigen, um zu bestätigen, dass dieser Unterschied auf die Bewirtschaftungsmethode zurückzuführen ist und nicht auf andere Variablen?"*

Eine starke Antwort wird: Δ*E* korrekt definieren, festhalten, dass 4,7 klar wahrnehmbar ist, Störvariablen identifizieren (Tiefe, Feuchte zum Zeitpunkt der Probenahme, Ausgangsgestein, saisonale Variation) und ein kontrolliertes Studiendesign vorschlagen, um sie zu berücksichtigen.

* * *

## Materialliste für Klassen 9–12

| Einheit | Wichtige Materialien |
|---|---|
| 1 | Probenbeutel, Standortbeschreibungsformulare, Munsell-Karte, pH-Streifen, EC-Meter, Spaten, Kamera, GPS |
| 2 | Bodenproben, Siebe, Präzisionswaage, Mörser, FFP2-Masken, Schutzbrillen, Laborheft |
| 3 | Gemahlenes Pigment, Smartphones mit Spectroid, GIMP auf Laptop, RRUFF online, Aquarellpapier |
| 4 | Gemahlenes Pigment, 5 Bindemittel, Waage, Timer, GIMP, Aquarellpapier, Polarisationsfilter (optional) |
| 5 | Endpigment, gewähltes Bindemittel, Glasgläser, Etiketten, Archivformular, Aquarellpapier |
| 6 | senseBox-Daten (CSV), Spektraldaten aus Einheit 3, Tabellenkalkulationssoftware, Millimeterpapier |
| 7 | Laborhefte, Pigmentgläser, Gemälde, Posterpapier oder digitales Präsentationswerkzeug |

**FFP2-Masken und Schutzbrillen in Einheiten 2 und 3 beim Trockenмahlen und Sieben erforderlich.**

* * *

## Weiterführende Literatur (für Lehrende)

- Toland, A., Noller, J.S. & Wessolek, G. (Hrsg.) (2019): *Field to Palette — Dialogues on Soil and Art in the Anthropocene.* CRC Press. 681 S. [Unverzichtbar für Einheit 7; die Struktur des künstlerisch-wissenschaftlichen Dialogs im Buch spiegelt das Poster-/Präsentationsformat der Schüler*innen wider. Wessolek ist Emeritus an der TU Berlin — ein natürlicher Ansprechpartner für weiterführende Schülerprojekte]
- Feller, C., Landa, E.R., Toland, A. & Wessolek, G. (2015): Case studies of soil in art. *SOIL* 1: 543–559. DOI: 10.5194/soil-1-543-2015 [Open Access; Schüler*innen können diesen Peer-reviewed-Artikel im Rahmen der Facharbeit als Methodik-Präzedenz für Einheit 6 zitieren. Kostenlos herunterladbar]
- Wessolek, G. (2021): Böden in Kunst und Gesellschaft neu positionieren. *Handbuch der Bodenkunde.* Wiley. DOI: 10.1002/9783527678495.hbbk2021001 [Theoretischer Rahmen für Facharbeiten an der Schnittstelle von Bodenwissenschaft und Gesellschaft]
- Schwertmann, U. & Cornell, R.M. (2000): *Iron Oxides in the Laboratory.* Wiley-VCH. [Grundlage für Einheiten 3 und 6; behandelt RRUFF-vergleichbare Eisenoxid-Spektren]
- Blume, H.-P. u.a. (2018): *Scheffer/Schachtschabel: Lehrbuch der Bodenkunde.* 17. Auflage. Springer Spektrum. [Vollständiger bodenkundlicher Hintergrund für Einheiten 1–2]
- AG Boden / BGR (2024): *Bodenkundliche Kartieranleitung* (KA6). 6. Auflage. E. Schweizerbart, Stuttgart. [Für Facharbeiten zitierbar zur Probenahme-Methodik]
- Doerner, M. / Hoppe, T. (2011): *Malmaterial und seine Verwendung im Bilde.* 24. Auflage. Maier, Ravensburg. [Kolloidphysik der Bindemittel für Einheit 4]

* * *

*Dieses Material ist Teil der Erdpuls-OER-Sammlung und steht unter CC BY-NC-SA 4.0 zur Verfügung.*
*© Living-Lab Erdpuls Müllrose / Michel Garand (2026) und seine Übersetzungen | Gefördert von Änderwerk gGmbH im Rahmen des Programms „Vor Ort Vereint" mit Unterstützung der Robert Bosch Stiftung und der Christian und Dorothee Bürkert Stiftung*
