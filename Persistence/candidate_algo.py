import Persistence.candidate_persistence as cd, Persistence.company_persistence as cp, Persistence.job_persistence as jb
from pymongo import MongoClient
from bson.objectid import ObjectId

def find_matches(candidate_id):
    client = MongoClient("mongodb+srv://jryan52:password1234@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    cursor = client.myFirstDatabase.Job.find({})

    candidate = cd.candidate(candidate_id)
    c_tech    = [x.lower() for x in candidate.get_tech()]
    c_biz     = [x.lower() for x in candidate.get_business()]
    c_att     = [x.lower() for x in candidate.get_attitude()]
    
    matches = []

    if len(candidate.get_matches()) > 0:
        for match in candidate.get_matches():
                var_set = (match[0], int(match[1]))
                matches.append(var_set)

    for doc in cursor:
        job_id = doc["_id"]
        job       = jb.job(job_id)
        j_tech    = [x.lower() for x in job.get_tech()]
        j_biz     = [x.lower() for x in job.get_business()]
        j_att     = [x.lower() for x in job.get_attitude()]

        tech_count, business_count, attitude_count = 0, 0, 0

        for skill in j_tech:
            if skill in c_tech:
                tech_count += 1
            
        for skill in j_biz:
            if skill in c_biz:
                business_count += 1
        
        for skill in j_att:
            if skill in c_att:
                attitude_count += 1
        
        total_score = tech_count + business_count + attitude_count
        if total_score > 0:
            if len(matches) < 10:
                matches.append((job_id, total_score))
                matches.sort(key = lambda x: x[1], reverse=True)
            elif len(matches) == 10:
                #check minimum score of last candidate
                min_score = matches[-1][1]
                #if score is lower than current candidate, replace in matches and sort
                if total_score > min_score:
                    del matches[-1]
                    matches.append((job_id, total_score))
                    matches = matches.sort(key = lambda x: x[1])
            candidate.db.update_one({"_id" : ObjectId(candidate_id)}, { "$set" : {"bestMatch" : matches}})