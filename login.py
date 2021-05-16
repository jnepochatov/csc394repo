#Password-Username Database

from hashlib import sha256
from databases import Databases
from candidate_object import CandidateObject
#from company_object import CompanyObject

running = True

dbs = Databases("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
candidate_db = dbs.get_candidate_db()
company_db = dbs.get_company_db()

# Used the while loop to make it easier to test
# Feel free to remove it and switcher section at the bottom

while(running):
    selection = int(input('''
    Please enter a number to perform an action(0 to exit):
    (1): register
    (2): login
    '''))
    if selection == 0:
        break
    def register():
        reg_selection = int(input('''
        Please select the type of registration(or 0 to exit):
        (1): Candidate
        (2): Company
        '''))
        while(1):
            if(reg_selection == 0):
                break
            elif(reg_selection == 1):
                candidateReg()
                print("Registration Successful!")
            elif(reg_selection == 1):
                companyReg()
                print("Registration Successful!")
            else:
                print("Please select a valid option \"1\" or \"2\"")
                register()
            

    def login():
        username = str(input("Please enter your username: "))
        password = str(input("Please enter your password: "))
        valid = is_valid_credentials(username.lower(), password)
        if not valid:
            print("Password or username is incorrect.")
        else:
            print("Login Successful!")

    def is_valid_credentials(username, password):
        exists = candidate_exists(username)
        if not exists:
            print("The username you have entered is not registered")
            return False
        else:
            #Check password section
            passwordHash = hash_text(password)
            return False
        return True
    
        
    def candidateReg():
        #Change the following line to get the username input from the GUI section
        username = str(input("Please enter a username: "))
        exists = candidate_exists(username)
        while(exists):
            username = str(input("Username is taken. Please enter a new username or login: "))
            exists = candidate_exists(username)
        #Change the following line to get the username input from the GUI section
        password = str(input("Please enter desired password: "))
        hashed_password = hash_text(password)
        email = str(input("Please enter an email: "))
        fullName = str(input("Please enter your full name: "))
        phoneNum = str(input("Please enter your phone number: "))
        references = str(input("Please enter the name of any references you may have: "))
        cont = 1
        tSkills = list()
        bSkills = list()
        aSkills = list()
        while(1):
            skill = str(input("Please enter a technical skill you have (or 0 to finish adding): "))
            if(skill == "0"):
                break;
            tSkills.append(skill)
        while(1):
            skill = str(input("Please enter a business skill you have (or 0 to finish adding): "))
            if(skill == "0"):
                break;
            bSkills.append(skill)
        while(1):
            skill = str(input("Please enter a attitude skill you have (or 0 to finish adding): "))
            if(skill == "0"):
                break;
            aSkills.append(skill)
        candidate = CandidateObject(username.lower(), hashed_password, email, fullName, phoneNum, references, tSkills, bSkills, aSkills, [])
        create_candidate(candidate)
        return candidate
    
    def companyReg():
        username = str(input("Please enter a username: "))
        exists = company_exists(username)
        while(exists):
            username = str(input("Username is taken. Please enter a new username or login: "))
            exists = company_exists(username)
        #Change the following line to get the username input from the GUI section
        password = str(input("Please enter desired password: "))
        hashed_password = hash_text(password)
        CompanyName = str(input("Please enter the company's name: "))
        email = str(input("Please enter an email: "))
        phoneNum = str(input("Please enter your phone number: "))
        job_list = list()
        company  = CompanyObject(CompanyName, email, phoneNum, username, hashed_password, job_list)
        company.create()
        
    def candidate_exists(username):
        candidates = candidate_db.find()
        for info in candidates:
            if info["userName"] == username.lower():
                return True
        return False
    def company_exists(name):
        companies = company_db.find()
        for info in companies:
            if info["userName"] == username.lower():
                return True
        return False

    
    
    def hash_text(password):
        hashedText = sha256(password.encode('utf-8')).hexdigest()
        return hashedText
    
    #For debugging purposes
    #
    #def printDB():
    #    for row in cur.execute('SELECT * FROM users'):
    #        print(row)
    
    switcher = {
        1: register,
        2: login,
    }
    func = switcher.get(selection, lambda: "Invalid Selection")
    func()
        
#Closes the database
con.close()
