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

    # Makes sure the password is at least 4 characters long
    if length < 4:
        length = 4

    # Starts with one character from each required category
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Pool of all possible characters
    all_characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    # Fills the rest of the password randomly
    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffles so the required characters aren't always first
    random.shuffle(password)

    # Converts the list into a string
    return "".join(password)