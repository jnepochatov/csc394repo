from hashlib import sha256
from Persistence.candidate import CandidateObject
from Persistence.company import CompanyObject
from pymongo import MongoClient


dbs = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase
candidate_db = dbs.Candidate
company_db = dbs.Company
admin_db = dbs.admin


def candidate_login(username, password):
    valid = is_valid_candidate_credentials(username.lower(), password)
    if not valid:
        return False
    else:
        return True

def is_valid_candidate_credentials(username, password):
    exists = candidate_exists(username)
    candidates = candidate_db.find()
    if not exists:
        print("The username you have entered is not registered")
        return False
    else:
        # Check password section
        passwordHash = hash_text(password)
        for info in candidates:
            if info["userName"].lower() == username.lower():
                if info["password"] == passwordHash:
                    return True
            else:
                continue
    return False


def candidate_exists(username):
    candidates = candidate_db.find()
    for info in candidates:
        if info["userName"] == username.lower():
            return True
    return False


def hash_text(password):
    hashedText = sha256(password.encode('utf-8')).hexdigest()
    return hashedText
