

       
from tkinter import *

# Create main window
root = Tk()
root.title("Calculator App")
root.geometry("350x500")
root.configure(bg="black")
root.resizable(False, False)

# Entry box
entry = Entry(root,
              font=("Arial", 24),
              bd=10,
              relief=RIDGE,
              justify=RIGHT,
              bg="white")
entry.pack(fill=BOTH, ipadx=8, pady=10, padx=10)

# Function to press buttons
def press(num):
    entry.insert(END, num)

# Function to clear screen
def clear():
    entry.delete(0, END)

# Function to calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button Frame
button_frame = Frame(root, bg="black")
button_frame.pack()

# Button design
btn_style = {
    "font": ("Arial", 18, "bold"),
    "width": 5,
    "height": 2,
    "bd": 5
}

# Row 1
Button(button_frame, text="7", bg="gray", fg="white",
       command=lambda: press("7"), **btn_style).grid(row=0, column=0)

Button(button_frame, text="8", bg="gray", fg="white",
       command=lambda: press("8"), **btn_style).grid(row=0, column=1)

Button(button_frame, text="9", bg="gray", fg="white",
       command=lambda: press("9"), **btn_style).grid(row=0, column=2)

Button(button_frame, text="/", bg="orange", fg="white",
       command=lambda: press("/"), **btn_style).grid(row=0, column=3)

# Row 2
Button(button_frame, text="4", bg="gray", fg="white",
       command=lambda: press("4"), **btn_style).grid(row=1, column=0)

Button(button_frame, text="5", bg="gray", fg="white",
       command=lambda: press("5"), **btn_style).grid(row=1, column=1)

Button(button_frame, text="6", bg="gray", fg="white",
       command=lambda: press("6"), **btn_style).grid(row=1, column=2)

Button(button_frame, text="*", bg="orange", fg="white",
       command=lambda: press("*"), **btn_style).grid(row=1, column=3)

# Row 3
Button(button_frame, text="1", bg="gray", fg="white",
       command=lambda: press("1"), **btn_style).grid(row=2, column=0)

Button(button_frame, text="2", bg="gray", fg="white",
       command=lambda: press("2"), **btn_style).grid(row=2, column=1)

Button(button_frame, text="3", bg="gray", fg="white",
       command=lambda: press("3"), **btn_style).grid(row=2, column=2)

Button(button_frame, text="-", bg="orange", fg="white",
       command=lambda: press("-"), **btn_style).grid(row=2, column=3)

# Row 4
Button(button_frame, text="0", bg="gray", fg="white",
       command=lambda: press("0"), **btn_style).grid(row=3, column=0)

Button(button_frame, text="C", bg="red", fg="white",
       command=clear, **btn_style).grid(row=3, column=1)

Button(button_frame, text="=", bg="green", fg="white",
       command=equal, **btn_style).grid(row=3, column=2)

Button(button_frame, text="+", bg="orange", fg="white",
       command=lambda: press("+"), **btn_style).grid(row=3, column=3)

# Run app
root.mainloop()
