import string
import random

# Functions that check password characteristics
def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_number(password):
    return any(char.isdigit() for char in password)

def check_special(password):
    return any(char in string.punctuation for char in password)

def calculate_score(password):
    score = 0
    if check_uppercase(password):
        score += 1
    if check_lowercase(password):
        score += 1
    if check_number(password):
        score += 1
    if check_special(password):
        score += 1
    if len(password) >= 8:
        score += 1
    return score

def generate_password(length=12):
    characters= string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

