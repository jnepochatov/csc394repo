# Password-Username Database

from hashlib import sha256
from Persistence.candidate_persistence import CandidateObject
from Persistence.company_persistence import CompanyObject

from pymongo import MongoClient


# from company_object import CompanyObject


def main():
    running = True

    dbs = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase
    candidate_db = dbs.Candidate
    company_db = dbs.Company
    admin_db = dbs.admin

    # Used the while loop to make it easier to test
    # Feel free to remove it and switcher section at the bottom

    while running:
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
            while 1:
                if reg_selection == 0:
                    break
                elif reg_selection == 1:
                    candidateReg()
                    print("Registration Successful!")
                    break
                elif reg_selection == 2:
                    companyReg()
                    print("Registration Successful!")
                    break
                else:
                    print("Please select a valid option \"1\" or \"2\"")
                    register()
                    break
        def login():
            log_sel = int(input('''
            Please select the type of login(or 0 to exit):
            (1): Candidate
            (2): Company
            (3): Admin
            '''))
            while 1:
                if log_sel == 0:
                    break
                elif log_sel == 1:
                    candidate_login()
                    break
                elif log_sel == 2:
                    company_login()
                    break
                elif log_sel == 3:
                    admin_login()
                    break
                else:
                    print("Please select a valid option \"1\" or \"2\"")
                    break

        def admin_login():
            username = str(input("Please enter your username: "))
            password = str(input("Please enter your password: "))
            valid = is_valid_admin_credentials(username.lower(), password)
            if not valid:
                print("Password or username is incorrect.")
            else:
                print("Login Successful!")
                admin_actions()

        def admin_actions():
            admin_sel = int(input('''
                        Please select admin action (or 0 to exit):
                        (1): Delete account
                        '''))
            while 1:
                if admin_sel == 0:
                    break
                elif admin_sel == 1:
                    del_account()
                    break

        def del_account():
            username = str(input("Please enter the account username you wish to delete"))
            can_exists = candidate_exists(username)
            com_exists = company_exists(username)
            if can_exists == False and com_exists == False:
                print("The username you have entered does not exist")
            elif can_exists:
                candidate_db.delete_one({
                    "userName": username
                })
            else:
                company_db.delete_one({
                    "userName": username
                })
            print("Deletion of " + username + "successful!")

        def candidate_login():
            username = str(input("Please enter your username: "))
            password = str(input("Please enter your password: "))
            valid = is_valid_candidate_credentials(username.lower(), password)
            if not valid:
                print("Password or username is incorrect.")
            else:
                print("Login Successful!")

        def company_login():
            username = str(input("Please enter your username: "))
            password = str(input("Please enter your password: "))
            valid = is_valid_company_credentials(username.lower(), password)
            if not valid:
                print("Password or username is incorrect.")
            else:
                print("Login Successful!")

        def is_valid_admin_credentials(username, password):
            exists = admin_exists(username)
            admins = admin_db.find()
            if not exists:
                print("The admin username you have entered is not registered")
                return False
            else:
                #Check password section
                #passwordHash = hash_text(password)
                for info in admins:
                    if info["userName"].lower() == username.lower():
                        if info["password"] == password:
                            return True
                    else:
                        continue
            return False


        def is_valid_candidate_credentials(username, password):
            exists = candidate_exists(username)
            candidates = candidate_db.find()
            if not exists:
                print("The username you have entered is not registered")
                return False
            else:
                #Check password section
                passwordHash = hash_text(password)
                for info in candidates:
                    if info["userName"].lower() == username.lower():
                        if info["password"] == passwordHash:
                            return True
                    else:
                        continue
            return False

        def is_valid_company_credentials(username, password):
            exists = company_exists(username)
            companies = company_db.find()
            if not exists:
                print("The username you have entered is not registered")
                return False
            else:
                # Check password section
                passwordHash = hash_text(password)
                for info in companies:
                    if info["userName"].lower() == username.lower():
                        if info["password"] == passwordHash:
                            return True
                    else:
                        continue
            return False


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
            tSkills = list()
            bSkills = list()
            aSkills = list()
            while(1):
                skill = str(input("Please enter a technical skill you have (or 0 to finish adding): "))
                if(skill == "0"):
                    break
                tSkills.append(skill)
            while(1):
                skill = str(input("Please enter a business skill you have (or 0 to finish adding): "))
                if(skill == "0"):
                    break
                bSkills.append(skill)
            while(1):
                skill = str(input("Please enter a attitude skill you have (or 0 to finish adding): "))
                if(skill == "0"):
                    break
                aSkills.append(skill)
            candidate = CandidateObject(username.lower(), hashed_password, email, fullName, phoneNum, references, tSkills, bSkills, aSkills, [])
            candidate.create()

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
        def company_exists(username):
            companies = company_db.find()
            for info in companies:
                if info["userName"] == username.lower():
                    return True
            return False

        def admin_exists(username):
            admins = admin_db.find()
            for info in admins:
                if info["userName"] == username.lower():
                    return True
            return False


        def hash_text(password):
            hashedText = sha256(password.encode('utf-8')).hexdigest()
            return hashedText

        switcher = {
            1: register,
            2: login,
        }
        func = switcher.get(selection, lambda: "Invalid Selection")
        func()

if __name__ == "__main__":
    main()