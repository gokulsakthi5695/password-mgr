from tkinter import *
#Since message box is not a class in the tkinter and it is a seperate module we import the messagebox seperately from tkinter
from tkinter import messagebox
import random
#The use of Pyperclip will help us copy the password automatically which is being generated without even doing it manually
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Making use of the day 5 project of password generator and modifying it
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

    #Using the join method to convert the password_list into a string
    password = "".join(password_list)
    #Inserting the generated password when the user clicks the button
    pass_input.insert(END,password)
    #Using the pyperclip module to copy the generated password
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#Creating a new txt file to save the password
def save():
    website_entry = website_input.get()
    username_entry = user_input.get()
    password_entry = pass_input.get()

    if len(website_entry) == 0 or len(password_entry) == 0 or len(username_entry) == 0:
        messagebox.showerror(title="Error",message="Please don't leave any of the fields empty")

    else:
#There are many options in message box and we can call it as per our preference Eg
# messagebox.showinfo(title="title",message="message")
#The output of the messsagebox will be a boolean, so it should write in the text file only if they click ok and not when they click cancel
        is_ok = messagebox.askokcancel(title=website_entry,message=f"These are the details you entered: \nEmail: {username_entry} \nPassword: {password_entry} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website_entry} | {username_entry} | {password_entry} \n")
                website_input.delete(0,END)
                #If you are saving it to the same email, then it need not be deleted
                # user_input.delete(0,END)
                pass_input.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=tomato_img)
canvas.grid(row=0,column=1)

#Creating the rest of the UI and also making use of the columnspan function
#Creating the labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

user_label = Label(text="Email/Username:")
user_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#Creating the input boxes
website_input = Entry(width=39)
website_input.grid(row=1,column=1,columnspan=2)
#Using the focus method to start the cursor on the website entry as soon as the program launches
# website_input.focus()

user_input = Entry(width=39)
user_input.grid(row=2,column=1,columnspan=2)
#Starting the entry with already populated username/email because they will save all the password to the same email id
user_input.insert(END," ")

pass_input = Entry(width=21)
pass_input.grid(row=3,column=1)

#Creating the buttons
gen_pass_button = Button(text="Generate Password",command=generate_password)
gen_pass_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()