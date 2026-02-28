import { useState } from "react";

// ── Colour system ─────────────────────────────────────────────────────────────
const STAGE_COLORS = {
  Awareness:      { bg: "bg-amber-500",    ring: "ring-amber-400",    text: "text-amber-700",    light: "bg-amber-50",    border: "border-amber-400",  dot: "#f59e0b" },
  Acknowledgment: { bg: "bg-orange-600",   ring: "ring-orange-400",   text: "text-orange-700",   light: "bg-orange-50",   border: "border-orange-400", dot: "#ea580c" },
  Attitude:       { bg: "bg-blue-600",     ring: "ring-blue-400",     text: "text-blue-700",     light: "bg-blue-50",     border: "border-blue-400",   dot: "#2563eb" },
  Action:         { bg: "bg-emerald-800",  ring: "ring-emerald-600",  text: "text-emerald-800",  light: "bg-emerald-50",  border: "border-emerald-600",dot: "#065f46" },
};

const CONVERGENCE_COLOR = "bg-violet-100 border-violet-400 text-violet-800";

// ── Pathway data ──────────────────────────────────────────────────────────────
const GROUPS = [
  {
    id: "youth",
    label: "Children & Youth",
    emoji: "🌱",
    ages: "Ages 8–18",
    tagline: "Building the ecological imagination before the values-action gap hardens",
    entryZone: "Zone B — Outdoor Soil Laboratory",
    color: "from-emerald-700 to-emerald-900",
    accent: "emerald",
    nodes: [
      {
        stage: "Awareness",
        title: "First Contact with Living Soil",
        ring: "Ring 0–1",
        workshops: ["Questions to the Soil Guide 1"],
        experience: "Ring 0 body calibration; Tier 1 sensory soil encounter (touch, smell, colour, texture); Life Count (organisms per m²); Mystery Soil challenge; Soil Explorer Field Sheet",
        output: "Completed Soil Explorer Field Sheet; photographic soil profile record; oral Life Count",
        token: "Cooperation",
        vag: "You just counted 12 organisms. When did you last think about soil being alive? What would change if you thought about it every day?",
        clusters: ["Environmental Literacy", "Social-Emotional Learning"],
      },
      {
        stage: "Acknowledgment",
        title: "From Campus to Planet",
        ring: "Ring 1–2",
        workshops: ["Questions to the Soil Guide 1", "iNaturalist upload session"],
        experience: "Tier 2 tool introduction (pH strips, thermometer, ribbon test); sensor dialogue; iNaturalist species upload; openSenseMap data entry; connection to global open dataset",
        output: "Verified iNaturalist observations; openSenseMap data point; one named pattern card",
        token: "Mutualism",
        vag: "Your observation is now searchable by a scientist in another country. What else do you know that no one has recorded?",
        clusters: ["Environmental Literacy", "Scientific Inquiry"],
      },
      {
        stage: "Attitude",
        title: "Economy as Ecology",
        ring: "Ring 2–3",
        workshops: ["Token Economy Guide 1 — Garden Economy Game", "Bioregion Mapping Guide 1"],
        experience: "Garden Economy Game (Round 1: market / Round 2: reciprocal); four-element discussion; bioregion boundary deliberation; first Values-Action Map (age-appropriate)",
        output: "Token card set from Garden Economy Game; one bioregion boundary proposal; first Values-Action Map",
        token: "Reciprocity",
        vag: "Round 2 felt different in your body. If your school ran on Round 2 rules, what would change tomorrow?",
        clusters: ["Economic Understanding", "Social-Emotional Learning"],
      },
      {
        stage: "Action",
        title: "From Learner to Contributor",
        ring: "Ring 3–4",
        workshops: ["Co-facilitation of Node 1 session", "Independent senseBox research", "Seasonal longitudinal dataset"],
        experience: "Student facilitator role for a younger group; OR independent research question with senseBox MCU; OR full-season longitudinal soil dataset contribution to Erdpuls commons",
        output: "Facilitation evaluation record; OR documented research question with data; OR seasonal dataset in openSenseMap with narrative",
        token: "Regeneration",
        vag: "You have now taught someone else. What changed in your own understanding when you had to explain it? What do you want to investigate next season?",
        clusters: ["Scientific Inquiry", "Technology Competence", "Social-Emotional Learning"],
      },
    ],
    convergences: [
      { event: "Memory Market", with: "Elders & Intergenerational", nodes: "N3–N4", tokens: "Reciprocity" },
      { event: "Seasonal Cycle", with: "All groups (spring baseline)", nodes: "N2", tokens: "Mutualism" },
    ],
  },

  {
    id: "adults",
    label: "Adults & Families",
    emoji: "🌿",
    ages: "Ages 18+",
    tagline: "Honouring existing knowledge before building new frameworks",
    entryZone: "Full campus — Ring sequence and Repair Café",
    color: "from-teal-700 to-teal-900",
    accent: "teal",
    nodes: [
      {
        stage: "Awareness",
        title: "Sensory Re-entry",
        ring: "Ring 0–4",
        workshops: ["Questions to the Soil Guide 2", "Full ring sequence"],
        experience: "Full ring sequence (Rings 0–4); Goethean observation protocol; Soil Explorer Notebook; sensor dialogue (Tier 1→2); Ring 3 oral history prompt (landscape memory)",
        output: "Completed Soil Explorer Notebook; Ring 3 landscape memory record; first Sensor Dialogue journal entry",
        token: "Cooperation",
        vag: "You estimated the soil temperature correctly within 2 degrees. When did you learn that? What else do you know that you have forgotten you know?",
        clusters: ["Environmental Literacy", "Social-Emotional Learning"],
      },
      {
        stage: "Acknowledgment",
        title: "Seeing What We Already Exchange",
        ring: "Ring 1–2",
        workshops: ["Token Economy Guide 2 — Seeing What We Already Exchange"],
        experience: "'Seeing What We Already Exchange' workshop; mapping non-monetary exchanges already in daily life; four-element identification; Values-Action Map (full adult version)",
        output: "Personal exchange map (A3 visual); Values-Action Map; Cooperation and Reciprocity tokens from session",
        token: "Reciprocity",
        vag: "Three exchanges appeared on your map you never thought of as economic before. Which of those would disappear if they had to be paid for?",
        clusters: ["Economic Understanding", "Social-Emotional Learning"],
      },
      {
        stage: "Attitude",
        title: "Values in Space",
        ring: "Ring 3–4",
        workshops: ["Bioregion Mapping Guide 2", "Repair Café (learner role)"],
        experience: "Bioregion boundary deliberation (Ring 4 walking transect); home garden comparison dataset; Personal Quality Commitment card; Repair Café first participation as learner/fixer",
        output: "GPS transect data for bioregion; home garden soil data in Erdpuls commons; Personal Quality Commitment; repaired object documentation",
        token: "Mutualism + Regeneration",
        vag: "Your garden data shows the same pH shift we see in Zone B after rain. You have been monitoring soil without knowing it. What else might qualify as citizen science in your daily life?",
        clusters: ["Environmental Literacy", "Economic Understanding"],
      },
      {
        stage: "Action",
        title: "Token Holder & Community Anchor",
        ring: "Full campus",
        workshops: ["Token Holder activation", "Repair Café (facilitator role)", "Season-end BNE Quality session"],
        experience: "Token Holder status activation; Repair Café facilitator role (with training); season-end Values-Action Map review; optional co-facilitator in adult Node 1 sessions",
        output: "Active Stellar token holder account; documented Repair Café facilitation; season-end VAG comparison map",
        token: "Regeneration + Mutualism",
        vag: "Compare your Values-Action Map from Node 2 with this one. What actually moved? Design one specific action for next season targeting the most stubborn gap.",
        clusters: ["Economic Understanding", "Technology Competence", "Social-Emotional Learning"],
      },
    ],
    convergences: [
      { event: "Memory Market", with: "Elders & Intergenerational", nodes: "N3", tokens: "Reciprocity" },
      { event: "Repair Café", with: "Elders (craft knowledge)", nodes: "N3–N4", tokens: "Reciprocity" },
      { event: "Annual Pattern Language Assembly", with: "All groups", nodes: "N4", tokens: "Mutualism" },
    ],
  },

  {
    id: "elders",
    label: "Elders & Intergenerational",
    emoji: "🧠",
    ages: "Ages 60+ | Mixed-age",
    tagline: "Elder memory as primary ecological science data",
    entryZone: "Zone E — Heritage & Community Hub + Ring 3",
    color: "from-amber-700 to-amber-900",
    accent: "amber",
    nodes: [
      {
        stage: "Awareness",
        title: "The Landscape Remembers",
        ring: "Ring 3",
        workshops: ["Questions to the Soil Guide 3 — Elder Memory Prompts"],
        experience: "Ring 3 oral history walk; Elder Memory Prompts (what grew here? where did water flow differently? what disappeared first?); sensory comparison of current landscape against memory",
        output: "Elder Memory Record (oral testimony transcribed or recorded); Ring 3 annotated map with memory locations",
        token: "Reciprocity",
        vag: "You just described a species that is no longer here. Is that knowledge written down anywhere? What would be lost if it stayed only in your memory?",
        clusters: ["Environmental Literacy", "Social-Emotional Learning"],
      },
      {
        stage: "Acknowledgment",
        title: "Memory as Science",
        ring: "Ring 3–4",
        workshops: ["BNE Quality Guide 3 — Memory Market", "GIS Elder Memory Map"],
        experience: "Memory Market workshop: elder knowledge stations paired with young participants; Elder Memory Map (overlaying memory on current GIS); comparison with iNaturalist data from same locations",
        output: "Memory Market exchange documentation; Elder Memory Map (GIS layer); Reciprocity token flows",
        token: "Reciprocity + Mutualism",
        vag: "Your memory of the willow stand by the stream matched what the soil data shows. Your knowledge was scientific all along. What else would you like to contribute to the record?",
        clusters: ["Environmental Literacy", "Scientific Inquiry"],
      },
      {
        stage: "Attitude",
        title: "From Memory to Future",
        ring: "Ring 3–4",
        workshops: ["Token Economy Guide 3 — Memory Market", "Wisdom Circle"],
        experience: "Wisdom Circle session: past→present→future temporal arc; intergenerational values dialogue; Personal Stewardship Commitment; Erzählcafé archive contribution",
        output: "Wisdom Circle collective reflection record; Personal Stewardship Commitment; Erzählcafé testimony",
        token: "Regeneration",
        vag: "You described what you want to hand on. What specific knowledge needs to be documented before it is lost, and who is the right person to document it with you?",
        clusters: ["Social-Emotional Learning", "Environmental Literacy"],
      },
      {
        stage: "Action",
        title: "Custodian of Place-Knowledge",
        ring: "Full bioregion",
        workshops: ["Elder Memory Map OER publication", "Wisdom Circle facilitation", "Pattern Language Assembly"],
        experience: "Elder Memory Map published as OER (with consent and attribution); Wisdom Circle facilitator role; pattern card custodian (names and authenticates patterns from other groups); Pattern Language Assembly participation",
        output: "OER Elder Memory Map; facilitated Wisdom Circle session record; authenticated pattern cards",
        token: "Regeneration + Mutualism",
        vag: "Your memory map is now searchable by researchers and children you will never meet. What else should be in that map?",
        clusters: ["Environmental Literacy", "Social-Emotional Learning", "Technology Competence"],
      },
    ],
    convergences: [
      { event: "Memory Market", with: "Children & Youth + Adults", nodes: "N2", tokens: "Reciprocity + Mutualism" },
      { event: "Repair Café", with: "Adults & Families", nodes: "N3", tokens: "Reciprocity (craft knowledge)" },
      { event: "Annual Pattern Language Assembly", with: "All groups (as authenticator)", nodes: "N4", tokens: "Mutualism" },
    ],
  },

  {
    id: "artists",
    label: "Artists & Researchers",
    emoji: "🎨",
    ages: "Any age",
    tagline: "Defamiliarisation and methodological depth as a public good",
    entryZone: "Full campus — sustained multi-session residency",
    color: "from-violet-700 to-violet-900",
    accent: "violet",
    nodes: [
      {
        stage: "Awareness",
        title: "Slowing Down to See",
        ring: "Ring 0–4 sustained",
        workshops: ["Pattern Discovery Toolkit — Goethean depth protocol"],
        experience: "Full ring sequence at Goethean depth: sustained single-location observation (minimum 3 sessions, different times of day/weather); Ring 0 body calibration daily journal; Tier 1→2→3 sensory progression explicitly tracked; sensor dialogue with body as primary instrument",
        output: "Daily observation journal (minimum 5 entries); Goethean field notes distinguishing perception from interpretation; first Sensor Dialogue record",
        token: "Cooperation",
        vag: "What did the fifth visit show that the first did not? What did your body notice that your notebook did not initially record?",
        clusters: ["Environmental Literacy", "Scientific Inquiry"],
      },
      {
        stage: "Acknowledgment",
        title: "Patterns Beyond Disciplines",
        ring: "Ring 2–4",
        workshops: ["Pattern Discovery Toolkit — Non-standard cartography", "GIS integration"],
        experience: "Non-standard cartography session: maps campus using own perceptual categories (sound, light, proxemic comfort, aesthetic charge); GIS layer integration with existing open data; pattern documentation across multiple media",
        output: "Non-standard cartographic work; minimum 3 named pattern cards; contribution to Erdpuls longitudinal commons",
        token: "Mutualism",
        vag: "Your sound map and the soil pH map show the same boundary. What is the pattern that connects them, and who needs to know about it?",
        clusters: ["Environmental Literacy", "Technology Competence", "Scientific Inquiry"],
      },
      {
        stage: "Attitude",
        title: "Value Beyond Price",
        ring: "Ring 1–3 (community)",
        workshops: ["Token Economy Guide 4 — Value Beyond Price", "Community integration session"],
        experience: "'Value Beyond Price' workshop: critical examination of what market price fails to measure; four-element token design applied to own practice; critical dialogue on tokenisation and extraction; community integration session with at least one other target group",
        output: "Written responses to four critical dialogue questions; token economy design sketch; community engagement record",
        token: "Reciprocity + Mutualism",
        vag: "Describe your work as embedded in the community that made it possible. What changes in the description? What obligations appear?",
        clusters: ["Economic Understanding", "Social-Emotional Learning"],
      },
      {
        stage: "Action",
        title: "Residency as Living Research",
        ring: "Full bioregion → OER commons",
        workshops: ["OER publication", "GIS synthesis", "Pattern Language Assembly", "Optional: senseBox sensor design"],
        experience: "Residency output published as OER with Creative Commons attribution; GIS synthesis of full-residency pattern language; Pattern Language Assembly presentation; optional sensor station design contribution",
        output: "Published OER residency output; full-residency pattern language synthesis (GIS + narrative); Pattern Language Assembly presentation; optional sensor station documentation",
        token: "Regeneration + Mutualism",
        vag: "Your work is now searchable by anyone. Which of the five target groups is most likely to encounter it, and what do you want them to find?",
        clusters: ["Environmental Literacy", "Scientific Inquiry", "Technology Competence", "Economic Understanding"],
      },
    ],
    convergences: [
      { event: "Community Integration Session", with: "Any other target group", nodes: "N3", tokens: "Reciprocity (bidirectional)" },
      { event: "Pattern Language Assembly", with: "All groups (GIS synthesis)", nodes: "N4", tokens: "Mutualism" },
      { event: "Value Beyond Price dialogue", with: "Programme development", nodes: "N3", tokens: "Mutualism (quality input)" },
    ],
  },

  {
    id: "crossborder",
    label: "Cross-Border DE/PL",
    emoji: "🇩🇪🇵🇱",
    ages: "Any age",
    tagline: "One landscape, two languages, a shared future",
    entryZone: "Zone E — trilingual, balanced DE/PL composition",
    color: "from-rose-700 to-rose-900",
    accent: "rose",
    nodes: [
      {
        stage: "Awareness",
        title: "One Landscape, Two Languages",
        ring: "Ring 0–1 trilingual",
        workshops: ["Questions to the Soil Guide 5", "Trilingual Ring 0 calibration"],
        experience: "Shared glacial landscape introduction as common ground predating the border; trilingual Ring 0 body calibration; multilingual Life Count (same organisms, two languages); soil observation with proxemic notes on cultural distance norms",
        output: "Trilingual Life Count record (DE/EN/PL); individual Ring 0 calibration notes in own language; first cross-cultural proxemic observation",
        token: "Cooperation",
        vag: "You just used three languages to describe the same organism. Which description felt most alive to you? Why might that matter for the science?",
        clusters: ["Environmental Literacy", "Social-Emotional Learning"],
      },
      {
        stage: "Acknowledgment",
        title: "Frameworks That Converge",
        ring: "Ring 2–4",
        workshops: ["BNE Quality Guide 5 — Quality Without Borders", "Cross-border iNaturalist project"],
        experience: "'Quality Without Borders' framework comparison: each delegation presents its sustainability education framework; minimum 5 convergences and 2 genuine divergences identified; shared bioregion boundary deliberation; cross-border citizen science data linked",
        output: "Framework comparison matrix; cross-border bioregion boundary proposal; iNaturalist observations from both sides linked in shared project",
        token: "Mutualism + Reciprocity",
        vag: "Your two frameworks agreed on the same principle but called it different names. What was lost in the naming difference? What would it mean to act on that principle together?",
        clusters: ["Environmental Literacy", "Social-Emotional Learning", "Scientific Inquiry"],
      },
      {
        stage: "Attitude",
        title: "Designing Cross-Border Reciprocity",
        ring: "Zone E — shared meal",
        workshops: ["Token Economy Guide 5 — One Economy, Two Languages", "Shared meal"],
        experience: "Cross-border token economy design workshop; cultural proxemic differences explicitly named as design input; shared meal as embodied reciprocal economy; bilateral Personal Quality Commitment",
        output: "Cross-border token economy design document (bilingual); shared meal documentation; bilateral commitment (signed both sides)",
        token: "Cooperation + Reciprocity + Mutualism",
        vag: "The meal crossed the border because you crossed the border first. What else that currently stops at the border would you like to see crossing it?",
        clusters: ["Economic Understanding", "Social-Emotional Learning"],
      },
      {
        stage: "Action",
        title: "Partnership as Infrastructure",
        ring: "Full bioregion + institutional",
        workshops: ["Cross-border quality principles OER", "INTERREG partnership proposal", "Reciprocal facilitation exchange"],
        experience: "Shared quality principles document (bilingual OER); formal partnership proposal for INTERREG or bilateral funding; cross-border citizen science network design; reciprocal facilitation (DE facilitates in Poland; PL facilitates in Germany)",
        output: "Bilingual quality principles OER document; partnership proposal framework; citizen science network protocol; documented reciprocal facilitation event",
        token: "Regeneration + Mutualism",
        vag: "You now have a working document, a network, and a facilitation exchange. What is the one specific barrier that remains? Who in the room has the power to address it?",
        clusters: ["Economic Understanding", "Social-Emotional Learning", "Technology Competence"],
      },
    ],
    convergences: [
      { event: "Cross-border iNaturalist project", with: "Artists & Researchers (GIS layer)", nodes: "N2", tokens: "Mutualism" },
      { event: "Reciprocal Facilitation Exchange", with: "Any facilitated group", nodes: "N4", tokens: "Regeneration" },
      { event: "Pattern Language Assembly", with: "All groups", nodes: "N4", tokens: "Mutualism" },
    ],
  },
];

