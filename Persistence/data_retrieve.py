from pymongo import MongoClient
from bson.objectid import ObjectId

class data_retrieve:
    def __init__(self, _id):
        self._id = _id
        self.client = MongoClient("mongodb+srv://jryan52:password1234@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    def open_connection(self, var):
        for result in self.db.find({"_id": ObjectId(self._id)}, {var: 1}):
            variable = result[var]
        return variable
    
    def close_connection(self):
        self.client.close()
    
    def get_matches(self):
        try:
            var = self.open_connection("bestMatch")
            self.best = var
            self.close_connection()
            return self.best
        except:
            return "Might not have matches yet"