# src/cases/genitive.py

###############################################################################
# GENITIVE CASE MODULE / МОДУЛЬ РОДОВОГО ВІДМІНКА
#
# EN: Rules for transforming a base noun into its Genitive singular form.
# UK: Правила трансформації іменника в форму родового відмінка однини.
###############################################################################

def apply_rules(word: str, props: dict) -> str:
    """
    EN: Executes structural mutations based on gender and stem parameters.
    UK: Виконує структурні зміни на основі роду та типу основи.
    """
    gender = props["gender"]
    stem = props["stem_type"]

    # -------------------------------------------------------------------------
    # EN: Strategy F: Feminine Rules (Ends in а/я -> drops vowel for и/і)
    # UK: Стратегія Ж: Жіночий рід (Закінчується на а/я -> змінюється на и/і)
    # -------------------------------------------------------------------------
    if gender == "F":
        base = word[:-1]  # EN: Strip last char / UK: Видаляємо останню літеру
        return base + "і" if stem == "soft" else base + "и"

    # -------------------------------------------------------------------------
    # EN: Strategy M/N: Masculine & Neuter Rules (Appends -а / -я)
    # UK: Стратегія Ч/С: Чоловічий та Середній рід (Додається -а / -я)
    # -------------------------------------------------------------------------
    elif gender in ["M", "N"]:
        # EN: If word ends in a soft marker or structural vowel, strip it first
        # UK: Якщо слово закінчується на м'який знак або голосну, спочатку видаляємо її
        base = word[:-1] if word[-1] in ['ь', 'й', 'о', 'е'] else word

        return base + "я" if stem == "soft" else base + "а"

    return word