import { useState } from "react";

// ── Colour system ─────────────────────────────────────────────────────────────
const STAGE_COLORS = {
  Awareness:      { bg: "bg-amber-500",    ring: "ring-amber-400",    text: "text-amber-700",    light: "bg-amber-50",    border: "border-amber-400",  dot: "#f59e0b" },
  Acknowledgment: { bg: "bg-orange-600",   ring: "ring-orange-400",   text: "text-orange-700",   light: "bg-orange-50",   border: "border-orange-400", dot: "#ea580c" },
  Attitude:       { bg: "bg-blue-600",     ring: "ring-blue-400",     text: "text-blue-700",     light: "bg-blue-50",     border: "border-blue-400",   dot: "#2563eb" },
  Action:         { bg: "bg-emerald-800",  ring: "ring-emerald-600",  text: "text-emerald-800",  light: "bg-emerald-50",  border: "border-emerald-600",dot: "#065f46" },
};

// ── Stage display labels (UK) ─ keys stay English for STAGE_COLORS lookup ──────
const STAGE_LABELS = {
  Awareness:      "Усвідомлення",
  Acknowledgment: "Визнання",
  Attitude:       "Ставлення",
  Action:         "Дія",
};

const CONVERGENCE_COLOR = "bg-violet-100 border-violet-400 text-violet-800";

