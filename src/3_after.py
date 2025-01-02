import collections
import os
import random
import re
import string
from pprint import pprint


def generate_password():
    password_length = 10
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        # Генерируем случайный пароль
        password = "".join(random.choice(characters) for _ in range(password_length))

        # Проверяем, содержит ли пароль как цифры, так и буквы
        if re.search(r'\d', password) and re.search(r'[a-zA-Z]', password):
            return password



def count_words(file_path):
    with open(file_path,'r', encoding="utf-8") as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        word_count = collections.Counter(words)
    return word_count.most_common(10)


def list_files(directory):
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            files.append(os.path.join(directory, file))
    return files


if __name__ == '__main__':
    # password = generate_password()
    # print("Generated Password:", password)

    # word_count = count_words("data/example.txt")
    # print("Word Count:", dict(word_count))

    files = list_files(r"C:\Program Files\Python312\Lib")
    print("Files in Directory:")
    pprint(files)