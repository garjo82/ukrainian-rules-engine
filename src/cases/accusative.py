# src/cases/accusative.py

###############################################################################
# ACCUSATIVE CASE MODULE / МОДУЛЬ ЗНАХІДНОГО ВІДМІНКА
#
# EN: Rules for transforming a base noun into its Accusative singular form.
# UK: Правила трансформації іменника в форму знахідного відмінка однини.
###############################################################################

from cases import genitive


def apply_rules(word: str, props: dict) -> str:
    """
    EN: Executes direct object mutations based on gender, stem, and animacy.
    UK: Виконує зміни знахідного відмінка на основі роду, основи та істоти.
    """
    gender = props["gender"]
    stem = props["stem_type"]
    is_animate = props["is_animate"]

    # -------------------------------------------------------------------------
    # EN: Strategy F: Feminine Rules (а -> у, я -> ю)
    # UK: Стратегія Ж: Жіночий рід (а -> у, я -> ю)
    # -------------------------------------------------------------------------
    if gender == "F":
        base = word[:-1]
        return base + "ю" if stem == "soft" else base + "у"

    # -------------------------------------------------------------------------
    # EN: Strategy M: Masculine Rules (Depends entirely on Animacy)
    # UK: Стратегія Ч: Чоловічий рід (Повністю залежить від категорії істоти)
    # -------------------------------------------------------------------------
    elif gender == "M":
        if is_animate:
            # EN: Animate Masculine morphs identically to the Genitive case
            # UK: Назви істот чоловічого роду змінюються так само, як у родовому
            return genitive.apply_rules(word, props)
        else:
            # EN: Inanimate Masculine completely retains its Nominative base
            # UK: Назви неістот чоловічого роду зберігають початкову форму
            return word

    # -------------------------------------------------------------------------
    # EN: Strategy N: Neuter Rules (Always retains Nominative base)
    # UK: Стратегія С: Середній рід (Завжди зберігає початкову форму)
    # -------------------------------------------------------------------------
    elif gender == "N":
        return word

    return word