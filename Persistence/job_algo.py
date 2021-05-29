import candidate_persistence as cd, job_persistence as jb
from pymongo import MongoClient
from bson.objectid import ObjectId

def find_matches(job_id):
    client = MongoClient("mongodb+srv://jryan52:password1234@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    cursor = client.myFirstDatabase.Candidate.find({})

    job       = jb.job(job_id)
    j_tech    = [x.lower() for x in job.get_tech()]
    j_biz     = [x.lower() for x in job.get_business()]
    j_att     = [x.lower() for x in job.get_attitude()]
    j_matches = job.get_matches()
    
    matches = []

    if len(j_matches) > 0:
        for match in j_matches:
                var_set = (match[0], int(match[1]))
                matches.append(var_set)


    for doc in cursor:
        candidate_id = doc["_id"]
        candidate = cd.candidate(candidate_id)
        c_tech    = [x.lower() for x in candidate.get_tech()]
        c_biz     = [x.lower() for x in candidate.get_business()]
        c_att     = [x.lower() for x in candidate.get_attitude()]
        c_name    = candidate.get_username()

        tech_count, business_count, attitude_count = 0, 0, 0

        for skill in c_tech:
            if skill in j_tech:
                tech_count += 1
            
        for skill in c_biz:
            if skill in j_biz:
                business_count += 1
        
        for skill in c_att:
            if skill in j_att:
                attitude_count += 1
        
        total_score = tech_count + business_count + attitude_count

        if total_score > 0 and (c_name, total_score) not in matches:
            
            if len(matches) < 10:
                matches.append((c_name, total_score))
                
            elif len(matches) == 10:
                #check minimum score of last candidate
                min_score = matches[-1][1]
                #if score is lower than current candidate, replace in matches and sort
                if total_score > min_score:
                    del matches[-1]
                    matches.append((c_name, total_score))

            matches.sort(key = lambda x: x[1], reverse=True)

    if matches != None: 
        matches = list(matches)       
        job.db.update_one({"_id" : ObjectId(job_id)}, { "$set" : {"bestMatch" : matches}})

#find_matches("60a97ff7fc1c5254e872f38a")