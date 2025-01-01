import collections
import os
import random
import re


def generate_password():
    password_length = 10
    password = ""
    characters = "abcdefghijklmnopqrstuvwxyz1234567890"
    for i in range(password_length):
        password += random.choice(characters)
    if not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password):
        return generate_password()
    return password


def count_words(file_path):
    with open(file_path) as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        word_count = collections.Counter(words)
    return word_count


def list_files(directory):
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            files.append(os.path.join(directory, file))
    return files


password = generate_password()
print("Generated Password:", password)

word_count = count_words("example.txt")
print("Word Count:", dict(word_count))

files = list_files("example_directory")
print("Files in Directory:", files)