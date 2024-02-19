import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create task entry
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Create add button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=10)

# Create task listbox
tasks_listbox = tk.Listbox(root, width=50)
tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create delete button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()