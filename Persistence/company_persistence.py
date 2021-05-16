from pymongo import MongoClient
from bson.objectid import ObjectId

class CompanyPersistence:
    def __init__(self, server_url):
        self.client = MongoClient(server_url)
        self.company_db = self.client.myFirstDatabase.Company
        self.company_name = ""

    def close_connection(self):
        self.client.close()

    def get_company_name(self):
        pass

    def get_email(self, username):
        pass

    def get_phone(self):
        pass

    def get_username(self):
        pass

    def get_password(self):
        pass

comp_pers = CompanyPersistence()