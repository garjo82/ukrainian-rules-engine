# src/analyzer.py

def analyze_noun_properties(word: str) -> dict:
    """
    EN: Analyzes a raw Cyrillic string to extract structural metadata.
    UK: Аналізує кириличний рядок для визначення структурних метаданих.
    """
    word = word.strip().lower()
    last_char = word[-1] if word else ""

    # EN: Default state: Masculine, Hard Stem, Inanimate
    # UK: Початковий стан: Чоловічий рід, тверда основа, неістота
    props = {
        "gender": "M",
        "stem_type": "hard",
        "is_animate": False
    }

    # EN: Layer 1: Detect Feminine Structural Class (Ends in а/я)
    # UK: Рівень 1: Визначення жіночого роду (Закінчується на а/я)
    if last_char in ['а', 'я']:
        props["gender"] = "F"
        props["stem_type"] = "soft" if last_char == 'я' else "hard"

    # EN: Layer 2: Detect Neuter Structural Class (Ends in о/е/я)
    # UK: Рівень 2: Визначення середнього роду (Закінчується на о/е/я)
    elif last_char in ['о', 'е', 'я']:
        props["gender"] = "N"
        props["stem_type"] = "soft" if last_char == 'е' else "hard"

    # EN: Layer 3: Refine Masculine Stem Types (Ends in soft sign / й)
    # UK: Рівень 3: Уточнення основи чоловічого роду (Закінчується на ь/й)
    elif last_char in ['ь', 'й']:
        props["gender"] = "M"
        props["stem_type"] = "soft"

    return props