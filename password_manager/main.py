from tkinter import *
from tkinter import messagebox
import random
import json
from functools import partial

PIN  = "0022"

def create_password():
    password_entry.delete(0,END)
    letters_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    letters_big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters_small) for char in range(3)]
    password_list += [random.choice(letters_big) for char in range(3)]
    password_list += [random.choice(numbers) for char in range(3)]
    password_list += [random.choice(symbols) for char in range(3)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)


def save_password():
    website = website_entry.get()
    password = password_entry.get()
    user = user_entry.get()

    with open("library_1.json","r") as input_file:
        data = json.load(input_file)

    if len(password) > 0 and len(website) > 0 and len(user) > 0 :
        is_okey = messagebox.askokcancel(title= website,message=f"These are the details entered : \n{user}"
                                                              f"\nPassword : {password} \nIs it ok to save?")
        if is_okey:
            new_user = {"website":website,"email":user,"password":password}
            data.append(new_user)
            with open("library_1.json", mode="w") as file_manager:
                json.dump(data,file_manager,indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showinfo(title= "Error",message="You can't leave any fields empty")

def show_list():
    root = Tk ( )
    root.title("Password List")
    root.config (pady=20 , padx=20)
    scrollbar = Scrollbar (root , orient="vertical")
    lb = Listbox (root , width=50 , height=20 , yscrollcommand=scrollbar.set)
    scrollbar.config (command=lb.yview)

    root.grid_rowconfigure (0 , weight=1)
    root.grid_columnconfigure (0 , weight=1)

    #scrollbar.grid (row=0 , column=1 , sticky="ns",columnspan=2)
    lb.grid (row=0 , column=0 , sticky="nsew",columnspan=2)

    pin_label = Label (root,text="Pin :")
    pin_label.grid (column=0 , row=1)

    pin_entry = Entry (root,width=35,show="*")
    pin_entry.grid (column=1 , row=1,padx=5, pady=5 )
    pin_entry.focus ( )



    with open("library_1.json","r") as input_file:
        data = json.load(input_file)


    for element in data:
        one_line = f"Website : {'*' * len(element['website'])} ;   Email : {'*' * len(element['email'])} ;   Password : {'*' * len(element['password']) }"
        lb.insert (END , one_line)

    show_censored_data = Button (root,text="Show censored data" , width=36,command=partial(show_data,pin_entry,data,lb) )
    show_censored_data.grid (column=0 , row=3 , columnspan=2,padx=5, pady=3)
    root.mainloop()

def show_data(pin_entry,data,lb):
    pin = pin_entry.get()

    if pin ==PIN:
        pin_entry.delete (0 , END)
        lb.delete(0,END)

        for element in data:
            one_line = f"Website : {element['website']};   Email : {element['email']};   Password : {element['password']}"
            lb.insert (END , one_line)
    else:
        messagebox.showerror (title="Error" , message="Wrong PIN!" )
        pin_entry.delete (0 , END)


window = Tk()
window.config(pady=20,padx=20)
window.title("Password Manager")

canvas = Canvas(width=200,height=200,highlightthickness=0)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=bg_image)
canvas.grid(column=1,row=0)

website_label = Label(text="Website :")
website_label.grid(column=0,row=1)

user_label = Label(text="Email/Username :")
user_label.grid(column=0,row=2)

password_label = Label(text="Password :")
password_label.grid(column=0,row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

user_entry = Entry(width=35)
user_entry.grid(column=1,row=2,columnspan=2)
user_entry.insert(0,"@gmail")

password_entry = Entry(width=21,show="*")
password_entry.grid(column=1,row=3)

passwoord_button = Button(text="Generate Password",width=15,command=create_password)
passwoord_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)

show_list_button = Button(text="Show list",width=15,command=show_list)
show_list_button.grid(column=0,row=4)



window.mainloop()