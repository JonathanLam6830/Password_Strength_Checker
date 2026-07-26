import string

print("Password Strength Checker")

password = input("Enter a password: ")

has_uppercase = False
has_lowercase = False
has_number = False
has_special = False

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
    print("Your password has an uppercase letter, which is good for security.")
if has_lowercase:
    print("Your password has a lowercase letter, which is good for security.")
if has_number:
    print("Your password has a number, which is good for security.")
if has_special:
    print("Your password has a special character, which is good for security.")

#Checks the length of the password
if len(password) < 8:
    print("Weak password: too short")
else:
    print("Good length password")

