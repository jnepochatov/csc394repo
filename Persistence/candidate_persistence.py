from data_retrieve import data_retrieve

class Candidate(data_retrieve):
    def __init__(self, _id):
        data_retrieve.__init__(self, _id)
        self._id = _id
        self.db  = self.client.myFirstDatabase.Candidate

    def get_candidate_db(self):
        return self.db

    def get_username(self):
        var = self.open_connection("userName")
        self.user = var
        self.close_connection()
        return self.user

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

    def get_references(self):
        var = self.open_connection("references")
        self.ref = var
        self.close_connection()
        return self.ref

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

c1 = Candidate('6079f93c951c8b029023efe6')

print(c1.get_tech())

print(c1.get_matches())

print(c1.get_phone())

print(c1.get_username())
