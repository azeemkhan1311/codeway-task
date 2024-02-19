import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Length must be greater than 0.", fg="red")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: " + password, fg="green")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid integer.", fg="red")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create length entry
length_label = tk.Label(root, text="Enter Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Create generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create result label
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()