// ── Sub-components ────────────────────────────────────────────────────────────

function NodeCard({ node, index, isSelected, onClick }) {
  const sc = STAGE_COLORS[node.stage];
  return (
    <button
      onClick={() => onClick(index)}
      className={`relative flex flex-col items-center cursor-pointer group transition-all duration-200 ${isSelected ? "scale-105" : "hover:scale-102"}`}
      style={{ minWidth: 0 }}
    >
      {/* Connector line to next node */}
      {index < 3 && (
        <div className="absolute top-8 left-1/2 w-full h-0.5 bg-gray-300 z-0"
          style={{ transform: "translateX(50%)" }} />
      )}

      {/* Node circle */}
      <div className={`relative z-10 w-16 h-16 rounded-full flex items-center justify-center border-4 shadow-lg transition-all
        ${sc.bg} border-white
        ${isSelected ? "ring-4 ring-offset-2 " + sc.ring : ""}`}>
        <span className="text-white font-bold text-lg">{index + 1}</span>
      </div>

      {/* Stage badge */}
      <div className={`mt-2 px-2 py-0.5 rounded-full text-xs font-bold text-white ${sc.bg}`}>
        {node.stage}
      </div>

      {/* Title */}
      <div className={`mt-1 text-center text-xs font-semibold leading-tight max-w-24
        ${isSelected ? sc.text : "text-gray-600"}`}>
        {node.title}
      </div>
    </button>
  );
}

