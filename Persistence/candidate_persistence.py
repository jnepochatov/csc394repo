from Persistence.data_retrieve import DataRetrieve
from pymongo import MongoClient


class Candidate(DataRetrieve):
    def __init__(self, _id):
        DataRetrieve.__init__(self, _id)
        self._id = _id
        self.db  = self.client.myFirstDatabase.Candidate

    def get_candidate_db(self):
        return self.db

    def get_username(self):
        var = self.open_connection("userName")
        self.user = var
        self.close_connection()
        return self.user

    def get_email(self):
        var = self.open_connection("email")
        self.email = var
        self.close_connection()
        return self.email

    def get_phone(self):
        var = self.open_connection("phoneNum")
        self.phone = var
        self.close_connection()
        return self.phone

    def get_references(self):
        var = self.open_connection("references")
        self.ref = var
        self.close_connection()
        return self.ref

    def get_tech(self):
        var = self.open_connection("tech_Skills")
        self.tech = var
        self.close_connection()
        return self.tech
    
    def get_business(self):
        var = self.open_connection("business_Skills")
        self.business = var
        self.close_connection()
        return self.business
    
    def get_attitude(self):
        var = self.open_connection("attitude")
        self.attitude = var
        self.close_connection()
        return self.attitude

    def get_matches(self):
        try:
            var = self.open_connection("bestMatch")
            self.best = var
            self.close_connection()
            return self.best
        except:
            return "Might not have matches yet"

class CandidateObject:
    def __init__(self, username, password, email, name, phoneNum, references,
                 tech_skills, business_skills, attitude, bestMatch):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.phoneNum = phoneNum
        self.references = business_skills
        self.tech_skills = tech_skills
        self.business_skills = business_skills
        self.attitude = attitude
        self.bestMatch = bestMatch
        self.db = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.Candidate


    def create(self):

        candidate_data = {
                'password': self.password,
                'userName': self.username,
                'email': self.email,
                'phoneNum': self.phoneNum,
                'references': self.references,
                'tech_skills': self.tech_skills,
                'business_skills': self.business_skills,
                'attitude': self.attitude,
                'bestMatch': self.bestMatch,
                'name': self.name
            }
        self.db.insert_one(candidate_data)

"""
c1 = Candidate('6079f93c951c8b029023efe6')
candidate = CandidateObject("TT123", "password123", "Tetris@email.com", "Tetris Tetromino", "7737778888", "Puyo", ["Java", "c++"], ["Fast learner"], ["Hard working"], ["Job1"])
candidate.create()

print(c1.get_tech())

print(c1.get_matches())

print(c1.get_phone())

print(c1.get_username())
"""