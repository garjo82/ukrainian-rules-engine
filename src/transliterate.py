# src/transliterate.py

# EN: Latin to Cyrillic phonetic mapping dictionary
# UK: Словник фонетичної транслітерації з латиниці на кирилицю
TRANSLIT_MAP = {
    'ch': 'ч', 'sh': 'ш', 'shch': 'щ', 'kh': 'х', 'ts': 'ц',
    'ya': 'я', 'yu': 'ю', 'ye': 'є', 'yi': 'ї', 'zh': 'ж',
    'a': 'а', 'b': 'б', 'v': 'в', 'h': 'г', 'g': 'ґ', 'd': 'д',
    'e': 'е', 'z': 'з', 'y': 'и', 'i': 'і', 'k': 'к', 'l': 'л',
    'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'r': 'р', 's': 'с',
    't': 'т', 'u': 'у', 'f': 'ф', "'": "'"
}


def latin_to_cyrillic(text: str) -> str:
    """
    EN: Converts phonetic Latin input into Cyrillic text by descending token length.
    UK: Конвертує фонетичне латинське введення в кирилицю.
    """
    result = text.lower()

    # EN: Sort keys by length so longer sequences like 'shch' match before 'sh' or 'c'
    # UK: Сортуємо за довжиною, щоб 'shch' розпізнавалося раніше ніж 'sh'
    sorted_keys = sorted(TRANSLIT_MAP.keys(), key=len, reverse=True)

    for key in sorted_keys:
        result = result.replace(key, TRANSLIT_MAP[key])

    return result