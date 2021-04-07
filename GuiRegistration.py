from tkinter import *
import tkinter.messagebox
import sqlite3
from hashlib import sha256

con = sqlite3.connect('username.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
                    (username TEXT NOT NULL UNIQUE, 
                     password TEXT NOT NULL)''')

root = Tk()
root.geometry("500x300")

"""
running = True

# Used the while loop to make it easier to test
# Feel free to remove it and switcher section at the bottom

while(running):
    selection = int(input('''
    Please enter a number to perform an action(0 to exit):
    (1): register
    (2): login
    (3): printDB
    '''))
    if selection == 0:
        break

"""

def register():
    userName = enter_username()
    exists = user_exists(userName)
    if not exists:
        passWord = enter_password()
        passwordHash = hash_text(passWord)
        credentials = (userName, passwordHash)
        cur.execute('INSERT INTO users VALUES (?,?)', credentials)
        con.commit()
    else:
        tkinter.messagebox.showinfo('Popup Window(Title)','That username is already taken')
        print("That username is already taken")
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)


def login():
    username = enter_username()
    password = enter_password()
    valid = is_valid_credentials(username, password)
    if not valid:

        print("Password or username is incorrect.")
        tkinter.messagebox.showinfo('Popup Window(Title)', 'Password or username is incorrect')
    else:
        tkinter.messagebox.showinfo('Popup Window(Title)','Login Successful!')
        print("Login Successful!")
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)

def is_valid_credentials(username, password):
    exists = user_exists(username)
    if not exists:
        tkinter.messagebox.showinfo('Popup Window(Title)','The username you have entered is not registered')
        print("The username you have entered is not registered")
        return False
    else:
        passwordHash = hash_text(password)
        for row in cur.execute('SELECT * FROM users WHERE username=?', (username,)):
            if row[0] == username:
                if row[1] == passwordHash:
                    return True
                else:
                    return False

def enter_username():
    #Change the following line to get the username input from the GUI section
    #username = str(input("Please enter a username: "))
    username = str(usernameEntry.get())
    return username

def enter_password():
    #Change the following line to get the username input from the GUI section
    #password = str(input("Please enter a password: "))
    password = str(passwordEntry.get())
    return password

def user_exists(username):
    cur.execute('SELECT * FROM users WHERE username=?', (username,))
    exists = cur.fetchall()
    return exists


def hash_text(password):
    hashedText = sha256(password.encode('utf-8')).hexdigest()
    return hashedText

#For debugging purposes
def printDB():
    for row in cur.execute('SELECT * FROM users'):
        print(row)

"""

switcher = {
    1: register,
    2: login,
    3: printDB
}
func = switcher.get(selection, lambda: "Invalid Selection")
func()
"""

#GUI
Label(root, text="Registration Form", font ="arial 15 bold").grid(row=0, column=3)

#Field variable names
usernameLabel = Label(root, text="UserName")
passwordLabel = Label(root, text="Password")

#Packing variables
usernameLabel.grid(row=1, column=2)
passwordLabel.grid(row=2, column=2)

#Storing the value of our variables
usernameValue = StringVar
passwordValue = StringVar
checkValue = IntVar

#Entry fields
usernameEntry = Entry(root, textvariable = usernameValue)
passwordEntry = Entry(root, show="*", textvariable = passwordValue)

# Packing entry fields
usernameEntry.grid(row=1, column=3)
passwordEntry.grid(row=2, column=3)

#Check button
#checkbtn = Checkbutton(text = "remember me?", variable = checkValue)
#checkbtn.grid(row=6, column=3)

#Submit button
Button(text="Log In", command=login).grid(row=7, column = 2)
Button(text="Register", command=register).grid(row=7, column = 3)
#For debugging
Button(text="Print", command=printDB).grid(row=7, column = 4)


root.mainloop()
con.close()
