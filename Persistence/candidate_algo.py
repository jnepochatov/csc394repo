import Persistence.candidate_persistence as cd, Persistence.job_persistence as jb
from pymongo import MongoClient
from bson.objectid import ObjectId

def find_matches(candidate_id):
    #Connect to the database
    client = MongoClient("mongodb+srv://jryan52:password1234@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    #Create a cursor to scroll through all available jobs
    cursor = client.myFirstDatabase.Job.find({})
    #Create candidate object using ObjectId
    candidate = cd.candidate(candidate_id)
    c_tech    = [x.lower() for x in candidate.get_tech()]
    c_biz     = [x.lower() for x in candidate.get_business()]
    c_att     = [x.lower() for x in candidate.get_attitude()]
    c_matches = candidate.get_matches()
    #Create matches array
    matches = []

    if len(c_matches) > 0:
        for match in c_matches:
                var_set = (match[0], int(match[1]))
                matches.append(var_set)
    #Scroll through cursor and check if jobs align with candidates various skills
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
        #Create total score
        total_score = tech_count + business_count + attitude_count
        
        if total_score > 0 and (job_id, total_score) not in matches:
            #If the candidate doesn't have 10 matches yet, add the job to the match list
            if len(matches) < 10:
                matches.append((job_id, total_score))

            #If the candidate already has a list of 10 matches
            elif len(matches) == 10:
                #check minimum score of last candidate
                min_score = matches[-1][1]
                #if score is higher than current last place job, replace in matches and sort
                if total_score > min_score:
                    del matches[-1]
                    matches.append((job_id, total_score))
            matches = matches.sort(key = lambda x: x[1])
    #Update the best matches list in the database
    candidate.db.update_one({"_id" : ObjectId(candidate_id)}, { "$set" : {"bestMatch" : matches}})

#find_matches("60ac7f921ab56f248fd12fe0")