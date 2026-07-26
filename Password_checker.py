print("Password Strength Checker")

password = input("Enter a password: ")

for char in password:
    if char.isupper():
        print("Your password contains an uppercase letter, which is good for security")
# This code checks the length of the password
if len(password) < 8:
    print("Weak password: too short")
else:
    print("Good length password")

