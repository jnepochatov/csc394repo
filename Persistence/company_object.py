from pymongo import MongoClient
from bson.objectid import ObjectId

class CompanyObject:
    def __init__(self, companyName, email, phoneNum, userName, password, job_list):

        self.companyName = companyName
        self.email = email
        self.phoneNum = phoneNum
        self.userName = userName
        self.password = password
        self.job_list = job_list
        self.db = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.Company

    def addJob(self, jobID):
        self.job_list.append(jobID)
        

    def create(self):
        
        company_data = {
                'companyName': self.companyName,
                'email': self.email,
                'phoneNum': self.phoneNum,
                'userName': self.userName,
                'password': self.password,
                'job_list': self.job_list,
            }

        self.db.insert_one(company_data)

company = CompanyObject("Vega Corporation", "Vega@email.com", "7735674321", "vega123", "password123", ["job1", "job2"])
