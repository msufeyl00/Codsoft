import tkinter as tk
from tkinter import messagebox
import random
import string

# Initialize the list to save passwords
saved_passwords = []

# Function to generate a password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4 characters.")
            return

        # Define possible characters
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number for the password length.")

# Function to save the generated password
def save_password():
    password = password_entry.get()
    if password:
        saved_passwords.append(password)
        messagebox.showinfo("Info", "Password saved successfully!")
    else:
        messagebox.showwarning("Warning", "No password to save.")

# Function to display saved passwords
def display_saved_passwords():
    if saved_passwords:
        saved_passwords_window = tk.Toplevel(root)
        saved_passwords_window.title("Saved Passwords")
        saved_passwords_listbox = tk.Listbox(saved_passwords_window, width=50, height=10)
        saved_passwords_listbox.pack(pady=10)
        
        for pwd in saved_passwords:
            saved_passwords_listbox.insert(tk.END, pwd)
    else:
        messagebox.showinfo("Info", "No passwords have been saved yet.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Label and entry to specify password length
length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack(pady=5)

length_entry = tk.Entry(root, width=30)
length_entry.pack(pady=5)

# Entry to display the generated password
password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=10)

# Buttons for generating, saving, and displaying passwords
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.pack(pady=5)

display_button = tk.Button(root, text="Display Saved Passwords", command=display_saved_passwords)
display_button.pack(pady=5)

# Start the main loop
root.mainloop()