import tkinter as tk

from password_tools import (check_uppercase,
                            check_lowercase,
                            check_number,
                            check_special,
                            calculate_score,
                            generate_password
)
window = tk.Tk()
window.columnconfigure(0, weight=1)

window.title("Password Security Analyzer")
window.geometry("500x450")

title = tk.Label(
    window,
    text="Password Security Analyzer",
    font=("Arial", 18, "bold")
)
title.grid(row=0, column=0, pady=(20,10))

label = tk.Label(window, text="Enter a password:")
label.grid(row=1, column=0, padx=20, pady=5)

entry = tk.Entry(window, width=30, show="*")
entry.grid(row=2, column=0, padx=20, pady=5)

show_password = tk.BooleanVar()

def check_password():
    password = entry.get()

    score = calculate_score(password)

    feedback = ""

    if score == 5:
        feedback = "Excellent! Your password meets all the recommended security checks."
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
        strength = "❌ Weak"
        color = "red"
    elif score <= 4:
        strength = "🟡 Medium"
        color = "orange"
    else:
        strength = "✅ Strong"
        color = "green"
    
    result_label.config(
        text=f"Password Strength: {strength} ({score}/5)\n\n{feedback}",
        fg=color
    )

def generate_new_password():
    new_password = generate_password()
    entry.delete(0, tk.END)
    entry.insert(0, new_password)

    check_password()

def toggle_password():
    if show_password.get():
        entry.config(show="")
    else:
        entry.config(show="*")

result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, padx=20, pady=10)

# Check Password Button
button = tk.Button(
    window,
    text="Check Password",
    command=check_password
)
button.grid(row=5, column=0, pady=5)

# Generate Password Button
generate_button = tk.Button(
    window,
    text="Generate Secure Password",
    command=generate_new_password
)
generate_button.grid(row=6, column=0, pady=5)
# Show password Checkbox
show_button = tk.Checkbutton(
    window,
    text="Show Password",
    variable=show_password,
    command=toggle_password
)

show_button.grid(row=3, column=0, pady=5)

window.mainloop()