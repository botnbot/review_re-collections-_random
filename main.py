import re
from collections import Counter


def is_email(email: str) -> bool:
    """Функция проверяет, является ли строка корректным email-адресом."""
    pattern = re.compile(r'^[a-zA-Z0-9%._+=-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if pattern.fullmatch(email):
        return True
    return False


def format_dates(text):
    """Функция находит в тексте все даты и переводит их в формат DD.MM.YYYY"""
    pattern = re.compile(
        r'\b(\d\d)/(\d\d)/(\d\d\d\d)\b')  # Регулярное выражение для нахождения дат в формате MM/DD/YYYY

    def replace_date(match):  # Функция для замены найденных дат на формат DD.MM.YYYY
        month, day, year = match.groups()
        return f'{day}.{month}.{year}'

    formatted_text = re.sub(pattern, replace_date, text)  # Замена всех найденных дат в тексте
    return formatted_text


def most_common_letter(string: str) -> list:
    """Функция принимает строку и возвращает наиболее часто встречающуюся букву в строке(без учета регистра и без цифр).
    Если таких букв несколько, возвращает список со всеми найденными буквами."""
    letters = [letter.lower() for letter in string if letter.isalpha()]
    letter_count = Counter(letters)
    best_letters = max(letter_count.values(), default=0)
    print(f"{best_letters} буквы", end=' ')
    most_common = [letter for letter, count in letter_count.items() if count == best_letters]

    return most_common


if __name__ == '__main__':
    # print(f'example@gmail.com {is_email("example@gmail.com")}') # True
    # print(f'example.gmail.com {is_email("example.gmail.com")}') # False
    # print(f'user@example.com {is_email("user@example.com")}')  # True
    # print(f'user+alias@example.com {is_email("user+alias@example.com")}')  # True
    # print(f'user.name@sub.example.org {is_email("user.name@sub.example.org")}')  # True
    # print(f'user@123.456 {is_email("user@123.456")}')  # False
    # print(f'user@.com {is_email("user@.com")}')  # False
    # print(f'user@com {is_email("user@com")}') # False

    # text = "Встреча назначена на 05/20/2022. Подтвердите свое участие 05/10/2022."
    # formatted_text = format_dates(text)
    # print(formatted_text)  # Встреча назначена на 05.20.2022. Подтвердите свое участие 05.10.2022.

    string = ("Пример текста для проверки. В этом тексте есть несколько букв, которые встречаются часто,"
              " а некоторые из них повторяются больше, чем другие. Проверим, как работает функция для поиска наиболее"
              " частых букв. Привет, мир! Давайте проверим, какие буквы будут самыми популярными."
              " Возможно, они будут одинаковыми")
    print(most_common_letter(string))  # ['о']
