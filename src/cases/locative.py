# src/cases/locative.py

def apply_rules(word: str, props: dict) -> str:
    gender, stem = props["gender"], props["stem_type"]

    if gender == "F":
        base = word[:-1]
        if base.endswith('к'):
            return base[:-1] + "ці"
        elif base.endswith('г'):
            return base[:-1] + "зі"
        elif base.endswith('х'):
            return base[:-1] + "сі"
        return base + "і"

    elif gender in ["M", "N"]:
        # Match words ending in k or ok variants to structural -у
        if word.endswith(('к', 'ок', 'ик')):
            return word + "у"
        base = word[:-1] if word[-1] in ['ь', 'й', 'о', 'е'] else word
        return base + "і"

    return word