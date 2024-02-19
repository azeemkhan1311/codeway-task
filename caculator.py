import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + number)

def clear_display():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry screen
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
#  example "7" is the number wich appears on button, 1 defines the row, 0 defines the column
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == "C":
        button = tk.Button(root, text=text, padx=40, pady=20, command=clear_display)
    elif text == "=":
        button = tk.Button(root, text=text, padx=91, pady=20, command=calculate)
    else:
        button = tk.Button(root, text=text, padx=40, pady=20, command=lambda num=text: button_click(num))
    button.grid(row=row, column=col)

root.mainloop()