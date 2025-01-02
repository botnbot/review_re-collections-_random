import re


def is_email(email:str) -> bool:
    """Функция проверяет, является ли строка корректным email-адресом."""
    pattern = re.compile(r'^[a-zA-Z0-9%._+=-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if pattern.fullmatch(email):
        return True
    return False


def format_dates(text):
    """Функция находит в тексте все даты и переводит их в формат DD.MM.YYYY"""
    pattern =  re.compile(r'\b(\d\d)/(\d\d)/(\d\d\d\d)\b')  #Регулярное выражение для нахождения дат в формате MM/DD/YYYY

    def replace_date(match):  # Функция для замены найденных дат на формат DD.MM.YYYY
        month, day, year = match.groups()
        return f'{day}.{month}.{year}'

    formatted_text = re.sub(pattern, replace_date, text)  # Замена всех найденных дат в тексте
    return formatted_text


if __name__ == '__main__':

    # password = generate_password()
    # print("Generated Password:", password)
    #
    # word_count = count_words("example.txt")
    # print("Word Count:", dict(word_count))
    #
    # files = list_files("example_directory")
    # print("Files in Directory:", files)

    # print(f'example@gmail.com {is_email("example@gmail.com")}') # True
    # print(f'example.gmail.com {is_email("example.gmail.com")}') # False
    # print(f'user@example.com {is_email("user@example.com")}')  # True
    # print(f'user+alias@example.com {is_email("user+alias@example.com")}')  # True
    # print(f'user.name@sub.example.org {is_email("user.name@sub.example.org")}')  # True
    # print(f'user@123.456 {is_email("user@123.456")}')  # False
    # print(f'user@.com {is_email("user@.com")}')  # False
    # print(f'user@com {is_email("user@com")}') # False

    text = "Встреча назначена на 05/20/2022. Подтвердите свое участие 05/10/2022."
    formatted_text = format_dates(text)
    print(formatted_text)  # Встреча назначена на 05.20.2022. Подтвердите свое участие 05.10.2022.
