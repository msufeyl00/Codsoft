import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

# Initialize a list to store contacts
contacts = []

# Function to sort contacts by name
def sort_contacts():
    return sorted(contacts, key=lambda x: x['name'].lower())

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter name:")
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email:")
    address = simpledialog.askstring("Input", "Enter address:")
    
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        refresh_contact_list()
    else:
        messagebox.showwarning("Warning", "Name and phone number are required fields.")

# Function to update a selected contact
def update_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        name = simpledialog.askstring("Input", "Update name:", initialvalue=contact["name"])
        phone = simpledialog.askstring("Input", "Update phone number:", initialvalue=contact["phone"])
        email = simpledialog.askstring("Input", "Update email:", initialvalue=contact["email"])
        address = simpledialog.askstring("Input", "Update address:", initialvalue=contact["address"])
        
        if name and phone:
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            refresh_contact_list()
        else:
            messagebox.showwarning("Warning", "Name and phone number are required fields.")
    else:
        messagebox.showwarning("Warning", "Please select a contact to update.")

# Function to delete a selected contact
def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        refresh_contact_list()
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

# Function to refresh and display the contact list in ascending order
def refresh_contact_list():
    contact_listbox.delete(0, tk.END)
    sorted_contacts = sort_contacts()
    for contact in sorted_contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search for a contact
def search_contact(event=None):
    query = search_entry.get().lower()
    contact_listbox.delete(0, tk.END)
    for contact in sort_contacts():
        if query in contact['name'].lower() or query in contact['phone']:
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to display selected contact details
def show_contact_details(event):
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        contact = sort_contacts()[index]
        details = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
        messagebox.showinfo("Contact Details", details)

# Create the main application window
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")

# Search bar at the top
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Search:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side=tk.LEFT, padx=5)
search_entry.bind("<KeyRelease>", search_contact)

# Listbox to display contacts
contact_listbox = tk.Listbox(root, width=50, height=15)
contact_listbox.pack(pady=10)
contact_listbox.bind("<<ListboxSelect>>", show_contact_details)

# Buttons for add, update, and delete at the bottom
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact)
update_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.pack(side=tk.LEFT, padx=5)

# Refresh the contact list initially
refresh_contact_list()

# Start the main loop
root.mainloop()
