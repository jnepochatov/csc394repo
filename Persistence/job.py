from pymongo import MongoClient
from Persistence.job_algo import find_matches

class JobObject:
    def __init__(self, jobName, jobRole, jobDescription, tech_skills, business_skills, attitude, bestMatch):
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

#job = JobObject("Junior Software Developer", "Software Developer",
                #"Looking for a full stack software developer who has experience developing in-house algorithms",
                #["MongoDB", "HTML", "CSS", "Python"], ["Problem Solving", "Leadership"],
                #["Hard-Working", "Attention to detail"], list())

#job.create()