import tkinter as tk
from tkinter import messagebox

# Initialize counters for task status
success_count = 0
fail_count = 0

# Initialize lists to store tasks
task_list = []
failed_tasks = []

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Create a frame for the list and scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Add a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a listbox to display tasks
task_listbox = tk.Listbox(frame, width=50, height=10, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=task_listbox.yview)

# Add an entry widget to add new tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Display the status of tasks
status_label = tk.Label(root, text=f"Tasks Completed: {success_count}, Tasks Failed: {fail_count}")
status_label.pack(pady=5)

# Define functions to add, delete, update, skip, and mark tasks
def add_task():
    task = task_entry.get()
    if task:
        task_list.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            task_listbox.delete(selected_task_index)
            task_list.pop(selected_task_index[0])
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            task = task_entry.get()
            if task:
                task_list[selected_task_index[0]] = task
                task_listbox.delete(selected_task_index)
                task_listbox.insert(selected_task_index, task)
                task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a task to update.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")

def complete_task():
    global success_count
    try:
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            task_listbox.delete(selected_task_index)
            task_list.pop(selected_task_index[0])
            success_count += 1
            update_status_label()
    except:
        messagebox.showwarning("Warning", "Please select a task to complete.")

def skip_task():
    global fail_count
    try:
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            task = task_listbox.get(selected_task_index)
            task_listbox.delete(selected_task_index)
            failed_tasks.append(task)
            task_list.pop(selected_task_index[0])
            fail_count += 1
            update_status_label()
    except:
        messagebox.showwarning("Warning", "Please select a task to skip.")

def update_status_label():
    status_label.config(text=f"Tasks Completed: {success_count}, Tasks Failed: {fail_count}")

# Create buttons to add, delete, update, complete, and skip tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=5)

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(pady=5)

skip_button = tk.Button(root, text="Skip Task", command=skip_task)
skip_button.pack(pady=5)

# Start the main loop
root.mainloop()
