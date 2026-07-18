# src/cases/dative.py

def apply_rules(word: str, props: dict) -> str:
    gender, stem = props["gender"], props["stem_type"]

    if gender == "F":
        base = word[:-1]
        # Velar Mutations / Чергування приголосних
        if base.endswith('к'):
            return base[:-1] + "ці"
        elif base.endswith('г'):
            return base[:-1] + "зі"
        elif base.endswith('х'):
            return base[:-1] + "сі"
        return base + "і"

    elif gender in ["M", "N"]:
        base = word[:-1] if word[-1] in ['ь', 'й', 'о', 'е'] else word
        return base + "еві" if stem == "soft" else base + "у"

    return word