function NodeDetail({ node, index }) {
  const sc = STAGE_COLORS[node.stage];
  return (
    <div className={`rounded-2xl border-2 ${sc.border} ${sc.light} p-5 space-y-4`}>
      {/* Header */}
      <div className="flex items-start gap-3">
        <div className={`w-10 h-10 rounded-full flex items-center justify-center text-white font-bold text-lg flex-shrink-0 ${sc.bg}`}>
          {index + 1}
        </div>
        <div>
          <div className={`text-xs font-bold uppercase tracking-wider ${sc.text}`}>
            {node.stage} · {node.ring}
          </div>
          <div className="text-gray-900 font-bold text-base leading-tight">{node.title}</div>
        </div>
      </div>

      {/* Workshops */}
      <div>
        <div className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1">Linked Workshops</div>
        <div className="flex flex-wrap gap-1">
          {node.workshops.map((w, i) => (
            <span key={i} className="bg-white border border-gray-200 text-gray-700 text-xs px-2 py-0.5 rounded-full">{w}</span>
          ))}
        </div>
      </div>

      {/* Core experience */}
      <div>
        <div className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1">Core Experience</div>
        <div className="text-sm text-gray-700 leading-relaxed">{node.experience}</div>
      </div>

      {/* Output */}
      <div className="bg-white rounded-xl border border-gray-100 p-3">
        <div className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1">Output / Evidence Artefact</div>
        <div className="text-sm text-gray-700">{node.output}</div>
      </div>

      {/* Token + VAG */}
      <div className="grid grid-cols-2 gap-3">
        <div className={`rounded-xl p-3 ${sc.light} border ${sc.border}`}>
          <div className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1">Token Earned</div>
          <div className={`text-sm font-bold ${sc.text}`}>{node.token}</div>
        </div>
        <div className="rounded-xl p-3 bg-white border border-yellow-200">
          <div className="text-xs font-bold text-yellow-700 uppercase tracking-wide mb-1">Competency Clusters</div>
          <div className="flex flex-wrap gap-1">
            {node.clusters.map((c, i) => (
              <span key={i} className="text-xs bg-yellow-50 border border-yellow-200 text-yellow-800 px-1.5 py-0.5 rounded">{c}</span>
            ))}
          </div>
        </div>
      </div>

      {/* VAG Bridge */}
      <div className="bg-amber-50 border border-amber-200 rounded-xl p-3">
        <div className="text-xs font-bold text-amber-700 uppercase tracking-wide mb-1">Values-Action Gap Bridge</div>
        <div className="text-sm text-amber-900 italic leading-relaxed">"{node.vag}"</div>
      </div>
    </div>
  );
}

