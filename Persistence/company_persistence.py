from data_retrieve import data_retrieve
from pymongo import MongoClient


class Company(data_retrieve):
    def __init__(self, _id):
        data_retrieve.__init__(self, _id)
        self._id = _id
        self.db  = self.client.myFirstDatabase.Company
        
    def get_company_db(self):
        return self.db

    def get_username(self):
        var = self.open_connection("userName")
        self.user = var
        self.close_connection()
        return self.user

    def get_companyName(self):
        var = self.open_connection("companyName")
        self.companyName = var
        self.close_connection()
        return self.companyName
    
    def get_email(self):
        var = self.open_connection("email")
        self.email = var
        self.close_connection()
        return self.email

    def get_phone(self):
        var = self.open_connection("phoneNum")
        self.phone = var
        self.close_connection()
        return self.phone

    def get_jobs(self):
        var = self.open_connection("job_list")
        self.job_list = var
        self.close_connection()
        return self.job_list

    def get_matches(self):
        try:
            var = self.open_connection("bestMatch")
            self.best = var
            self.close_connection()
            return self.best
        except:
            return "Might not have matches yet"


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


company = CompanyObject("X Station 360", "VideoGames@email.com", "7738979176", "XS360", "pcmasterrace", ["job1", "job2", "job3"])
company.create()
