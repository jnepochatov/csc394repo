from pymongo import MongoClient
from bson.objectid import ObjectId

class AdminPersistence:
    def __init__(self, server_url):
        self.client = MongoClient(server_url)
        self.candidate_db = self.client.myFirstDatabase.job
        self.username = ""

    def close_connection(self):
        self.client.close()

    def get_username(self):
        pass

    def get_password(self):
        pass
    
adm_pers = AdminPersistence()