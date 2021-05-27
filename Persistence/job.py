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
"""
job = JobObject(1, "accountant", "accountant", "Looking for a skilled accountant willing to put in the time.", ["python", "MATLAB"], ["Quickbooks", "Accounting", "Finance", "mathematics"], ["committed", "professional", "responsible"], list()).create()
job = JobObject(2, "programmer", "programming", "need experienced programmers", ["C", "C#", "C++", "Assembly"], ["communication", "problem solving", "critical thinking"], ["committed", "dependable", "professional"], list()).create()
job = JobObject(3, "software developer", "software developer", "need beginner software developers", ["Java", "python", "PL/SQL"], ["communication", "problem solving", "critical thinking"], ["committed", "dependable", "professional"], list()).create()
job = JobObject(4, "research assistant", "assist lead researcher", "help with research", ["PL/SQL"], ["communication", "Organization", "research"], ["respectful", "helpfulness", "responsible"], list()).create()
job = JobObject(5, "IT", "information technology", "IT role", ["HTML", "CSS", "JavaScript", "Java"], ["information technology"], ["helpfulness", "adaptable"], list()).create()

job = JobObject(6, "digital media specialist", "social media manager", "Looking to grow our social media presence.", list(), ["marketing/sales", "digital media", "writing", "graphic design"], ["enthusiastic", "adaptable", "creative"], list()).create()
job = JobObject(7, "marketing associate", "marketing associate", "need marketing associate to help relay our company message.", list(), ["digital media", "marketing/sales"], ["enthusiastic", "adaptable"], list()).create()
job = JobObject(8, "grocery manager", "grocery manager", "need grocery manager to handle shift leading", list(), ["customer service", "food services"], ["dependable"], list()).create()
job = JobObject(9, "insurance consultant", "insurance consultant", "in need of insurance consultant", ["MATLAB", "R"], ["Finance", "Insurance"], ["professional"], list()).create()
job = JobObject(10, "restaurant management", "restaurant management", "looking for a restaurant manager", list(), ["customer service", "food services", "multitasking"], ["dependable", "responsible"], list()).create()

job = JobObject(11, "newsletter columnist", "newsletter columnist", "looking for new columnist", list(), ["multilingual", "writing", "research"], ["committed", "professional"], list()).create()
job = JobObject(12, "economist", "economist", "economic advisor", ["R"], ["Finance", "Accounting"], ["dependable", "responsible", "professional"], list()).create()
job = JobObject(13, "head of human resources", "head of human resources", list(), list(), list(), list(), list()).create()
job = JobObject(14, "cloud engineer", "cloud engineer", "not looking for meteorologists", ["C++", "Swift"], ["critical thinking", "cloud computing"], ["innovative"], list()).create()
job = JobObject(15, "research analyst", "researcher", "analyzing research", ["PL/SQL", "R"], ["research"], ["committed", "professional"], list()).create()

job = JobObject(16, "tetris downstacker", "demolition", "it's tetris yo", list(), ["critical thinking"], ["enthusiastic", "cheerful", "innovative", "adaptable"], list()).create()
job = JobObject(17, "puyo exterminator", "exterminator", "time for puyo puyo", list(), ["critical thinking"], ["cheerful", "helpful", "adaptable"], list()).create()
job = JobObject(18, "architect", "opposite of demolition", "what should the buildings look like though", list(), ["Organization", "engineering"], ["innovative", "creative"], list()).create()
job = JobObject(19, "engineer", "how", "enginering...", ["MATLAB"], ["engineering"], ["innovative", "adaptable", "creative"], list()).create()
job = JobObject(20, "graphic design", "graphic designer", "whoah did you make this!", ["CSS"], ["graphic design"], ["creative"], list())
"""