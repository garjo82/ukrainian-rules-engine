# src/app.py
import streamlit as st
import re
from analyzer import analyze_noun_properties
from transliterate import latin_to_cyrillic
from cases import genitive, accusative, dative, instrumental, locative, vocative

# UI Styling Configuration / Конфігурація інтерфейсу
st.set_page_config(page_title="UA Case Constructor", page_icon="🇺🇦", layout="centered")

# 1. Main Title Header (English & Native Cyrillic)
st.title("🇺🇦 Ukrainian Case Constructor")
st.markdown("### Конструктор відмінків української мови")

# Concise Subtitle Context
st.markdown(
    "*A deterministic system that builds singular noun endings from first principles without a dictionary database.*")
st.write("---")

# Navigation Mappings
CASE_DISPLAY_MAP = {
    "Nominative (Називний відмінок)": "nominative",
    "Genitive (Родовий відмінок)": "genitive",
    "Accusative (Знахідний відмінок)": "accusative",
    "Dative (Давальний відмінок)": "dative",
    "Instrumental (Орудний відмінок)": "instrumental",
    "Locative (Місцевий відмінок)": "locative",
    "Vocative (Кличний відмінок)": "vocative"
}

# Sidebar settings with bilingual context
st.sidebar.header("Metadata Configuration / Конфігурація")
override_animate = st.sidebar.checkbox("Force Animate / Назва істоти (Людина / Тварина)", value=False)

# 2. Interactive App Inputs (With Clean Bilingual Labels)
word_input = st.text_input(
    "Enter base noun (Phonetic Latin or Cyrillic) / Введіть іменник (Латиницею або Кириличницею):", value="kniha")
selected_case_display = st.selectbox("Select Target Case / Оберіть цільовий відмінок:", list(CASE_DISPLAY_MAP.keys()))
target_case = CASE_DISPLAY_MAP[selected_case_display]

if word_input:
    word = word_input.strip()

    # Execute phonetic mappings and vowel guards
    if re.match(r"^[A-Za-z']+$", word):
        word = latin_to_cyrillic(word)
        word = word.replace('гі', 'ги').replace('кі', 'ки').replace('хі', 'хи')

    if re.match(r"^[А-Яа-яЄєІіЇїҐґ']+$", word):
        props = analyze_noun_properties(word)
        if override_animate:
            props["is_animate"] = True

        # Route logic
        if target_case == "nominative":
            output = word
        elif target_case == "genitive":
            output = genitive.apply_rules(word, props)
        elif target_case == "accusative":
            output = accusative.apply_rules(word, props)
        elif target_case == "dative":
            output = dative.apply_rules(word, props)
        elif target_case == "instrumental":
            output = instrumental.apply_rules(word, props)
        elif target_case == "locative":
            output = locative.apply_rules(word, props)
        elif target_case == "vocative":
            output = vocative.apply_rules(word, props)

        # 3. Dynamic Results Display Area
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Parsed Base Token / Початкова форма", value=word)
        with col2:
            st.metric(label="Calculated Mutation / Змінена форма", value=output)

        # 4. Decoupled Diagnostic Expanders (Separate English and Ukrainian Blocks)
        with st.expander("View Rule Evaluation Context / Переглянути контекст аналізу правил"):

            # Map values to native equivalents for translation panels
            gender_ua = {"M": "Чоловічий (M)", "F": "Жіночий (F)", "N": "Середній (N)"}.get(props["gender"],
                                                                                            props["gender"])
            stem_ua = {"hard": "Тверда (Hard)", "soft": "М’яка (Soft)"}.get(props["stem_type"], props["stem_type"])

            st.markdown("#### 🇬🇧 English Engine Analysis")
            st.json({
                "Inferred Gender": props["gender"],
                "Inferred Stem Type": props["stem_type"],
                "Is Animate Object": props["is_animate"]
            })

            st.markdown("#### 🇺🇦 Український аналіз двигуна")
            st.json({
                "Визначений рід": gender_ua,
                "Тип основи": stem_ua,
                "Категорія істоти": "Так (True)" if props["is_animate"] else "Ні (False)"
            })

        # 5. Explanatory Context Footer with Repository Reference
        st.write("---")
        st.markdown("""
        **How this works / Як це працює:**  
        Instead of looking up words in a dictionary database, this app applies linguistic structural rules directly to the word's stem. 
        It automatically detects the gender and stem type, then calculates changes—like soft vowel transitions or velar sound shifts ($k \\rightarrow ts$)—using pure logic loops.

        *Замість пошуку слів у базі даних, цей додаток застосовує правила безпосередньо до основи слова. Він автоматично визначає рід і тип основи, а потім розраховує зміни за допомогою чистих логічних циклів.*

        ---
        📂 **Open Source / Вихідний код:**  
        The complete modular architecture, bilingual codebase, and deterministic case modules are completely open-source. Feel free to explore the structural engine design directly on GitHub:  
        [GitHub Repository: ukrainian-case-constructor](https://github.com) *(Replace this link with your actual repository URL)*
        """)

    else:
        st.error("Invalid character set layout. / Некоректний набір символів.")