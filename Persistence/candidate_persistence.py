from pymongo import MongoClient
from bson.objectid import ObjectId
from databases import Databases

class CandidatePersistence:
    def __init__(self):
        self.client = MongoClient(server_url)
        self.candidate_db = self.client.myFirstDatabase.Candidate
        self.username = ""
        self.query = self.candidate_db.find()

    def close_connection(self):
        self.client.close()

    def get_username(self, user_name):
        pass
    
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