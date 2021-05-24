from Persistence.data_retrieve import data_retrieve

class job(data_retrieve):
    def __init__(self, _id):
        data_retrieve.__init__(self, _id)
        self._id = _id
        self.db  = self.client.myFirstDatabase.Job
    
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