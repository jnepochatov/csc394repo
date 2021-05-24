from Persistence.data_retrieve import data_retrieve

class company(data_retrieve):
    def __init__(self, _id):
        data_retrieve.__init__(self, _id)
        self._id = _id
        self.db  = self.client.myFirstDatabase.Company

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