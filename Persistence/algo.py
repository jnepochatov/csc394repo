import candidate_persistence as cd, company_persistence as cp, job_persistence as jb
from pymongo import MongoClient
from bson.objectid import ObjectId

#Take out job_id and make script to call all jobs when a new candidate is created

def find_matches(candidate_id, job_id):
    candidate = cd.candidate(candidate_id)
    c_tech    = candidate.get_tech()
    c_biz     = candidate.get_business()
    c_att     = candidate.get_attitude()
    c_matches = candidate.get_matches()

    job       = jb.job(job_id)
    j_tech    = job.get_tech()
    j_biz     = job.get_business()
    j_att     = job.get_attitude()
    j_matches = job.get_matches()

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
    print(total_score)
    if total_score > 0:
        if j_matches.size() < 10:
            j_matches.append({candidate.get_username() : total_score})
            j_matches = sorted(j_matches, key = lambda x: x[1])
            print(j_matches)
        elif j_matches.size() == 10:
            #check minimum score of last candidate
            min_score = j_matches[-1][1]
            #if score is lower than current candidate, replace in matches and sort
            if total_score > min_score:
                del j_matches[-1]
                j_matches.append({candidate.get_username() : total_score})
                j_matches = sorted(j_matches, key = lambda x: x[1])
                print(j_matches)
        job.db.replace_one({"_id" : ObjectId(job_id)}, {"bestMatch" : j_matches})
    else:
        #candidate is not match for job
        return