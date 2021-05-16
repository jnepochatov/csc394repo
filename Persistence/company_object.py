from databases import Databases
from bson.objectid import ObjectId

class CompanyObject:
    def __init__(self, companyName, email, phoneNum, userName, password, job_list):

        self.companyName = companyName
        self.email = email
        self.phoneNum = phoneNum
        self.userName = userName
        self.password = password
        self.job_list = job_list
    def addJob(self, jobID):
        self.job_list.append(jobID)
        

    def create_company(company):
        
        company_data = {
                'companyName': company.companyName,
                'email': company.email,
                'phoneNum': company.phoneNum,
                'userName': company.userName,
                'password': company.password,
                'job_list': company.job_list,
            }
        table = dbs.get_company_db()
        table.insert_one(company_data)

dbs = Databases("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
company = CompanyObject("Vega Corporation", "Vega@email.com", "7735674321", "vega123", "password123", ["job1", "job2"])
