#Password-Username Database

import sqlite3
from hashlib import sha256

running = True

con = sqlite3.connect('username.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
                    (username TEXT NOT NULL UNIQUE, 
                     password TEXT NOT NULL)''')

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
    def register():
        userName = str(input("Please enter a username to register with: ")) 
        exists = user_exists(userName)
        if not exists:
            passWord = str(input("Please enter a password: "))
            passwordHash = hash_text(passWord)
            credentials = (userName, passwordHash)
            cur.execute('INSERT INTO users VALUES (?,?)', credentials)
            con.commit()
        else:
            print("That username is already taken")

    def login():
        username = str(input("Please enter a username: "))
        password = str(input("Please enter a password: "))
        valid = is_valid_credentials(username, password)
        if not valid:
            print("Password or username is incorrect.")
        else:
            print("Login Successful!")

    def is_valid_credentials(username, password):
        exists = user_exists(username)
        if not exists:
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
    
    switcher = {
        1: register,
        2: login,
        3: printDB
    }
    func = switcher.get(selection, lambda: "Invalid Selection")
    func()
        
#Closes the database
con.close()
