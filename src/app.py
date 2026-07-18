# src/app.py
import streamlit as st
import re
from analyzer import analyze_noun_properties
from transliterate import latin_to_cyrillic
from cases import genitive, accusative, dative, instrumental, locative, vocative

# UI Styling Configuration / Конфігурація інтерфейсу
st.set_page_config(page_title="UA Grammar Engine", page_icon="🇺🇦", layout="centered")

st.title("🇺🇦 Ukrainian Grammar Rules Engine")
st.markdown("### Algorithmic Morphological Mutations / Детермінований Двигун")
st.write("---")

# Navigation Mappings
CASE_DISPLAY_MAP = {
    "Nominative (Називний)": "nominative",
    "Genitive (Родовий)": "genitive",
    "Accusative (Знахідний)": "accusative",
    "Dative (Давальний)": "dative",
    "Instrumental (Орудний)": "instrumental",
    "Locative (Місцевий)": "locative",
    "Vocative (Кличний)": "vocative"
}

# Sidebar settings for manual testing configurations
st.sidebar.header("Metadata Flags")
override_animate = st.sidebar.checkbox("Force Animate / Тварина чи Людина", value=False)

# UI Input Selectors
word_input = st.text_input("Enter base noun (Phonetic Latin or Cyrillic):", value="kniha")
selected_case_display = st.selectbox("Select Target Case:", list(CASE_DISPLAY_MAP.keys()))
target_case = CASE_DISPLAY_MAP[selected_case_display]

if word_input:
    word = word_input.strip()

    # Run the exact master input validation script sequence
    if re.match(r"^[A-Za-z']+$", word):
        word = latin_to_cyrillic(word)
        word = word.replace('гі', 'ги').replace('кі', 'ки').replace('хі', 'хи')

    if re.match(r"^[А-Яа-яЄєІіЇїҐґ']+$", word):
        props = analyze_noun_properties(word)
        if override_animate:
            props["is_animate"] = True

        # Deterministic routing logic
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

        # Display Results
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Parsed Base Token", value=word)
        with col2:
            st.metric(label="Calculated Mutation", value=output)

        # Verification Expanders
        with st.expander("View Rule Evaluation Context"):
            st.json({
                "Inferred Gender": props["gender"],
                "Inferred Stem Type": props["stem_type"],
                "Active Animacy Flag": props["is_animate"]
            })
    else:
        st.error("Invalid characters. Please type using standard Latin phonetics or Cyrillic keys.")