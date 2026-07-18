# src/cases/vocative.py

def apply_rules(word: str, props: dict) -> str:
    gender, stem = props["gender"], props["stem_type"]

    if gender == "F":
        base = word[:-1]
        return base + "ю" if stem == "soft" else base + "о"

    elif gender == "M":
        if word.endswith(('к', 'г', 'х')):
            return word + "у"
        base = word[:-1] if word[-1] in ['ь', 'й'] else word
        return base + "ю" if stem == "soft" else base + "е"

    return word