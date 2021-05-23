from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)
candidates = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase.Candidate


@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/candidate/<username>')
def candidate(username):
    candidate = candidates.find({"userName": username})

    for info in candidate:
        name = info["name"]
        email = info["email"]
        phoneNum = info["phoneNum"]
        techSkills = info["tech_skills"]



    return render_template("candidate.html", username=username, name=name, email=email, phoneNum=phoneNum, techSkills=techSkills)

if __name__ == "__main__":
    app.run(debug=True)