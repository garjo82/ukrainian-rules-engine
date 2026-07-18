# Ukrainian Case Constructor / Конструктор відмінків української мови

A deterministic, rule-based computational engine designed to automatically calculate singular noun inflections in Ukrainian from first principles.

🔗 **Live Web Application:** [ukrainian-case-constructor.streamlit.app](https://ua-case-constructor.streamlit.app/)

---

## English Documentation

### 1. Instructions for Use
* **Input Entry:** Enter a singular base noun in the text input field. The system supports native Cyrillic characters (e.g., `книга`) as well as phonetic Latin script transliteration (e.g., `kniha`).
* **Automated Phonetic Guards:** If inputting phonetic Latin, the engine maps characters automatically and applies vowel-harmony guards (such as correcting `hi/ki/khi` combinations into appropriate native sound patterns like `ги/ки/хи`).
* **Case Selection:** Select the target grammatical case from the dropdown selector (Nominative, Genitive, Accusative, Dative, Instrumental, Locative, or Vocative).
* **Animacy Toggle:** For grammatical cases where animacy dictates noun endings (like the Accusative case), use the **Force Animate** sidebar toggle to manually flag the noun as a living being (human/animal) if the inference engine defaults to an inanimate state.
* **Diagnostics Panel:** Expand the "View Rule Evaluation Context" dropdown at the bottom to see the internal state machine variables (Inferred Gender, Stem Type, and Animacy status).

### 2. Logic and Design Choices
* **Dictionaryless Implementation:** Unlike traditional natural language processing tools that rely on massive database lookups, static dictionaries, or machine learning guesswork, this engine executes pure algorithmic morphological transformations. This algorithmic approach can serve as a framework for highly analytical learners to construct/deconstruct cases in real time, rather than having to rely on memorizing Ukrainian case tables.
* **First-Principles Linguistics:** The system isolates the noun's structural stem, automatically classifies its gender and stem property (hard vs. soft), and dynamically routes the token through deterministic logic loops.
* **Sound Mutation Pipelines:** Linguistic phenomena such as velar consonant mutations ($k \rightarrow ts$, $h \rightarrow s$, $g \rightarrow z$) and soft-vowel transitions are calculated entirely via functional code, mimicking the true phonetic laws of the language.

### 3. Current Limitations
* **Number Constraints:** The system is currently strictly limited to **singular** noun paradigms. Plural inflections are not yet processed.
* **Irregular Noun Exceptions:** High-frequency irregular nouns, unique loanwords, or nouns undergoing systemic vowel fleeting (e.g., *день* $\rightarrow$ *дня*, where the inner vowel drops out) may display irregular endings, as they sit outside standard rule paradigms.
* **Proper Nouns & Surnames:** While basic nouns work seamlessly, specialized regional proper nouns or highly complex surname inflections are not yet explicitly isolated.

### 4. Planned Feature Updates
* **Plural Paradigm Engine:** Expansion of the architectural routing loops to fully calculate plural case forms across all genders.
* **Fleeting Vowel Detection:** Algorithmic identification of shifting root vowels (like the $o/e \rightarrow i$ transitions or complete vowel dropouts) during stem isolation.
* **Expanded Parts of Speech:** Gradual integration of adjective agreement modules to allow users to decline entire noun-adjective phrases simultaneously.
* **Case Construction Visualization:** A graphical visualization to replace the rule evaluation context, which will provide learners with a visual mapping for case construction and deconstruction.

---

## Українська документація

### 1. Інструкція з використання
* **Введення слова:** Введіть іменник уднині у текстове поле. Система підтримує як рідну кирилицю (наприклад, `книга`), так і транслітерацію фонетичною латиницею (наприклад, `kniha`).
* **Автоматичні фонетичні фільтри:** При введенні латиницею двигун автоматично замінює символи та застосовує правила гармонії голосних (наприклад, коригує комбінації `hi/ki/khi` на відповідні звукові моделі `ги/ки/хи`).
* **Вибір відмінка:** Оберіть цільовий граматичний відмінок зі спадного списку (Називний, Родовий, Знахідний, Давальний, Орудний, Місцевий або Кличний).
* **Перемикач категорії істоти:** Для відмінків, де категорія істоти впливає на закінчення (наприклад, Знахідний відмінок), використовуйте прапорець **"Force Animate"** на бічній панелі, щоб вручну позначити іменник як живу істоту (людину чи тварину), якщо система автоматично визначила його як неживий предмет.
* **Діагностична панель:** Розгорніть меню "Переглянути контекст аналізу правил" внизу, щоб побачити внутрішні змінні стану двигуна (визначений рід, тип основи та категорію істоти).

### 2. Логіка та архітектурні рішення
* **Робота без словника:** На відміну від традиційних інструментів обробки природної мови, які покладаються на величезні бази даних, статичні словники або машинні прогнози, цей двигун виконує суто алгоритмічні морфологічні трансформації. Такий алгоритмічний підхід може слугувати основою для учнів з аналітичним складом мислення, дозволяючи їм конструювати та деконструювати відмінки в режимі реального часу замість того, щоб покладатися на зазубрювання таблиць відмінювання української мови.
* **Лінгвістика перших принципів:** Система ізолює структурну основу іменника, автоматично класифікує його рід та тип основи (тверда чи м'яка), а потім динамічно спрямовує токен через детерміновані логічні цикли.
* **Чергування звуків:** Лінгвістичні явища, такі як чергування приголосних ($k \rightarrow ts$, $h \rightarrow s$, $g \rightarrow z$) та переходи м'яких голосних, розраховуються повністю за допомогою функціонального коду, відтворюючи реальні фонетичні закони мови.

### 3. Поточні обмеження
* **Обмеження числа:** Наразі система суворо обмежена парадигмами іменників у **однині**. Форми множини поки що не обробляються.
* **Винятки та нерегулярні іменники:** Нерегулярні іменники з високою частотою вживання, унікальні запозичені слова або іменники з випадними голосними (наприклад, *день* $\rightarrow$ *дня*) можуть відображатися некоректно, оскільки вони виходять за межі стандартних правил.
* **Власні назви та прізвища:** Хоча загальні назви працюють чудово, специфічні власні назви або складні флексії прізвищ наразі не виділені в окремі правила.

### 4. Плановані оновлення функцій
* **Модуль множини:** Розширення архітектурних циклів маршрутизації для повного розрахунку відмінкових форм множини для всіх родів.
* **Визначення випадних голосних:** Алгоритмічне виявлення змінних кореневих голосних (таких як переходи $o/e \rightarrow i$ або повне випадіння голосного) під час ізоляції основи.
* **Узгодження з іншими частинами мови:** Поступова інтеграція модулів узгодження прикметників, що дозволить користувачам відмінювати цілі словосполучення (іменник + прикметник) одночасно.
* **Візуалізація конструювання відмінків:** Графічна візуалізація, яка замінить поточний контекст аналізу правил. Вона надасть учням наочну карту для візуального моделювання процесів конструювання та деконструювання відмінків.