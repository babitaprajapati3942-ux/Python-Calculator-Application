import tkinter as tk

window = tk.Tk()
window.title("My Calculator")
window.geometry("400x520")
window.resizable(False, False)


# Display
display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    bd=8
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=15,
    pady=20,
    ipady=12,
    sticky="ew"
)


# Add value to display
def click(value):
    display.insert(tk.END, value)


# Clear display
def clear():
    display.delete(0, tk.END)


# Calculate result
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]


for text, row, column in buttons:

    if text == "=":
        command = calculate
    else:
        command = lambda value=text: click(value)

    tk.Button(
        window,
        text=text,
        font=("Arial", 20),
        command=command
    ).grid(
        row=row,
        column=column,
        padx=6,
        pady=6,
        sticky="nsew"
    )


# Clear button
tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 18),
    command=clear
).grid(
    row=5,
    column=0,
    columnspan=4,
    padx=6,
    pady=10,
    sticky="nsew"
)


# Make all columns equal
for i in range(4):
    window.grid_columnconfigure(i, weight=1)


window.mainloop()