function ConvergencePanel({ convergences }) {
  return (
    <div className="mt-4 space-y-2">
      <div className="text-xs font-bold text-gray-500 uppercase tracking-wide">Cross-Group Convergence Zones</div>
      {convergences.map((c, i) => (
        <div key={i} className={`rounded-xl border p-3 ${CONVERGENCE_COLOR}`}>
          <div className="flex items-center justify-between">
            <div className="font-semibold text-sm">{c.event}</div>
            <div className="text-xs bg-violet-200 text-violet-800 px-2 py-0.5 rounded-full">{c.nodes}</div>
          </div>
          <div className="text-xs mt-1">With: <span className="font-medium">{c.with}</span></div>
          <div className="text-xs mt-0.5">Tokens: <span className="font-medium">{c.tokens}</span></div>
        </div>
      ))}
    </div>
  );
}

// ── Legend ────────────────────────────────────────────────────────────────────
function Legend() {
  return (
    <div className="flex flex-wrap gap-3 justify-center">
      {Object.entries(STAGE_COLORS).map(([stage, sc]) => (
        <div key={stage} className="flex items-center gap-1.5">
          <div className={`w-4 h-4 rounded-full ${sc.bg}`} />
          <span className="text-xs text-gray-600 font-medium">{stage}</span>
        </div>
      ))}
      <div className="flex items-center gap-1.5">
        <div className="w-4 h-4 rounded-full bg-violet-400" />
        <span className="text-xs text-gray-600 font-medium">Convergence Zone</span>
      </div>
    </div>
  );
}

