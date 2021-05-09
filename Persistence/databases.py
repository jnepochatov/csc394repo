from pymongo import MongoClient
from bson.objectid import ObjectId

class Databases:
	def __init__(self, server_url):
		self.client = MongoClient(server_url)
		self._db = self.client.myFirstDatabase
		self.candidates = self._db.Candidate
		self.companies = self._db.Company
		self.jobs = self._db.job
		self.admins = self._db.admin

	def get_candidate_db(self):
		return self.candidates

	def get_company_db(self):
		return self.companies

	def get_job_db(self):
		return self.jobs

	def get_admin_db(self):
		return self.admins



"""
	def open_connection(self, var):
		for result in self.db.find({"_id": ObjectId(self._id)}, {var: 1}):
			variable = result[var]
		return variable
    
	def close_connection(self):
		self.client.close()

client = MongoClient("db_access")

db = client["myFirstDatabase"]

candidates = db.Candidate
companies = db.Company
jobs = db.job
admins = db.admin

everyone = candidates.find()
"""

'''
for info in everyone:
	if info["userName"].lower() == "steve".lower():
		print(info["userName"])
'''

'''
t_skill_arr = []
names = []
for info in everyone:
	names = info["userName"]
	t_skill_arr = info["tech_Skills"]
	for t_skill in t_skill_arr:
		if t_skill == "c#".lower():
			print(names)
			print("Has this skill")
'''