// ── Pathway data ──────────────────────────────────────────────────────────────
const GROUPS = [
  {
    id: "youth",
    label: "Діти та молодь",
    emoji: "🌱",
    ages: "Вік 8–18",
    tagline: "Розбудова екологічної уяви, перш ніж розрив між цінностями та діями затвердіє",
    entryZone: "Зона B — Відкрита ґрунтова лабораторія",
    color: "from-emerald-700 to-emerald-900",
    accent: "emerald",
    nodes: [
      {
        stage: "Awareness",
        title: "Перший контакт із живим ґрунтом",
        ring: "Кільце 0–1",
        workshops: ["Путівник «Питання до ґрунту» 1"],
        experience: "Калібрування тіла в Кільці 0; чуттєва зустріч із ґрунтом Рівня 1 (дотик, запах, колір, текстура); Підрахунок життя (організмів на м²); виклик «Таємничий ґрунт»; Польовий аркуш дослідника ґрунту",
        output: "Заповнений Польовий аркуш дослідника ґрунту; фотографічний запис профілю ґрунту; усний Підрахунок життя",
        token: "Співпраця",
        vag: "Ти щойно нарахував 12 організмів. Коли ти востаннє думав про те, що ґрунт живий? Що змінилося б, якби ти думав про це щодня?",
        clusters: ["Екологічна грамотність", "Соціально-емоційне навчання"],
      },
      {
        stage: "Acknowledgment",
        title: "Від кампусу до планети",
        ring: "Кільце 1–2",
        workshops: ["Путівник «Питання до ґрунту» 1", "Сесія завантаження в iNaturalist"],
        experience: "Введення інструментів Рівня 2 (pH-смужки, термометр, стрічковий тест); сенсорний діалог; завантаження видів в iNaturalist; введення даних в openSenseMap; підключення до глобального відкритого набору даних",
        output: "Підтверджені спостереження iNaturalist; точка даних openSenseMap; одна названа картка патерну",
        token: "Мутуалізм",
        vag: "Твоє спостереження тепер може знайти науковець в іншій країні. Що ще ти знаєш, чого ніхто не записав?",
        clusters: ["Екологічна грамотність", "Наукове дослідження"],
      },
      {
        stage: "Attitude",
        title: "Економіка як екологія",
        ring: "Кільце 2–3",
        workshops: ["Путівник «Токенна економіка» 1 — Гра економіки саду", "Путівник «Картографування біорегіону» 1"],
        experience: "Гра економіки саду (Раунд 1: ринок / Раунд 2: реципрокний); обговорення чотирьох елементів; обмірковування межі біорегіону; перша Карта цінностей-дій (відповідна віку)",
        output: "Набір токенних карток із гри економіки саду; одна пропозиція межі біорегіону; перша Карта цінностей-дій",
        token: "Взаємність",
        vag: "Раунд 2 відчувався інакше в твоєму тілі. Якби твоя школа працювала за правилами Раунду 2, що змінилося б завтра?",
        clusters: ["Економічне розуміння", "Соціально-емоційне навчання"],
      },
      {
        stage: "Action",
        title: "Від учня до дописувача",
        ring: "Кільце 3–4",
        workshops: ["Співфасилітація сесії Вузла 1", "Самостійне дослідження із senseBox", "Сезонний поздовжній набір даних"],
        experience: "Роль учня-фасилітатора для молодшої групи; АБО самостійне дослідницьке питання із senseBox MCU; АБО внесок повносезонного поздовжнього набору даних ґрунту до спільноти Erdpuls",
        output: "Запис оцінювання фасилітації; АБО задокументоване дослідницьке питання з даними; АБО сезонний набір даних в openSenseMap з наративом",
        token: "Регенерація",
        vag: "Тепер ти навчив когось іншого. Що змінилося у твоєму власному розумінні, коли тобі довелося це пояснювати? Що ти хочеш дослідити наступного сезону?",
        clusters: ["Наукове дослідження", "Технологічна компетентність", "Соціально-емоційне навчання"],
      },
    ],
    convergences: [
      { event: "Ринок пам'яті", with: "Старші та міжпоколіннєві", nodes: "В3–В4", tokens: "Взаємність" },
      { event: "Сезонний цикл", with: "Усі групи (весняна базова лінія)", nodes: "В2", tokens: "Мутуалізм" },
    ],
  },

  {
    id: "adults",
    label: "Дорослі та сім'ї",
    emoji: "🌿",
    ages: "Вік 18+",
    tagline: "Ушанування наявного знання, перш ніж будувати нові рамки",
    entryZone: "Повний кампус — кільцева послідовність і Repair Café",
    color: "from-teal-700 to-teal-900",
    accent: "teal",
    nodes: [
      {
        stage: "Awareness",
        title: "Чуттєве повернення",
        ring: "Кільце 0–4",
        workshops: ["Путівник «Питання до ґрунту» 2", "Повна кільцева послідовність"],
        experience: "Повна кільцева послідовність (Кільця 0–4); протокол ґетеанського спостереження; Записник дослідника ґрунту; сенсорний діалог (Рівень 1→2); підказка усної історії в Кільці 3 (пам'ять ландшафту)",
        output: "Заповнений Записник дослідника ґрунту; запис пам'яті ландшафту в Кільці 3; перший запис у журналі Сенсорного діалогу",
        token: "Співпраця",
        vag: "Ви оцінили температуру ґрунту правильно з точністю до 2 градусів. Коли ви цьому навчилися? Що ще ви знаєте, про що забули, що знаєте?",
        clusters: ["Екологічна грамотність", "Соціально-емоційне навчання"],
      },
      {
        stage: "Acknowledgment",
        title: "Бачити те, чим ми вже обмінюємося",
        ring: "Кільце 1–2",
        workshops: ["Путівник «Токенна економіка» 2 — Бачити те, чим ми вже обмінюємося"],
        experience: "Майстер-клас «Бачити те, чим ми вже обмінюємося»; картографування негрошових обмінів, уже наявних у щоденному житті; визначення чотирьох елементів; Карта цінностей-дій (повна доросла версія)",
        output: "Особиста карта обмінів (візуальний A3); Карта цінностей-дій; токени Співпраці та Взаємності із сесії",
        token: "Взаємність",
        vag: "На вашій карті з'явилися три обміни, які ви раніше ніколи не вважали економічними. Який із них зник би, якби за нього довелося платити?",
        clusters: ["Економічне розуміння", "Соціально-емоційне навчання"],
      },
      {
        stage: "Attitude",
        title: "Цінності в просторі",
        ring: "Кільце 3–4",
        workshops: ["Путівник «Картографування біорегіону» 2", "Repair Café (роль учня)"],
        experience: "Обмірковування межі біорегіону (пішохідний трансект Кільця 4); порівняльний набір даних домашнього саду; картка Особистого зобов'язання щодо якості; перша участь у Repair Café як учня/майстра",
        output: "Дані GPS-трансекту для біорегіону; дані ґрунту домашнього саду у спільноті Erdpuls; Особисте зобов'язання щодо якості; документація полагодженої речі",
        token: "Мутуалізм + Регенерація",
        vag: "Ваші садові дані показують той самий зсув pH, який ми бачимо в Зоні B після дощу. Ви вели моніторинг ґрунту, не знаючи про це. Що ще у вашому щоденному житті могло б вважатися громадянською наукою?",
        clusters: ["Екологічна грамотність", "Економічне розуміння"],
      },
      {
        stage: "Action",
        title: "Власник токенів і опора громади",
        ring: "Повний кампус",
        workshops: ["Активація власника токенів", "Repair Café (роль фасилітатора)", "Сесія якості BNE наприкінці сезону"],
        experience: "Активація статусу власника токенів; роль фасилітатора Repair Café (із навчанням); перегляд Карти цінностей-дій наприкінці сезону; за бажанням співфасилітатор у дорослих сесіях Вузла 1",
        output: "Активний рахунок власника токенів на Stellar; задокументована фасилітація Repair Café; карта порівняння РЦД наприкінці сезону",
        token: "Регенерація + Мутуалізм",
        vag: "Порівняйте вашу Карту цінностей-дій із Вузла 2 з цією. Що насправді зрушило? Спроєктуйте одну конкретну дію на наступний сезон, спрямовану на найупертіший розрив.",
        clusters: ["Економічне розуміння", "Технологічна компетентність", "Соціально-емоційне навчання"],
      },
    ],
    convergences: [
      { event: "Ринок пам'яті", with: "Старші та міжпоколіннєві", nodes: "В3", tokens: "Взаємність" },
      { event: "Repair Café", with: "Старші (ремісниче знання)", nodes: "В3–В4", tokens: "Взаємність" },
      { event: "Щорічна Асамблея мови патернів", with: "Усі групи", nodes: "В4", tokens: "Мутуалізм" },
    ],
  },

  {
    id: "elders",
    label: "Старші та міжпоколіннєві",
    emoji: "🧠",
    ages: "Вік 60+ | Різновікові",
    tagline: "Пам'ять старших як первинні дані екологічної науки",
    entryZone: "Зона E — Осередок спадщини та громади + Кільце 3",
    color: "from-amber-700 to-amber-900",
    accent: "amber",
    nodes: [
      {
        stage: "Awareness",
        title: "Ландшафт пам'ятає",
        ring: "Кільце 3",
        workshops: ["Путівник «Питання до ґрунту» 3 — Підказки для пам'яті старших"],
        experience: "Прогулянка усної історії Кільцем 3; Підказки для пам'яті старших (що тут росло? де вода текла інакше? що зникло першим?); чуттєве порівняння теперішнього ландшафту з пам'яттю",
        output: "Запис пам'яті старших (усне свідчення, транскрибоване або записане); анотована карта Кільця 3 з місцями пам'яті",
        token: "Взаємність",
        vag: "Ви щойно описали вид, якого тут більше немає. Чи це знання десь записане? Що втратилося б, якби воно залишилося лише у вашій пам'яті?",
        clusters: ["Екологічна грамотність", "Соціально-емоційне навчання"],
      },
      {
        stage: "Acknowledgment",
        title: "Пам'ять як наука",
        ring: "Кільце 3–4",
        workshops: ["Путівник «Якість BNE» 3 — Ринок пам'яті", "Карта пам'яті старших ГІС"],
        experience: "Майстер-клас Ринку пам'яті: станції знань старших у парі з молодими учасниками; Карта пам'яті старших (накладання пам'яті на поточну ГІС); порівняння з даними iNaturalist із тих самих місць",
        output: "Документація обміну на Ринку пам'яті; Карта пам'яті старших (шар ГІС); потоки токенів Взаємності",
        token: "Взаємність + Мутуалізм",
        vag: "Ваша пам'ять про вербові зарості біля струмка збіглася з тим, що показують дані ґрунту. Ваше знання весь час було науковим. Що ще ви хотіли б внести до запису?",
        clusters: ["Екологічна грамотність", "Наукове дослідження"],
      },
      {
        stage: "Attitude",
        title: "Від пам'яті до майбутнього",
        ring: "Кільце 3–4",
        workshops: ["Путівник «Токенна економіка» 3 — Ринок пам'яті", "Коло мудрості"],
        experience: "Сесія Кола мудрості: часова дуга минуле→теперішнє→майбутнє; міжпоколіннєвий діалог цінностей; Особисте зобов'язання опікунства; внесок до архіву Erzählcafé",
        output: "Запис колективної рефлексії Кола мудрості; Особисте зобов'язання опікунства; свідчення Erzählcafé",
        token: "Регенерація",
        vag: "Ви описали те, що хочете передати. Яке конкретне знання потрібно задокументувати, перш ніж воно буде втрачене, і хто та правильна людина, щоб зробити це з вами?",
        clusters: ["Соціально-емоційне навчання", "Екологічна грамотність"],
      },
      {
        stage: "Action",
        title: "Хранитель знання про місце",
        ring: "Повний біорегіон",
        workshops: ["Публікація Карти пам'яті старших як OER", "Фасилітація Кола мудрості", "Асамблея мови патернів"],
        experience: "Карту пам'яті старших опубліковано як OER (за згодою та з атрибуцією); роль фасилітатора Кола мудрості; хранитель карток патернів (називає та засвідчує патерни інших груп); участь в Асамблеї мови патернів",
        output: "Карта пам'яті старших як OER; запис фасилітованої сесії Кола мудрості; засвідчені картки патернів",
        token: "Регенерація + Мутуалізм",
        vag: "Вашу карту пам'яті тепер можуть шукати дослідники та діти, яких ви ніколи не зустрінете. Що ще має бути в цій карті?",
        clusters: ["Екологічна грамотність", "Соціально-емоційне навчання", "Технологічна компетентність"],
      },
    ],
    convergences: [
      { event: "Ринок пам'яті", with: "Діти та молодь + Дорослі", nodes: "В2", tokens: "Взаємність + Мутуалізм" },
      { event: "Repair Café", with: "Дорослі та сім'ї", nodes: "В3", tokens: "Взаємність (ремісниче знання)" },
      { event: "Щорічна Асамблея мови патернів", with: "Усі групи (як засвідчувач)", nodes: "В4", tokens: "Мутуалізм" },
    ],
  },

  {
    id: "artists",
    label: "Митці та дослідники",
    emoji: "🎨",
    ages: "Будь-який вік",
    tagline: "Очуднення та методологічна глибина як суспільне благо",
    entryZone: "Повний кампус — тривала багатосесійна резиденція",
    color: "from-violet-700 to-violet-900",
    accent: "violet",
    nodes: [
      {
        stage: "Awareness",
        title: "Уповільнитися, щоб побачити",
        ring: "Кільце 0–4, тривало",
        workshops: ["Інструментарій виявлення патернів — протокол ґетеанської глибини"],
        experience: "Повна кільцева послідовність на ґетеанській глибині: тривале спостереження одного місця (щонайменше 3 сесії, різний час доби/погода); щоденний журнал калібрування тіла в Кільці 0; чуттєва прогресія Рівнів 1→2→3, відстежувана явно; сенсорний діалог із тілом як основним інструментом",
        output: "Щоденний журнал спостережень (щонайменше 5 записів); польові нотатки ґетеанського спостереження, що розрізняють сприйняття та інтерпретацію; перший запис Сенсорного діалогу",
        token: "Співпраця",
        vag: "Що показав п'ятий візит такого, чого не показав перший? Що ваше тіло помітило, чого ваш записник спершу не зафіксував?",
        clusters: ["Екологічна грамотність", "Наукове дослідження"],
      },
      {
        stage: "Acknowledgment",
        title: "Патерни поза дисциплінами",
        ring: "Кільце 2–4",
        workshops: ["Інструментарій виявлення патернів — нестандартна картографія", "Інтеграція ГІС"],
        experience: "Сесія нестандартної картографії: картографує кампус за власними перцептивними категоріями (звук, світло, проксемічний комфорт, естетичний заряд); інтеграція шару ГІС із наявними відкритими даними; документація патернів у кількох медіа",
        output: "Нестандартна картографічна робота; щонайменше 3 названі картки патернів; внесок до поздовжньої спільноти Erdpuls",
        token: "Мутуалізм",
        vag: "Ваша звукова карта та карта pH ґрунту показують ту саму межу. Який патерн їх поєднує і кому потрібно про це знати?",
        clusters: ["Екологічна грамотність", "Технологічна компетентність", "Наукове дослідження"],
      },
      {
        stage: "Attitude",
        title: "Цінність поза ціною",
        ring: "Кільце 1–3 (громада)",
        workshops: ["Путівник «Токенна економіка» 4 — Цінність поза ціною", "Сесія громадської інтеграції"],
        experience: "Майстер-клас «Цінність поза ціною»: критичне дослідження того, що ринкова ціна не вимірює; проєктування токенів за чотирма елементами для власної практики; критичний діалог про токенізацію та видобуток; сесія громадської інтеграції щонайменше з однією іншою цільовою групою",
        output: "Письмові відповіді на чотири питання критичного діалогу; ескіз проєкту токенної економіки; запис громадської залученості",
        token: "Взаємність + Мутуалізм",
        vag: "Опишіть свою роботу як вкорінену в громаді, що зробила її можливою. Що змінюється в описі? Які обов'язки з'являються?",
        clusters: ["Економічне розуміння", "Соціально-емоційне навчання"],
      },
      {
        stage: "Action",
        title: "Резиденція як живе дослідження",
        ring: "Повний біорегіон → спільнота OER",
        workshops: ["Публікація OER", "Синтез ГІС", "Асамблея мови патернів", "За бажанням: проєктування сенсора senseBox"],
        experience: "Результат резиденції опубліковано як OER з атрибуцією Creative Commons; синтез ГІС мови патернів за всю резиденцію; презентація на Асамблеї мови патернів; за бажанням внесок у проєктування сенсорної станції",
        output: "Опублікований результат резиденції як OER; синтез мови патернів за всю резиденцію (ГІС + наратив); презентація на Асамблеї мови патернів; за бажанням документація сенсорної станції",
        token: "Регенерація + Мутуалізм",
        vag: "Вашу роботу тепер може шукати будь-хто. Яка з п'яти цільових груп найімовірніше на неї натрапить і що ви хочете, щоб вони знайшли?",
        clusters: ["Екологічна грамотність", "Наукове дослідження", "Технологічна компетентність", "Економічне розуміння"],
      },
    ],
    convergences: [
      { event: "Сесія громадської інтеграції", with: "Будь-яка інша цільова група", nodes: "В3", tokens: "Взаємність (двоспрямована)" },
      { event: "Асамблея мови патернів", with: "Усі групи (синтез ГІС)", nodes: "В4", tokens: "Мутуалізм" },
      { event: "Діалог «Цінність поза ціною»", with: "Розвиток програми", nodes: "В3", tokens: "Мутуалізм (внесок у якість)" },
    ],
  },

  {
    id: "crossborder",
    label: "Транскордонні DE/PL",
    emoji: "🇩🇪🇵🇱",
    ages: "Будь-який вік",
    tagline: "Один ландшафт, дві мови, спільне майбутнє",
    entryZone: "Зона E — тримовна, збалансований склад DE/PL",
    color: "from-rose-700 to-rose-900",
    accent: "rose",
    nodes: [
      {
        stage: "Awareness",
        title: "Один ландшафт, дві мови",
        ring: "Кільце 0–1, тримовне",
        workshops: ["Путівник «Питання до ґрунту» 5", "Тримовне калібрування Кільця 0"],
        experience: "Знайомство зі спільним льодовиковим ландшафтом як спільним ґрунтом, що передує кордону; тримовне калібрування тіла в Кільці 0; багатомовний Підрахунок життя (ті самі організми, дві мови); спостереження ґрунту з проксемічними нотатками про культурні норми дистанції",
        output: "Запис тримовного Підрахунку життя (DE/EN/PL); індивідуальні нотатки калібрування Кільця 0 власною мовою; перше міжкультурне проксемічне спостереження",
        token: "Співпраця",
        vag: "Ви щойно використали три мови, щоб описати той самий організм. Який опис відчувся вам найживішим? Чому це може мати значення для науки?",
        clusters: ["Екологічна грамотність", "Соціально-емоційне навчання"],
      },
      {
        stage: "Acknowledgment",
        title: "Рамки, що сходяться",
        ring: "Кільце 2–4",
        workshops: ["Путівник «Якість BNE» 5 — Якість без кордонів", "Транскордонний проєкт iNaturalist"],
        experience: "Порівняння рамок «Якість без кордонів»: кожна делегація представляє свою рамку освіти для сталого розвитку; визначено щонайменше 5 збігів і 2 справжні розбіжності; спільне обмірковування межі біорегіону; пов'язано транскордонні дані громадянської науки",
        output: "Матриця порівняння рамок; транскордонна пропозиція межі біорегіону; спостереження iNaturalist з обох боків, пов'язані у спільному проєкті",
        token: "Мутуалізм + Взаємність",
        vag: "Ваші дві рамки погодилися на тому самому принципі, але назвали його по-різному. Що було втрачено у відмінності назв? Що означало б діяти за цим принципом разом?",
        clusters: ["Екологічна грамотність", "Соціально-емоційне навчання", "Наукове дослідження"],
      },
      {
        stage: "Attitude",
        title: "Проєктування транскордонної взаємності",
        ring: "Зона E — спільна трапеза",
        workshops: ["Путівник «Токенна економіка» 5 — Одна економіка, дві мови", "Спільна трапеза"],
        experience: "Майстер-клас проєктування транскордонної токенної економіки; культурні проксемічні відмінності явно названо як вхідні дані проєктування; спільна трапеза як утілена реципрокна економіка; двостороннє Особисте зобов'язання щодо якості",
        output: "Проєктний документ транскордонної токенної економіки (двомовний); документація спільної трапези; двостороннє зобов'язання (підписане з обох боків)",
        token: "Співпраця + Взаємність + Мутуалізм",
        vag: "Трапеза перетнула кордон, бо ви перетнули кордон першими. Що ще, що наразі зупиняється на кордоні, ви хотіли б побачити таким, що його перетинає?",
        clusters: ["Економічне розуміння", "Соціально-емоційне навчання"],
      },
      {
        stage: "Action",
        title: "Партнерство як інфраструктура",
        ring: "Повний біорегіон + інституційний",
        workshops: ["OER транскордонних принципів якості", "Пропозиція партнерства INTERREG", "Реципрокний обмін фасилітацією"],
        experience: "Спільний документ принципів якості (двомовний OER); формальна пропозиція партнерства для фінансування INTERREG або двостороннього; проєкт транскордонної мережі громадянської науки; реципрокна фасилітація (DE фасилітує в Польщі; PL фасилітує в Німеччині)",
        output: "Двомовний документ принципів якості як OER; рамка пропозиції партнерства; протокол мережі громадянської науки; задокументована подія реципрокної фасилітації",
        token: "Регенерація + Мутуалізм",
        vag: "Тепер ви маєте робочий документ, мережу та обмін фасилітацією. Який один конкретний бар'єр залишається? Хто в кімнаті має владу його подолати?",
        clusters: ["Економічне розуміння", "Соціально-емоційне навчання", "Технологічна компетентність"],
      },
    ],
    convergences: [
      { event: "Транскордонний проєкт iNaturalist", with: "Митці та дослідники (шар ГІС)", nodes: "В2", tokens: "Мутуалізм" },
      { event: "Реципрокний обмін фасилітацією", with: "Будь-яка фасилітована група", nodes: "В4", tokens: "Регенерація" },
      { event: "Асамблея мови патернів", with: "Усі групи", nodes: "В4", tokens: "Мутуалізм" },
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
        {STAGE_LABELS[node.stage]}
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
            {STAGE_LABELS[node.stage]} · {node.ring}
          </div>
          <div className="text-gray-900 font-bold text-base leading-tight">{node.title}</div>
        </div>
      </div>

      {/* Workshops */}
      <div>
        <div className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1">Пов'язані майстер-класи</div>
        <div className="flex flex-wrap gap-1">
          {node.workshops.map((w, i) => (
            <span key={i} className="bg-white border border-gray-200 text-gray-700 text-xs px-2 py-0.5 rounded-full">{w}</span>
          ))}
        </div>
      </div>

      {/* Core experience */}
      <div>
        <div className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1">Основний досвід</div>
        <div className="text-sm text-gray-700 leading-relaxed">{node.experience}</div>
      </div>

      {/* Output */}
      <div className="bg-white rounded-xl border border-gray-100 p-3">
        <div className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1">Результат / доказовий артефакт</div>
        <div className="text-sm text-gray-700">{node.output}</div>
      </div>

      {/* Token + VAG */}
      <div className="grid grid-cols-2 gap-3">
        <div className={`rounded-xl p-3 ${sc.light} border ${sc.border}`}>
          <div className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1">Зароблений токен</div>
          <div className={`text-sm font-bold ${sc.text}`}>{node.token}</div>
        </div>
        <div className="rounded-xl p-3 bg-white border border-yellow-200">
          <div className="text-xs font-bold text-yellow-700 uppercase tracking-wide mb-1">Компетентнісні кластери</div>
          <div className="flex flex-wrap gap-1">
            {node.clusters.map((c, i) => (
              <span key={i} className="text-xs bg-yellow-50 border border-yellow-200 text-yellow-800 px-1.5 py-0.5 rounded">{c}</span>
            ))}
          </div>
        </div>
      </div>

      {/* VAG Bridge */}
      <div className="bg-amber-50 border border-amber-200 rounded-xl p-3">
        <div className="text-xs font-bold text-amber-700 uppercase tracking-wide mb-1">Місток розриву між цінностями та діями</div>
        <div className="text-sm text-amber-900 italic leading-relaxed">"{node.vag}"</div>
      </div>
    </div>
  );
}

function ConvergencePanel({ convergences }) {
  return (
    <div className="mt-4 space-y-2">
      <div className="text-xs font-bold text-gray-500 uppercase tracking-wide">Зони міжгрупової конвергенції</div>
      {convergences.map((c, i) => (
        <div key={i} className={`rounded-xl border p-3 ${CONVERGENCE_COLOR}`}>
          <div className="flex items-center justify-between">
            <div className="font-semibold text-sm">{c.event}</div>
            <div className="text-xs bg-violet-200 text-violet-800 px-2 py-0.5 rounded-full">{c.nodes}</div>
          </div>
          <div className="text-xs mt-1">З ким: <span className="font-medium">{c.with}</span></div>
          <div className="text-xs mt-0.5">Токени: <span className="font-medium">{c.tokens}</span></div>
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
          <span className="text-xs text-gray-600 font-medium">{STAGE_LABELS[stage]}</span>
        </div>
      ))}
      <div className="flex items-center gap-1.5">
        <div className="w-4 h-4 rounded-full bg-violet-400" />
        <span className="text-xs text-gray-600 font-medium">Зона конвергенції</span>
      </div>
    </div>
  );
}

// ── Token legend ──────────────────────────────────────────────────────────────
const TOKEN_DESC = {
  "Співпраця": "Спільна дія з іншими",
  "Взаємність": "Двоспрямований обмін цінністю",
  "Мутуалізм": "Вигода, що поширюється на ширшу громаду",
  "Регенерація": "Відчутне екологічне чи соціальне поліпшення",
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
            Erdpuls · Center for Sustainability Literacy, Citizen Science & Reciprocal Economics
          </div>
          <h1 className="text-2xl font-bold">Карти навчальних траєкторій</h1>
          <p className="text-sm text-emerald-200 mt-1">
            П'ять траєкторій за цільовими групами · глибина 4A-траєкторії · питання-містки розриву між цінностями та діями · інтеграція токенної економіки
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
            <div className="font-bold mb-1">Зона входу</div>
            <div>{group.entryZone}</div>
          </div>
        </div>

        {/* Pathway diagram + node detail */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

          {/* Left: pathway map */}
          <div className="lg:col-span-1 bg-white rounded-2xl border border-gray-200 p-5 space-y-4">
            <div className="text-xs font-bold text-gray-500 uppercase tracking-wide">Карта траєкторії</div>

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
                      <div className={`text-xs font-bold ${sc.text}`}>{STAGE_LABELS[n.stage]}</div>
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
              {showConvergence ? "▲ Сховати" : "▼ Показати"} зони конвергенції
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
          <div className="text-xs font-bold text-gray-500 uppercase tracking-wide">Легенда стадій</div>
          <Legend />
          <div className="pt-2 border-t border-gray-100">
            <button
              onClick={() => setShowTokens(!showTokens)}
              className="text-xs font-semibold text-gray-600 hover:text-gray-900"
            >
              {showTokens ? "▲ Сховати" : "▼ Показати"} Довідник токенної економіки
            </button>
            {showTokens && <div className="mt-3"><TokenLegend /></div>}
          </div>
        </div>

        {/* Footer */}
        <div className="text-center text-xs text-gray-400 pb-4">
          <div>© 2025–2026 Erdpuls · CC BY-SA 4.0</div>
          <div className="mt-0.5">erdpuls@ubec.network · https://erdpuls.ubec.network</div>
        </div>
      </div>
    </div>
  );
}
