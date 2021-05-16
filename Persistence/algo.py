import candidate_persistence as cd, company_persistence as cp, job_persistence as jb

def find_matches(candidate_id, job_id):
    candidate = cd.candidate(candidate_id)
    job       = jb.job(job_id)
    matches   = job.get_matches()
    tech_count, business_count, attitude_count = 0, 0, 0

    for skill in candidate.get_tech():
        if skill in job.get_tech():
            tech_count += 1
        
    for skill in candidate.get_business():
        if skill in job.get_business():
            business_count += 1
    
    for skill in candidate.get_attitude():
        if skill in job.get_attitude():
            attitude_count += 1
    
    total_score = tech_count + business_count + attitude_count
    if total_score > 0:
        if matches.size() < 10:
            matches.append({candidate.get_username() : total_score})
        elif matches.size() == 10:
            #check minimum score of last candidate
            min_score = matches[-1][1]
            #if score is lower than current candidate, replace in matches and sort
            if total_score > min_score:
                matches.del(-1)
                matches.append({candidate.get_username() : total_score})
        #sort matches
        #update best matches in DB
    else:
        #candidate is not match for job
        return