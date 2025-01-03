import collections
import os
import random
import re


def generate_password():
    password_length = 10
    password = ""
    characters = "[abcdefghijklmnopqrstuvwxyz][\d+]"
    for i in range(password_length):
        password += random.choice(characters)
    return password


def count_words(file_path):
    with open(file_path) as file:
        text = file.read()
        words = re.findall(r'\w+', text)
        word_count = collections.Counter(words)
    return word_count


def list_files(directory):
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            files.append(file)
    return files

