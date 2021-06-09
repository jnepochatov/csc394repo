from flask import Flask, render_template, Blueprint,redirect, url_for, request, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from login import cand_login, hash_text, comp_login
from Persistence.candidate import CandidateObject
from Persistence.company import CompanyObject


app = Flask(__name__)
candidates = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.Candidate
jobs = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.Job
companies = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.Company


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/candidate_profile/<username>')
def candidate_profile(username):
    candidate = candidates.find({"userName": username})
    for info in candidate:
        name = info["name"]
        email = info["email"]
        phoneNum = info["phoneNum"]
        references = info["references"]
        tech_skills = info["tech_skills"]
        business_skills = info["business_skills"]
        att_skills = info["attitude"]

    return render_template("candidate_profile.html", username=username, name=name, email=email,
                           phoneNum=phoneNum, refences=references, tech_skills=tech_skills,
                           business_skills=business_skills, att_skills=att_skills)


@app.route('/candidate_login', methods=['GET', 'POST'])
def candidate_login():
    if request.method == 'POST':
        username = request.form.get('username').lower()
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        valid = cand_login(username, password)
        if not valid:
            flash("Please check your login details and try again.")
            return redirect(url_for('candidate_login'))
        return redirect(url_for('candidate_profile', username=username))
    else:
        return render_template('candidate_login.html')

@app.route('/company_login', methods=['GET', 'POST'])
def company_login():
    if request.method == 'POST':
        username = request.form.get('username').lower()
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        valid = comp_login(username, password)
        if not valid:
            flash("Please check your login details and try again.")
            return redirect(url_for('company_login'))
        return redirect(url_for('company_profile', username=username))
    else:
        return render_template('company_login.html')

@app.route('/candidate_signup', methods=['GET', 'POST'])
def candidate_signup():
    if request.method == 'POST':
        username = request.form.get('username')

        password = request.form.get('password')
        hashed_password = hash_text(password)
        email = request.form.get('email')
        name = request.form.get('name')
        phoneNum = request.form.get('phoneNum')
        references = request.form.get('references').strip().replace(' ', '').split(',')
        #for the checkboxes
        tech_skills = request.form.getlist('techSkill')
        business_skills = request.form.getlist('businessSkill')
        attitude_skills = request.form.getlist('attitudeSkill')
        #tech_skills = request.form.get('tech_skills').strip().replace(' ', '').split(',')
        #business_skills = request.form.get('business_skills').strip().replace(' ', '').split(',')
        #attitude_skills = request.form.get('attitude_skills').strip().replace(' ', '').split(',')
        if username == "" or password == "" or email == "":
            flash("Incorrect signup details.")
            return redirect(url_for('candidate_signup'))
        else:
            candidate = CandidateObject(username, hashed_password,email, name, phoneNum, references, tech_skills, business_skills, attitude_skills, list())
            candidate.create()
            return redirect(url_for('candidate_login'))
    else:
        return render_template('candidate_signup.html')

@app.route('/company_signup', methods=['GET', 'POST'])
def company_signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = hash_text(password)
        company_name = request.form.get('company_name')
        email = request.form.get('email')
        phoneNum = request.form.get('phoneNum')
        if username == "" or password == "" or email == "":
            flash("Incorrect signup details.")
            return redirect(url_for('company_signup'))
        else:
            company = CompanyObject(company_name, email, phoneNum, username, hashed_password, list())
            company.create()
            return redirect(url_for('company_login'))
    else:
        return render_template('company_signup.html')

@app.route('/company_profile/<username>')
def company_profile(username):
    company = companies.find({"userName": username})

    for info in company:
        userName = info["userName"]
        companyName = info["companyName"]
        email = info["email"]
        phoneNum = info["phoneNum"]
        jobList = info['job_list']

    return render_template('company_profile.html', userName=userName, companyname=companyName, email=email, phoneNum=phoneNum)

@app.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    return redirect(url_for('login'))

@app.route('/job/<username>/<j_id>')
def job(username, j_id):
    j = jobs.find({"j_id": j_id})
    #jobName = job['jobName']

    for info in j:
        jobName = info['jobName']
        jobRole = info['jobRole']
        jobDescription = info['jobDescription']
        techSkills= info['tech_skills']
        businessSkills = info['business_skills']
        attSkills = info['attitude']

    return render_template("job.html", username=username, jobName=jobName, jobRole=jobRole, jobDescription=jobDescription,
                           techSkills=techSkills, businessSkills=businessSkills, attSkills=attSkills)

@app.route('/<username>/add_job', methods=['GET', 'POST'])
def add_job(username):
    n = jobs.count_documents({})
    company = companies.find({"username": username})
    for info in company:
        j_list = info["job_list"]
    if request.method == 'POST':
        j_id = n+1
        job_name = request.form('job_name')
        job_role = request.form('job_role')
        job_description = request.form('job_description')
        tech_skills = request.form('tech_skills')
        business_skills = request.form('business_skills')
        attitude_skills = request.form('attitude_skills')
        best_match = list()

        if job_name == "" or job_role == "" or job_description == "" or tech_skills == "" or business_skills == "" or attitude_skills == "":
            flash("Please enter information in every field")
            return redirect((url_for('add_job', username=username)))

        j_list.append(j_id)
        query = {"userName": username}
        if query is not None:
            update = {"$set": {"job_list": j_list}}
            companies.update_one(query, update)
            return redirect(url_for('job', username=username, j_id=j_id))
    else:
        return render_template('add_job.html')

    return str(n)

@app.route('/job_list')
def job_list():
    job_list = list(jobs.find())
    return render_template('job_list.html', job_list=job_list)

@app.route('/logout')
def logout():
    return 'Logout'

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)
