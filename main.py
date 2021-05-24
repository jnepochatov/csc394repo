from flask import Flask, render_template, Blueprint,redirect, url_for, request, flash
from flask_login import LoginManager, login_user
from pymongo import MongoClient
from bson.objectid import ObjectId
from login import candidate_login


app = Flask(__name__)
candidates = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.Candidate
jobs = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.Job
companies = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.Company


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/candidate/<username>')
def candidate_profile(username):
    candidate = candidates.find({"userName": username})

    for info in candidate:
        name = info["name"]
        email = info["email"]
        phoneNum = info["phoneNum"]
        techSkills = info["tech_skills"]

    return render_template("candidate.html", username=username, name=name, email=email, phoneNum=phoneNum, techSkills=techSkills)

@app.route('/job/<job_id>')
def job(job_id):
    job = jobs.find({"_id": ObjectId(job_id)})
    #jobName = job['jobName']

    for info in job:
        jobName = info['jobName']
        jobRole = info['jobRole']
        jobDescription = info['jobDescription']
        techSkills= info['tech_skills']
        businessSkills = info['business_skills']
        attSkills = info['attitude']

    return render_template("job.html", jobName=jobName, jobRole=jobRole, jobDescription=jobDescription,
                           techSkills=techSkills, businessSkills=businessSkills, attSkills=attSkills)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        valid = candidate_login(username, password)
        if not valid:
            flash("Please check your login details and try again.")
            return redirect(url_for('login'))
        return redirect(url_for('candidate_profile', username=username))
    else:
        return render_template('login.html')

@app.route('/candidate_signup', methods=['GET', 'POST'])
def candidate_signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        name = request.form.get('name')
        phoneNum = request.form.get('phoneNum')
        references = request.form.get('references')
        tech_skills = request.form.get('tech_skills')
        business_skills = request.form.get('business_skills')
        attitude_skills = request.form.get('attitude_skills')
        return redirect(url_for('login'))
    else:
        return render_template('candidate_signup.html')

@app.route('/company_signup', methods=['GET', 'POST'])
def company_signup():

    return render_template('company_signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    return 'Logout'

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)