import tkinter as tk

from password_tools import (check_uppercase,
                            check_lowercase,
                            check_number,
                            check_special,
                            calculate_score,
                            generate_password
)
window = tk.Tk()

window.title("Password Strength Checker")
window.geometry("500x350")

label = tk.Label(window, text="Enter a password:")
label.grid(row=0, column=0)

entry = tk.Entry(window, width=30)
entry.grid(row=1, column=0)

def check_password():
    password = entry.get()

    score = calculate_score(password)

    feedback = ""

    if not check_uppercase(password):
        feedback += "Add an uppercase letter\n"

    if not check_lowercase(password):
        feedback += "Add a lowercase letter\n"

    if not check_number(password):
        feedback += "Add a number\n"

    if not check_special(password):
        feedback += "Add a special character\n"

    if len(password) < 8:
        feedback += "Make the password at least 8 characters long\n"
    if score<= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"
    
    result_label.config(
        text=f"Password Strength: {score}/5\n\n{feedback}"
    )

def generate_new_password():
    new_password = generate_password()
    entry.delete(0, tk.END)
    entry.insert(0, new_password)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, pady=10)

# Check Password Button
button = tk.Button(
    window,
    text="Check Password",
    command=check_password
)
button.grid(row=2, column=0)

# Generate Password Button
generate_button = tk.Button(
    window,
    text="Generate Strong Password",
    command=generate_new_password
)

generate_button.grid(row=4, column=0, pady=10)

window.mainloop()