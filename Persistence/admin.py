from pymongo import MongoClient


class Admin:
    def __init__(self, username, password):
        self.userName = username
        self.password = password
        self.db = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.admin

    def create(self):
        admin_data = {
            'userName': self.userName,
            'password': self.password,
        }
        self.db.insert_one(admin_data)

#admin = Admin("administrator", "adminpassword")
#admin.create()
