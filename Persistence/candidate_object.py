from databases import Databases
from bson.objectid import ObjectId

class CandidateObject:
    def __init__(self, username, password, email, name, phoneNum, references,
                 tech_skills, business_skills, attitude, bestMatch):
        self.username = username
        self.objectId = ObjectId()
        self.password = password
        self.email = email
        self.name = name
        self.phoneNum = phoneNum
        self.references = business_skills
        self.tech_skills = tech_skills
        self.business_skills = business_skills
        self.attitude = attitude
        self.bestMatch = bestMatch
        




def create_candidate(candidate):

    candidate_data = {
            '_id': candidate.objectId,
            'password': candidate.password,
            'userName': candidate.username,
            'email': candidate.email,
            'phoneNum': candidate.phoneNum,
            'references': candidate.references,
            'tech_skills': candidate.tech_skills,
            'business_skills': candidate.business_skills,
            'attitude': candidate.attitude,
            'bestMatch': candidate.bestMatch,
            'name': candidate.name
        }
    table = dbs.get_candidate_db()
    table.insert_one(candidate_data)

dbs = Databases("db_access")
person = CandidateObject("rick123", "password123", "rick@email.com", "Rick Rickerson", "7737778888", "Bob", ["Java", "c++"], ["Fast learner"], ["Hard working"], ["Job1"])

