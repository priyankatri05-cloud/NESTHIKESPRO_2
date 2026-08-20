import tkinter as tk
import math


# ==========================================================
#                 MAIN WINDOW
# ==========================================================

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("430x650")
root.resizable(False, False)

# Dark gray main background
root.configure(bg="#2B2B2B")


# ==========================================================
#                 FUNCTIONS
# ==========================================================

# Insert numbers/operators into display
def button_click(value):
    display.insert(tk.END, value)


# Clear display
def clear():
    display.delete(0, tk.END)


# Delete last character
def backspace():
    current = display.get()

    if current:
        display.delete(0, tk.END)
        display.insert(0, current[:-1])


# Calculate expression
def calculate():
    try:
        expression = display.get()

        # Replace calculator symbols with Python operators
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        result = eval(expression)

        # Remove unnecessary .0
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# ==========================================================
#                 SCIENTIFIC FUNCTIONS
# ==========================================================

# Square root
def square_root():
    try:
        number = float(display.get())

        if number < 0:
            raise ValueError

        result = math.sqrt(number)

        if result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Square
def square():
    try:
        number = float(display.get())

        result = number ** 2

        if result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Percentage
def percentage():
    try:
        number = float(display.get())

        result = number / 100

        if result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Sine - degrees
def sine():
    try:
        number = float(display.get())

        result = math.sin(math.radians(number))

        result = round(result, 10)

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Cosine - degrees
def cosine():
    try:
        number = float(display.get())

        result = math.cos(math.radians(number))

        result = round(result, 10)

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Tangent - degrees
def tangent():
    try:
        number = float(display.get())

        # Tangent is undefined at 90 + 180n
        angle = number % 180

        if abs(angle - 90) < 0.0000001:
            raise ValueError

        result = math.tan(math.radians(number))

        result = round(result, 10)

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# ==========================================================
#                 DISPLAY
# ==========================================================

display = tk.Entry(
    root,
    font=("Arial", 25),
    justify="right",
    bd=8,
    bg="#3A3A3A",
    fg="white",
    insertbackground="white"
)

display.pack(
    padx=15,
    pady=15,
    fill="x",
    ipady=10
)


# ==========================================================
#                 BUTTON FRAME
# ==========================================================

button_frame = tk.Frame(
    root,
    bg="#2B2B2B"
)

button_frame.pack()


# ==========================================================
#                 BUTTON LIST
# ==========================================================

buttons = [

    # Scientific buttons
    ("sin", 0, 0, sine),
    ("cos", 0, 1, cosine),
    ("tan", 0, 2, tangent),
    ("√",   0, 3, square_root),

    # Control buttons
    ("x²", 1, 0, square),
    ("%",  1, 1, percentage),
    ("C",  1, 2, clear),
    ("⌫",  1, 3, backspace),

    # Number and operator buttons
    ("7", 2, 0, lambda: button_click("7")),
    ("8", 2, 1, lambda: button_click("8")),
    ("9", 2, 2, lambda: button_click("9")),
    ("÷", 2, 3, lambda: button_click("÷")),

    ("4", 3, 0, lambda: button_click("4")),
    ("5", 3, 1, lambda: button_click("5")),
    ("6", 3, 2, lambda: button_click("6")),
    ("×", 3, 3, lambda: button_click("×")),

    ("1", 4, 0, lambda: button_click("1")),
    ("2", 4, 1, lambda: button_click("2")),
    ("3", 4, 2, lambda: button_click("3")),
    ("-", 4, 3, lambda: button_click("-")),

    ("0", 5, 0, lambda: button_click("0")),
    (".", 5, 1, lambda: button_click(".")),
    ("=", 5, 2, calculate),
    ("+", 5, 3, lambda: button_click("+"))
]


# ==========================================================
#                 CREATE BUTTONS
# ==========================================================

for text, row, column, command in buttons:

    # All buttons dark gray
    button_color = "#444444"

    # Default text color
    text_color = "white"

    # Make ONLY the Clear button text orange
    if text == "C":
        text_color = "#FF9500"

    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16),
        width=5,
        height=2,

        # Dark gray button
        bg=button_color,

        # Text color
        fg=text_color,

        # Button pressed color
        activebackground="#555555",

        # Keep text color when pressed
        activeforeground=text_color,

        # Remove button border
        bd=0,

        # Button command
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4
    )


# ==========================================================
#                 KEYBOARD SUPPORT
# ==========================================================

def keyboard_input(event):

    key = event.keysym
    char = event.char

    # Numbers, decimal and operators
    if char in "0123456789.+-*/":

        # Convert keyboard * to calculator ×
        if char == "*":
            display.insert(tk.END, "×")

        # Convert keyboard / to calculator ÷
        elif char == "/":
            display.insert(tk.END, "÷")

        else:
            display.insert(tk.END, char)

    # Enter = calculate
    elif key in ("Return", "KP_Enter"):
        calculate()

    # Backspace
    elif key == "BackSpace":
        backspace()

    # Escape = clear
    elif key == "Escape":
        clear()


# Connect keyboard with calculator
root.bind("<Key>", keyboard_input)


# ==========================================================
#                 START APPLICATION
# ==========================================================

root.mainloop()