from flask import Flask, redirect, render_template
<<<<<<< Updated upstream
# from flask_sqlalchemy import SQLAlchemy
=======
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import json
>>>>>>> Stashed changes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database2.db'
db = SQLAlchemy(app)

class StudentHomework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String, unique=False, nullable=False)
    hwCompletedPercent = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self
    
def resultParser(userinput):
    mylist = []
    for tmp in userinput:
        for i in tmp:
            i.split("'")
            mylist.append(i)
    return mylist

@app.route("/")
def home():
    return render_template("classroom.html", content=["one","another"])

@app.route("/details")
def details():
    return render_template("details.html")

@app.route("/leaderboard")
def leaderboard():
    result = db.session.execute(text('select studentname from student_homework'))
    players = resultParser(result)
    return render_template("leaderboard.html", progress=80, players=players)

@app.route("/create")
def create():
    sql = db.session.execute(text('INSERT INTO student_homework(studentname,hwCompletedPercent) VALUES ("Bob2", "16")'))
    db.session.commit()
    return "Done"
@app.route("/cmd/<command>")
def command(command):
    yep = f'select {command} from student_homework'
    print("="*50)
    print(yep)
    sql = db.session.execute(text(yep))
    return sql

@app.route("/seeall")
def name():
    result = db.session.execute(text('select studentname from student_homework'))
    return resultParser(result)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run()