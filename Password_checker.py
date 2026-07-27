import string

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

is_common_password = False
# List of frequently used passwords that should be avoided
common_passwords = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]
print("Password Strength Checker")

password = input("Enter a password: ")

has_uppercase = check_uppercase(password)
has_lowercase = check_lowercase(password)
has_number = check_number(password)
has_special = check_special(password)

if password.lower() in common_passwords:
    is_common_password = True
    print("WARNING: This password is commonly used and is not secure because it is easy to guess.")

score = calculate_score(password)

print(f"Your password has a strength score of {score}/5.")

#Gives suggestions for what is missing in the password to make it stronger
if not has_uppercase:
    print("Consider adding an uppercase letter")
if not has_lowercase:
    print("Consider adding a lowercase letter")
if not has_number:
    print("Consider adding a number")
if not has_special:
    print("Consider adding a special character")
if len(password) < 8:
    print("Consider making your password at least 8 characters long")

if score <= 2:
    print("Your password is weak. Consider making it stronger by adding more character types and increasing its length.")
elif score <=4:
    print("Your password is medium. You can improve it by adding more character types or increasing its length.")
else:
    print("Your password is strong. Good job!")