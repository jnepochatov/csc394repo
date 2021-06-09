from pymongo import MongoClient
from Persistence.job_algo import find_matches

class JobObject:
    def __init__(self, j_id, jobName, jobRole, jobDescription, tech_skills, business_skills, attitude, bestMatch):
        self.j_id = j_id
        self.jobName = jobName
        self.jobRole = jobRole
        self.jobDescription = jobDescription
        self.tech_skills = tech_skills
        self.business_skills = business_skills
        self.attitude = attitude
        self.bestMatch = bestMatch
        self.db = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.Job

    def create(self):
        job_data = {
            'j_id': self.j_id,
            'jobName': self.jobName,
            'jobRole': self.jobRole,
            'jobDescription': self.jobDescription,
            'tech_skills': self.tech_skills,
            'business_skills': self.business_skills,
            'attitude': self.attitude,
            'bestMatch': self.bestMatch,
        }
        job_id = self.db.insert_one(job_data).inserted_id
        find_matches(job_id)
        return job_id
