# src/main.py
import re
from analyzer import analyze_noun_properties
from cases import genitive
from transliterate import latin_to_cyrillic


def validate_input(user_input: str):
    """
    EN: Validates string counts and processes script translation if Latin is used.
    UK: Перевіряє введення та конвертує латиницю, якщо це необхідно.
    """
    tokens = user_input.strip().split()
    if len(tokens) != 2:
        print(" [EN] Error: Enter exactly two parameters: [Word] [Case]")
        print(" [UK] Помилка: Введіть рівно два параметри: [Слово] [Відмінок]")
        return None

    word, target_case = tokens[0], tokens[1].lower()

    # -------------------------------------------------------------------------
    # EN: Parse Word Token (Latin or Cyrillic)
    # UK: Обробка токена слова (Латиниця або Кирилиця)
    # -------------------------------------------------------------------------
    if re.match(r"^[A-Za-z']+$", word):
        word = latin_to_cyrillic(word)
    elif not re.match(r"^[А-Яа-яЄєІіЇїҐґ']+$", word):
        print(" [EN] Error: Word token must use Cyrillic characters or phonetic Latin.")
        print(" [UK] Помилка: Слово має бути написане кирилицею або фонетичною латиницею.")
        return None

    # -------------------------------------------------------------------------
    # EN: Parse and Normalize Case Token (Supports English or Cyrillic input)
    # UK: Обробка та нормалізація токена відмінка (Підтримка англійської або кирилиці)
    # -------------------------------------------------------------------------
    genitive_aliases = ["genitive", "родовий", "родового", "род"]

    if target_case in genitive_aliases:
        normalized_case = "genitive"
    else:
        print(f" [EN] Error: Unsupported case string '{target_case}'. Try: 'genitive' or 'родовий'")
        print(f" [UK] Помилка: Непідтримувана назва відмінка '{target_case}'. Спробуйте: 'genitive' або 'родовий'")
        return None

    return word, normalized_case


def main():
    print("=================================================================")
    print("  Ukrainian Algorithmic Rules Engine / Алгоритмічний Двигун")
    print("  Accepts standard Cyrillic or phonetic Latin inputs!")
    print("  Type 'exit' / 'вихід' to close program.")
    print("=================================================================")

    while True:
        try:
            prompt_text = "\nEnter word and case / Введіть слово та відмінок (pasport родовий): "
            raw_input = input(prompt_text)

            if raw_input.strip().lower() in ['exit', 'вихід']:
                break

            validated = validate_input(raw_input)
            if not validated:
                continue

            word, target_case = validated
            props = analyze_noun_properties(word)

            if target_case == "genitive":
                output = genitive.apply_rules(word, props)

            print(f" -> Internal Token / Токен: {word}")
            print(f" -> Mapping / Аналіз: Gender/Рід={props['gender']} | Stem/Основа={props['stem_type']}")
            print(f" -> Output / Результат: {output}")

        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()