from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)

#---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()
    new_data = {website: {"username": username, "password": password}}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Try reading old data
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is empty, initialize `data` as an empty dictionary
            data = {}

        # Update data with the new entry
        data.update(new_data)

        with open("data.json", "w") as data_file:
            # Save updated data
            json.dump(data, data_file, indent=4)

        # Clear the input fields
        input_website.delete(0, END)
        input_password.delete(0, END)
#---------------------------Search--------------------------------------#
def search_website():
    website = input_website.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter the website to search for.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading data from file
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found.")
        else:
            if website in data:
                username = data[website]["username"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Not Found", message=f"No details for {website} exist.")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)



canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

#labels
website_label = Label(window, text='Website:')
website_label.grid(column=0, row=1)

username_label = Label(window, text='Username/Email:')
username_label.grid(column=0, row=2)


password_label = Label(window, text='password:')
password_label.grid(column=0, row=3)

#entries
input_website = Entry(width = 52)
input_website.grid(column=1, row=1, columnspan=2)

input_username = Entry(width = 33)
input_username.grid(column=1, row=2)
input_username.insert(0, "synowim22@bonaventure.edu")

input_password = Entry(width = 33)
input_password.grid(column=1, row=3)

#buttoms
generate_button = Button(text = "Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text = "Add", width=44, command = save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text = "Search", width=14, command=search_website)
search_button.grid(column=2, row=2)

window.mainloop()