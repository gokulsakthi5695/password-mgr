from tkinter import *
from tkinter import messagebox
import random
import pyperclip

import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letter = [random.choice(letters) for char_letter in range(nr_letters)]
    pass_symbol = [random.choice(symbols) for char_symbol in range(nr_symbols)]
    pass_number = [random.choice(numbers) for char_number in range(nr_numbers)]

    password_list = pass_letter + pass_number + pass_symbol
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(END,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#Creating a new txt file to save the password
def save():
    website_entry = website_input.get()
    username_entry = user_input.get()
    password_entry = pass_input.get()
    #Creating a new dictionary for the JSON
    new_data = {website_entry:{"email":username_entry,"password":password_entry}}

    if len(website_entry) == 0 or len(password_entry) == 0 or len(username_entry) == 0:
        messagebox.showerror(title="Error",message="Please don't leave any of the fields empty")
#Using json.dump() to write to a json file -  asks for 2 inputs - dictionary and the location of the file
#Using the indent method will allow us to input the number of spaces required
                # json.dump(new_data,data_file,indent=4)
#Using json.load() to read the file and input the file path
                # print(json.load(data_file))
#Using the json.update() to append to the existing dictionary - we have to first json.load() and then proceed to update

#Since the load() and update() is functioning under read mode, to write/append the new data we have to open it in the write mode as done below
    # Using .json instead of a text format and making it as a write format
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            # Updating the new data with the old file
            data.update(new_data)
            with open("data.json", "w") as data_file:
            # Saving the updated data to the file
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data.keys():
                messagebox.showinfo(title=website,message=f"email: {data[website]['email']}\npassword:{data[website]['password']}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=tomato_img)
canvas.grid(row=0,column=1)

#Creating the labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

user_label = Label(text="Email/Username:")
user_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#Creating the input boxes
website_input = Entry(width=21)
website_input.grid(row=1,column=1)

user_input = Entry(width=21)
user_input.grid(row=2,column=1)
user_input.insert(END,"gokul@ssa.in")

pass_input = Entry(width=21)
pass_input.grid(row=3,column=1)

#Creating the buttons
gen_pass_button = Button(text="Generate Password",command=generate_password)
gen_pass_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",command=find_password,width=13)
search_button.grid(row=1,column=2)


window.mainloop()