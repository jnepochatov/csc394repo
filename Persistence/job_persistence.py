from data_retrieve import DataRetrieve
from pymongo import MongoClient


class Job(DataRetrieve):
    def __init__(self, _id):
        DataRetrieve.__init__(self, _id)
        self._id = _id
        self.db  = self.client.myFirstDatabase.job

    def get_job_db(self):
        return self.db

    def get_name(self):
        var = self.open_connection("jobName")
        self.name = var
        self.close_connection()
        return self.name

    def get_role(self):
        var = self.open_connection("jobRole")
        self.role = var
        self.close_connection()
        return self.role

    def get_description(self):
        var = self.open_connection("jobDescription")
        self.description = var
        self.close_connection()
        return self.description

    def get_tech(self):
        var = self.open_connection("tech_Skills")
        self.tech = var
        self.close_connection()
        return self.tech

    def get_business(self):
        var = self.open_connection("business_Skills")
        self.business = var
        self.close_connection()
        return self.business

    def get_attitude(self):
        var = self.open_connection("attitude")
        self.attitude = var
        self.close_connection()
        return self.attitude

    def get_matches(self):
        try:
            var = self.open_connection("bestMatch")
            self.best = var
            self.close_connection()
            return self.best
        except:
            return "Might not have matches yet"

class JobObject:
    def __init__(self, jobName, jobRole, jobDescription, tech_skills, business_skills, attitude):
        self.jobName = jobName
        self.jobRole = jobRole
        self.jobDescription = jobDescription
        self.tech_skills = tech_skills
        self.business_skills = business_skills
        self.attitude = attitude
        self.bestMatch = ["Candidate1"]
        self.db = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.job

    def create(self):
        job_data = {
            'jobName': self.jobName,
            'jobRole': self.jobRole,
            'jobDescription': self.jobDescription,
            'tech_skills': self.tech_skills,
            'business_skills': self.business_skills,
            'attitude': self.attitude,
            'bestMatch': self.bestMatch,
        }
        self.db.insert_one(job_data)


job = JobObject("Junior Software Developer", "Software Developer",
                "Looking for a full stack software developer who has experience developing in-house algorithms",
                ["MongoDB", "HTML", "CSS", "Python"], ["Problem Solving", "Leadership"],
                ["Hard-Working", "Attention to detail"])

job.create()


