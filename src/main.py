# src/main.py
import re
from analyzer import analyze_noun_properties
from transliterate import latin_to_cyrillic
from cases import genitive, accusative, dative, instrumental, locative, vocative

# EN: Universal routing translation map for foreign/native inputs
# UK: Універсальна карта маршрутизації для іншомовних та рідних значень
CASE_ROUTING_MAP = {
    "genitive": "genitive", "родовий": "genitive", "родового": "genitive", "род": "genitive",
    "accusative": "accusative", "знахідний": "accusative", "знахідного": "accusative", "знах": "accusative",
    "dative": "dative", "давальний": "dative", "давального": "dative", "дав": "dative",
    "instrumental": "instrumental", "орудний": "instrumental", "орудного": "instrumental", "оруд": "instrumental",
    "locative": "locative", "місцевий": "locative", "місцевого": "locative", "місц": "locative",
    "vocative": "vocative", "кличний": "vocative", "кличного": "vocative", "клич": "vocative"
}


def validate_and_route(user_input: str):
    """
    EN: Standardizes raw input tokens, resolves scripts, and matches target case execution tracks.
    UK: Стандартизує токени введення, вирішує алфавіт та підбирає трек виконання відмінка.
    """
    tokens = user_input.strip().split()
    if len(tokens) != 2:
        print(" [EN] Error: Enter exactly two parameters: [Word] [Case]")
        print(" [UK] Помилка: Введіть рівно два параметри: [Слово] [Відмінок]")
        return None

    word, raw_case = tokens[0], tokens[1].lower()

    # EN: Process phonetic Latin input tracking rules
    # UK: Обробка правил фонетичного латинського введення
    if re.match(r"^[A-Za-z']+$", word):
        word = latin_to_cyrillic(word)
        # EN: Localized vowel guard: enforce native hard stems after velars (hi/ki/khi -> ги/ки/хи)
        # UK: Локальний захист голосних: примусова тверда основа після задньоязикових
        word = word.replace('гі', 'ги').replace('кі', 'ки').replace('хі', 'хи')
    elif not re.match(r"^[А-Яа-яЄєІіЇїҐґ']+$", word):
        print(" [EN] Error: Word must use Cyrillic or phonetic Latin layout.")
        print(" [UK] Помилка: Слово має бути написане кирилицею або фонетичною латиницею.")
        return None

    if raw_case not in CASE_ROUTING_MAP:
        print(f" [EN] Error: Unsupported case key '{raw_case}'.")
        print(f" [UK] Помилка: Непідтримуваний відмінок '{raw_case}'.")
        return None

    return word, CASE_ROUTING_MAP[raw_case]


def main():
    print("=================================================================")
    print("  Ukrainian Algorithmic Rules Engine v2.1 / Модульний Двигун")
    print("  Inputs: [Phonetic Latin / Кириличне Слово] [Case / Відмінок]")
    print("  Example: 'kniha dative' or 'паспорт родовий'")
    print("  Type 'exit' / 'вихід' to close program.")
    print("=================================================================")

    while True:
        try:
            prompt_text = "\nInput / Введення: "
            raw_input = input(prompt_text)

            if raw_input.strip().lower() in ['exit', 'вихід']:
                print("Goodbye / До побачення!")
                break

            validated = validate_and_route(raw_input)
            if not validated:
                continue

            word, execution_case = validated
            props = analyze_noun_properties(word)

            # EN: Deterministic routing across individual target execution modules
            # UK: Детермінована маршрутизація через відповідні ізольовані модулі
            if execution_case == "genitive":
                output = genitive.apply_rules(word, props)
            elif execution_case == "accusative":
                output = accusative.apply_rules(word, props)
            elif execution_case == "dative":
                output = dative.apply_rules(word, props)
            elif execution_case == "instrumental":
                output = instrumental.apply_rules(word, props)
            elif execution_case == "locative":
                output = locative.apply_rules(word, props)
            elif execution_case == "vocative":
                output = vocative.apply_rules(word, props)

            print(f" -> Internal Token / Токен: {word}")
            print(f" -> Properties / Властивості: Gender={props['gender']} | Stem={props['stem_type']}")
            print(f" -> Output / Результат: {output}")

        except KeyboardInterrupt:
            print("\nAborted / Перервано.")
            break


if __name__ == "__main__":
    main()