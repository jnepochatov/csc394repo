from Persistence.data_retrieve import data_retrieve

class company(data_retrieve):
    def __init__(self, _id):
        data_retrieve.__init__(self, _id)
        self._id = _id
        self.db = self.client.myFirstDatabase.Company

    def get_username(self):
        var = self.open_connection("userName")
        self.user = var
        self.close_connection()
        return self.user

    def get_password(self):
        var = self.open_connection("password")
        self.password = var
        self.close_connection()
        return self.password
    
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

    def get_comp_name(self):
        var = self.open_connection("companyName")
        self.comp_name = var
        self.close_connection()
        return self.comp_name

    def update_comp_name(self, username, new_comp_name):
        query = {"userName": username}
        if query is not None:
            update = {"$set": {"companyName": new_comp_name}}
            self.db.update_one(query, update)
        return

    def update_password(self, username, new_password):
        query = {"userName": username}
        if query is not None:
            update = {"$set": {"password": new_password}}
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
