from Persistence.data_retrieve import data_retrieve

class job(data_retrieve):
    def __init__(self, _id):
        data_retrieve.__init__(self, _id)
        self._id = _id
        self.db  = self.client.myFirstDatabase.Job
    
    def get_job_name(self):
        var = self.open_connection("jobName")
        self.name = var
        self.close_connection()
        return self.name
    
    def get_role(self):
        var = self.open_connection("jobRole")
        self.role = var
        self.close_connection()
        return self.role

    def get_desc(self):
        var = self.open_connection("jobDescription")
        self.desc = var
        self.close_connection()
        return self.desc

    def get_tech(self):
        var = self.open_connection("tech_skills")
        self.tech = var
        self.close_connection()
        return self.tech
    
    def get_business(self):
        var = self.open_connection("business_skills")
        self.business = var
        self.close_connection()
        return self.business
    
    def get_attitude(self):
        var = self.open_connection("attitude")
        self.attitude = var
        self.close_connection()
        return self.attitude

    def update_job_name(self, job_id, new_job_name):
        query = {"_id": job_id}
        if query is not None:
            update = {"$set": {"jobName": new_job_name}}
            self.db.update_one(query, update)
        return

    def update_role(self, job_id, new_role):
        query = {"_id": job_id}
        if query is not None:
            update = {"$set": {"jobRole": new_role}}
            self.db.update_one(query, update)
        return

    def update_desc(self, job_id, new_desc):
        query = {"_id": job_id}
        if query is not None:
            update = {"$set": {"jobDescription": new_desc}}
            self.db.update_one(query, update)
        return

    def update_tech(self, job_id, new_desc):
        query = {"_id": job_id}
        if query is not None:
            update = {"$set": {"jobDescription": new_desc}}
            self.db.update_one(query, update)
        return

    def update_tech(self, job_id, new_tech):
        query = {"_id": job_id}
        if query is not None:
            for skills in new_tech:
                update = {"$addToSet": {"tech_skills": skills}}
                self.db.update_one(query, update)
        return

    def update_business(self, job_id, new_business):
        query = {"_id": job_id}
        if query is not None:
            for skills in new_business:
                update = {"$addToSet": {"business_skills": skills}}
                self.db.update_one(query, update)
        return

    def update_attitude(self, job_id, new_attitude):
        query = {"_id": job_id}
        if query is not None:
            for attr in new_attitude:
                update = {"$addToSet": {"attitude": attr}}
                self.db.update_one(query, update)
        return
