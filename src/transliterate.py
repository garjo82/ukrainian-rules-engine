# src/transliterate.py

# EN: Corrected phonetic mapping to handle standard 'h' and common 'g' as 'г'
# UK: Виправлена фонетична карта: 'h' та 'g' тепер відображаються як стандартна 'г'
TRANSLIT_MAP = {
    'ch': 'ч', 'sh': 'ш', 'shch': 'щ', 'kh': 'х', 'ts': 'ц',
    'ya': 'я', 'yu': 'ю', 'ye': 'є', 'yi': 'ї', 'zh': 'ж',
    'a': 'а', 'b': 'б', 'v': 'в', 'h': 'г', 'g': 'г', 'd': 'д',  # EN: Both h and g route to г
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

    # EN: Sort keys by length so longer sequences match first
    # UK: Сортуємо за довжиною для коректного розпізнавання багатолітерних фонем
    sorted_keys = sorted(TRANSLIT_MAP.keys(), key=len, reverse=True)

    for key in sorted_keys:
        result = result.replace(key, TRANSLIT_MAP[key])

    return result