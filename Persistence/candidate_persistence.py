from Persistence.data_retrieve import data_retrieve

class candidate(data_retrieve):
    def __init__(self, _id):
        data_retrieve.__init__(self, _id)
        self._id = _id
        self.db = self.client.myFirstDatabase.Candidate
    
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

    def get_name(self):
        var = self.open_connection("name")
        self.name = var
        self.close_connection()
        return self.name

    def update_name(self, username, new_name):
        query = {"userName": username}
        if query is not None:
            update = {"$set": {"name": new_name}}
            self.db.update_one(query, update)
        return

    def update_email(self, username, new_email):
        query = {"userName": username}
        if query is not None:
            update = {"$set": {"email": new_email}}
            self.db.update_one(query, update)
        return

    def update_phone(self, username, new_phone):
        query = {"userName": username}
        if query is not None:
            update = {"$set": {"phoneNum": new_phone}}
            self.db.update_one(query, update)
        return

    def update_references(self, username, new_references):
        query = {"userName": username}
        if query is not None:
            for refs in new_references:
                update = {"$addToSet": {"references": refs}}
                self.db.update_one(query, update)
        return

    def update_tech(self, username, new_tech):
        query = {"userName": username}
        if query is not None:
            for skills in new_tech:
                update = {"$addToSet": {"tech_skills": skills}}
                self.db.update_one(query, update)
        return

    def update_business(self, username, new_business):
        query = {"userName": username}
        if query is not None:
            for skills in new_business:
                update = {"$addToSet": {"business_skills": skills}}
                self.db.update_one(query, update)
        return

    def update_attitude(self, username, new_attitude):
        query = {"userName": username}
        if query is not None:
            for attr in new_attitude:
                update = {"$addToSet": {"attitude": attr}}
                self.db.update_one(query, update)
        return
