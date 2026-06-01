import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def complete_task():
    try:
        selected = task_listbox.curselection()[0]
        tasks[selected] = "✓ " + tasks[selected]
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Main Window
root = tk.Tk()
root.title("Colorful To-Do List")
root.geometry("600x600")
root.configure(bg="#1e1e2f")

# Title
title = tk.Label(
    root,
    text="TO-DO LIST APP",
    font=("Arial", 24, "bold"),
    bg="#1e1e2f",
    fg="yellow"
)
title.pack(pady=20)

# Entry Box
task_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 14),
    bd=3,
    bg="white"
)
task_entry.pack(pady=10)

# Add Button
add_btn = tk.Button(
    root,
    text="➕ Add Task",
    width=20,
    bg="#28a745",
    fg="white",
    font=("Arial", 12, "bold"),
    command=add_task
)
add_btn.pack(pady=5)

# Listbox
task_listbox = tk.Listbox(
    root,
    width=50,
    height=12,
    font=("Arial", 12),
    bg="#f8f9fa",
    fg="black",
    selectbackground="#007bff"
)
task_listbox.pack(pady=15)

# Complete Button
complete_btn = tk.Button(
    root,
    text="✔ Complete Task",
    width=20,
    bg="#17a2b8",
    fg="white",
    font=("Arial", 12, "bold"),
    command=complete_task
)
complete_btn.pack(pady=5)

# Delete Button
delete_btn = tk.Button(
    root,
    text="❌ Delete Task",
    width=20,
    bg="#dc3545",
    fg="white",
    font=("Arial", 12, "bold"),
    command=delete_task
)
delete_btn.pack(pady=5)

# Exit Button
exit_btn = tk.Button(
    root,
    text="🚪 Exit",
    width=20,
    bg="#6c757d",
    fg="white",
    font=("Arial", 12, "bold"),
    command=root.destroy
)
exit_btn.pack(pady=15)

# Footer
footer = tk.Label(
    root,
    text="Created by Ganapriya",
    bg="#1e1e2f",
    fg="lightgreen",
    font=("Arial", 10)
)
footer.pack(side="bottom", pady=10)

root.mainloop()