// ── Token legend ──────────────────────────────────────────────────────────────
const TOKEN_DESC = {
  Cooperation: "Collaborative action with others",
  Reciprocity: "Bidirectional value exchange",
  Mutualism: "Benefit extending to the wider community",
  Regeneration: "Demonstrable ecological or social improvement",
};

function TokenLegend() {
  return (
    <div className="grid grid-cols-2 gap-2">
      {Object.entries(TOKEN_DESC).map(([token, desc]) => (
        <div key={token} className="bg-gray-50 border border-gray-200 rounded-lg p-2">
          <div className="text-xs font-bold text-gray-800">{token}</div>
          <div className="text-xs text-gray-500">{desc}</div>
        </div>
      ))}
    </div>
  );
}

// ── Main App ──────────────────────────────────────────────────────────────────
export default function LearningPathwayMaps() {
  const [activeGroup, setActiveGroup] = useState(0);
  const [activeNode, setActiveNode] = useState(0);
  const [showConvergence, setShowConvergence] = useState(false);
  const [showTokens, setShowTokens] = useState(false);

  const group = GROUPS[activeGroup];
  const node = group.nodes[activeNode];

  const handleGroupChange = (idx) => {
    setActiveGroup(idx);
    setActiveNode(0);
    setShowConvergence(false);
  };

  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      {/* Header */}
      <div className="bg-gradient-to-r from-emerald-900 to-emerald-700 text-white px-6 py-5">
        <div className="max-w-5xl mx-auto">
          <div className="text-xs font-bold uppercase tracking-widest text-emerald-300 mb-1">
            Erdpuls Müllrose · Center for Sustainability Literacy, Citizen Science & Reciprocal Economics
          </div>
          <h1 className="text-2xl font-bold">Learning Pathway Maps</h1>
          <p className="text-sm text-emerald-200 mt-1">
            Five target-group pathways · 4A-Pathway depth · Values-Action Gap bridge questions · Token economy integration
          </p>
        </div>
      </div>

      {/* Group selector */}
      <div className="bg-white border-b border-gray-200 px-6 py-3">
        <div className="max-w-5xl mx-auto">
          <div className="flex gap-2 flex-wrap">
            {GROUPS.map((g, i) => (
              <button
                key={g.id}
                onClick={() => handleGroupChange(i)}
                className={`flex items-center gap-2 px-3 py-2 rounded-xl text-sm font-semibold transition-all border
                  ${activeGroup === i
                    ? `bg-gradient-to-r ${g.color} text-white border-transparent shadow-md`
                    : "bg-white text-gray-600 border-gray-200 hover:border-gray-400"}`}
              >
                <span>{g.emoji}</span>
                <span>{g.label}</span>
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="max-w-5xl mx-auto px-6 py-6 space-y-6">

        {/* Group header card */}
        <div className={`bg-gradient-to-r ${group.color} text-white rounded-2xl p-5 flex items-start justify-between`}>
          <div>
            <div className="text-3xl mb-1">{group.emoji}</div>
            <h2 className="text-xl font-bold">{group.label}</h2>
            <div className="text-sm opacity-80 mt-0.5">{group.ages}</div>
            <div className="text-sm italic opacity-90 mt-1">{group.tagline}</div>
          </div>
          <div className="text-right text-xs opacity-75">
            <div className="font-bold mb-1">Entry Zone</div>
            <div>{group.entryZone}</div>
          </div>
        </div>

        {/* Pathway diagram + node detail */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

          {/* Left: pathway map */}
          <div className="lg:col-span-1 bg-white rounded-2xl border border-gray-200 p-5 space-y-4">
            <div className="text-xs font-bold text-gray-500 uppercase tracking-wide">Pathway Map</div>

            {/* Nodes arranged vertically */}
            <div className="flex flex-col gap-4">
              {group.nodes.map((n, i) => {
                const sc = STAGE_COLORS[n.stage];
                return (
                  <button
                    key={i}
                    onClick={() => setActiveNode(i)}
                    className={`relative flex items-start gap-3 text-left p-3 rounded-xl border-2 transition-all
                      ${activeNode === i ? `${sc.border} ${sc.light}` : "border-gray-100 hover:border-gray-200 bg-gray-50"}`}
                  >
                    {/* Vertical line */}
                    {i < 3 && (
                      <div className="absolute left-6 top-full w-0.5 h-4 bg-gray-300 z-0" />
                    )}
                    <div className={`w-10 h-10 rounded-full flex-shrink-0 flex items-center justify-center text-white font-bold z-10 ${sc.bg}`}>
                      {i + 1}
                    </div>
                    <div className="min-w-0">
                      <div className={`text-xs font-bold ${sc.text}`}>{n.stage}</div>
                      <div className="text-sm font-semibold text-gray-800 leading-tight">{n.title}</div>
                      <div className="text-xs text-gray-500 mt-0.5">{n.ring}</div>
                    </div>
                  </button>
                );
              })}
            </div>

            {/* Convergence toggle */}
            <button
              onClick={() => setShowConvergence(!showConvergence)}
              className="w-full text-xs font-semibold text-violet-700 bg-violet-50 border border-violet-200 rounded-xl py-2 mt-2 hover:bg-violet-100 transition"
            >
              {showConvergence ? "▲ Hide" : "▼ Show"} Convergence Zones
            </button>
            {showConvergence && <ConvergencePanel convergences={group.convergences} />}
          </div>

          {/* Right: node detail */}
          <div className="lg:col-span-2">
            <NodeDetail node={node} index={activeNode} />
          </div>
        </div>

        {/* Legend row */}
        <div className="bg-white rounded-2xl border border-gray-200 p-4 space-y-3">
          <div className="text-xs font-bold text-gray-500 uppercase tracking-wide">Stage Legend</div>
          <Legend />
          <div className="pt-2 border-t border-gray-100">
            <button
              onClick={() => setShowTokens(!showTokens)}
              className="text-xs font-semibold text-gray-600 hover:text-gray-900"
            >
              {showTokens ? "▲ Hide" : "▼ Show"} Token Economy Reference
            </button>
            {showTokens && <div className="mt-3"><TokenLegend /></div>}
          </div>
        </div>

        {/* Footer */}
        <div className="text-center text-xs text-gray-400 pb-4">
          <div>© 2025–2026 Erdpuls Müllrose · CC BY-NC-SA 4.0</div>
          <div className="mt-0.5">erdpuls@ubec.network · https://erdpuls.ubec.network</div>
        </div>
      </div>
    </div>
  );
}
