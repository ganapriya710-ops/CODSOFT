import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#2C3E50")

title = tk.Label(root,
                 text="Password Generator",
                 font=("Arial", 18, "bold"),
                 bg="#2C3E50",
                 fg="white")
title.pack(pady=15)

tk.Label(root,
         text="Password Length:",
         bg="#2C3E50",
         fg="white",
         font=("Arial", 12)).pack()

length_entry = tk.Entry(root, font=("Arial", 14))
length_entry.pack(pady=10)

generate_btn = tk.Button(root,
                         text="Generate Password",
                         bg="#27AE60",
                         fg="white",
                         font=("Arial", 12, "bold"),
                         command=generate_password)
generate_btn.pack(pady=10)

result_entry = tk.Entry(root,
                        font=("Arial", 14),
                        width=30,
                        justify="center")
result_entry.pack(pady=20)

root.mainloop()