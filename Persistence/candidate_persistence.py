from pymongo import MongoClient
from bson.objectid import ObjectId
from databases import Databases

class CandidatePersistence:
    def __init__(self, candidate_db):
        self.candidate_db = candidate_db

    def get_username(self, username):
        query = self.candidate_db.find()
        user = None

        for names in query:
            queried_username = names["userName"]
            if queried_username == username:
                user = queried_username

        if user is None:
            print("Could not find user in db")

        return user

    def get_all_users(self):
        query = self.candidate_db.find()
        for names in query:
            print(names["userName"])
        return
    
    def get_email(self, username):
        pass

    def get_phone(self):
        pass
    
    def get_reference_names(self):
        pass

    def get_reference_write_up(self):
        pass

    def get_tech(self):
        pass
    
    def get_business(self):
        pass
    
    def get_attitude(self):
        pass

    def get_matches(self):
        pass


dbs = Databases("db_access")
cp = CandidatePersistence(dbs.get_candidate_db())