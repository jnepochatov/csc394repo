from pymongo import MongoClient
from bson.objectid import ObjectId

class JobPersistence:
    def __init__(self, server_url):
        self.client = MongoClient(server_url)
        self.candidate_db = self.client.myFirstDatabase.job
        self.job_title = ""

    def close_connection(self):
        self.client.close()

    def get_job_title(self):
        pass
    
    def get_job_description(self):
        pass

    def get_poster_name(self):
        pass

    def get_poster_contact_info(self):
        pass
    
job_pers = JobPersistence()