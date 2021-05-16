from pymongo import MongoClient
from bson.objectid import ObjectId

class CandidatePersistence:
    def __init__(self, server_url):
        self.client = MongoClient(server_url)
        self.candidate_db = self.client.myFirstDatabase.Candidate
        self.username = ""

    def close_connection(self):
        self.client.close()

    def get_password(self):
        pass

    def get_username(self):
        pass
    
    def get_email(self, username):
        pass

    def get_phone(self):
        pass
    
    def get_references(self):
        pass

    def get_tech(self):
        pass
    
    def get_business(self):
        pass
    
    def get_attitude(self):
        pass

    def get_job_matches(self):
        pass

cand_pers = CandidatePersistence()