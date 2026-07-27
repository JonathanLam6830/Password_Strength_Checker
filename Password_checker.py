import string

score = 0
has_uppercase = False
has_lowercase = False
has_number = False
has_special = False
is_common_password = False

common_passwords = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]
print("Password Strength Checker")

password = input("Enter a password: ")

if password.lower() in common_passwords:
    is_common_password = True
    print("WARNING: This password is commonly used and is not secure because it is easy to guess.")

#Checks if the password has at least one uppercase and/or lowercase letter
for char in password:
    if char.isupper():
        has_uppercase = True
    if char.islower():
        has_lowercase = True
    if char.isdigit():
        has_number = True
    if char in string.punctuation:
        has_special = True

if has_uppercase:
    score += 1
    print("Your password has an uppercase letter, which is good for security.")
if has_lowercase:
    score += 1
    print("Your password has a lowercase letter, which is good for security.")
if has_number:
    score += 1
    print("Your password has a number, which is good for security.")
if has_special:
    score += 1
    print("Your password has a special character, which is good for security.")
if len(password) >= 8:
    score += 1
    print("Your password is at least 8 characters long, which is good for security.")

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

print(f"Your password has a strength score of {score}/5.")

if score <= 2:
    print("Your password is weak. Consider making it stronger by adding more character types and increasing its length.")
elif score <=4:
    print("Your password is medium. You can improve it by adding more character types or increasing its length.")
else:
    print("Your password is strong. Good job!")