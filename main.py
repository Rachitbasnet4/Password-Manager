"""
A simple GUI-based Password Manager built using Tkinter.

This module provides functionality to:
- Generate secure random passwords using the PasswordGenerator class.
- Automatically copy generated passwords to the clipboard via pyperclip.
- Save login credentials (website, email/username, password) to a JSON file.
- Retrieve previously saved credentials using a search function.

The application features an interactive Tkinter interface with input fields
for website, email, and password, along with buttons to add, search, and
generate passwords. User input is validated before storage, and all data is
persisted in JSON format for later access.

Modules used:
    - tkinter: for UI creation and message dialogs
    - json: for reading and writing credential data
    - pyperclip: for clipboard copy functionality
    - password (PasswordGenerator): custom module for password generation
"""

import tkinter as tk
import json
from tkinter import messagebox
import pyperclip
from password import PasswordGenerator


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
password_generate = PasswordGenerator()


def password_generator_for_entry():
    """
        Generate a new password, display it in the password entry field,
        and automatically copy it to the clipboard.

        This function uses the PasswordGenerator instance to create a secure
        password, clears any existing text from the password input box, inserts
        the newly generated password into the entry widget, and finally copies
        it to the system clipboard for convenient pasting.
    """
    password = password_generate.generate()
    password_text_field.delete(0, tk.END)
    password_text_field.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """ 
    Save website login details (website, email, password) to a JSON file.

    The function retrieves user input from the GUI entry fields, validates
    the email format and checks for empty fields. If the input is valid, it
    stores the data in a JSON file (`details_data.json`). If the file does
    not exist or is unreadable, a new file is created automatically.

    Workflow:
        1. Collect input from text fields.
        2. Validate that no field is left empty and the email format is valid.
        3. Attempt to read existing JSON data; create new storage if not found.
        4. Update the stored data with new credentials.
        5. Write the updated data back to the JSON file.
        6. Clear the input fields after successful save.

    Alerts are displayed through messagebox to guide the user in case of
    invalid input or missing file.
    """

    website = website_text_field.get()
    email = email_text_field.get()
    password = password_text_field.get()
    new_data = {website.title(): {
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please make sure you haven't left any field empty")
    elif "@" not in email or "." not in email:
        messagebox.showinfo(title="Invalid Email",
                            message="Please enter a valid email address")
    else:
        try:
            with open("details_data.json",
                      mode="r", encoding="utf-8") as data_file:
                # Reading data
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
            # updating data
        data.update(new_data)
        with open("details_data.json",
                  mode="w", encoding="utf-8") as data_file:
            # write data in the json file
            json.dump(data, data_file, indent=4)

            website_text_field.delete(0, tk.END)
            email_text_field.delete(0, tk.END)
            password_text_field.delete(0, tk.END)


# ----------------------------  Search Password ----------------------------  #
def find_password():
    """ 
    Search for stored login credentials associated with a given website.

    The function retrieves the website name entered by the user and attempts
    to load stored data from `details_data.json`. If the file exists and the
    website is found, the associated email and password are displayed in a
    messagebox window. If no data file is found or the website does not
    exist in the stored records, a corresponding warning/alert message is
    shown to the user.

    Workflow:
        1. Read website name from input field.
        2. Attempt to open and load the JSON password storage file.
        3. Display error if file is missing.
        4. If file exists, look up the website credentials.
        5. Show matching email and password if found.
        6. Display an error message if no matching entry exists.
    """
    website = website_text_field.get().title()
    try:
        with open("details_data.json",
                  mode="r", encoding="utf-8") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Error", message="No Data File Found\nTry after adding data.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details found for {website}")


# ---------------------------- UI SETUP ------------------------------- #
windows = tk.Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

# canvas
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(
    file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# website lable
website_lable = tk.Label(text="Website:")
website_lable.grid(row=1, column=0)

# email lable
email_lable = tk.Label(text="Email/Username:")
email_lable.grid(row=2, column=0)

# password lable
password_lable = tk.Label(text="Password:")
password_lable.grid(row=3, column=0)

# website name entry field
website_text_field = tk.Entry(width=21)
website_text_field.grid(row=1, column=1)
website_text_field.focus()

# email entry field
email_text_field = tk.Entry(width=38)
email_text_field.grid(row=2, column=1, columnspan=2)
# email_text_field.insert(0, "gmail@gmaiil.com")

# password entry field
password_text_field = tk.Entry(width=21)
password_text_field.grid(row=3, column=1)

# generate search button
search_button = tk.Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=2)

# generate password button
pass_button = tk.Button(text="Generate Password",
                        command=password_generator_for_entry)
pass_button.grid(row=3, column=2)

# add button
add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

windows.mainloop()
