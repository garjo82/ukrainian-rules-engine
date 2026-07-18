# src/cases/instrumental.py

def apply_rules(word: str, props: dict) -> str:
    gender, stem = props["gender"], props["stem_type"]

    if gender == "F":
        base = word[:-1]
        return base + "ею" if stem == "soft" else base + "ою"

    elif gender in ["M", "N"]:
        base = word[:-1] if word[-1] in ['ь', 'й', 'о', 'е'] else word
        return base + "ем" if stem == "soft" else base + "ом"

    return word