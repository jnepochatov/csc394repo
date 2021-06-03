from pymongo import MongoClient
from bson.objectid import ObjectId

client   = MongoClient("mongodb+srv://jryan52:password1234@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db       = client.myFirstDatabase

def tech_filter(query_list, collection):
    connection  = db[collection]
    result      = connection.find({"tech_skills" : {"$all" : query_list}})
    results     = []
    for x in result:
        results.append(x["_id"])
    client.close()
    return results

def business_filter(query_list, collection):
    connection  = db[collection]
    result      = connection.find({"business_skills" : {"$all" : query_list}})
    results     = []
    for x in result:
        results.append(x["_id"])
    client.close()
    return results

def attitude_filter(query_list, collection):
    connection  = db[collection]
    result      = connection.find({"attitude" : {"$all" : query_list}})
    results     = []
    for x in result:
        results.append(x["_id"])
    client.close()
    return results