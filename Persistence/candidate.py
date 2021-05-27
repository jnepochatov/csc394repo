from pymongo import MongoClient
from Persistence.candidate_algo import find_matches


class CandidateObject:
    def __init__(self, username, password, email, name, phoneNum, references,
                 tech_skills, business_skills, attitude, bestMatch):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.phoneNum = phoneNum
        self.references = references
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
        cand_id = self.db.insert_one(candidate_data).inserted_id
        find_matches(cand_id)