from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # establishes database connect to sqlite
db = SQLAlchemy(app)

class StudentHomework(db.Model):    # Creates table in database called student_homework
    id = db.Column(db.Integer, primary_key=True)    # first column of table
    studentname = db.Column(db.String, unique=False, nullable=False)    # second column of table
    hwCompletedPercent = db.Column(db.Integer, nullable=False)    # third column of table

    def __repr__(self):
        return self
    
@app.route("/")    # Web path for classroom.html file (127.0.0.1:5000/)
def home():
    students = db.session.execute(text('SELECT studentname, hwCompletedPercent FROM student_homework'))    # queries student_homework table for the student name and their progress
    studentlist = []                                  #  these lines of code iterate over,
    for i in students:                                #  every result from the table query,
        student = {"student":i[0],"progress":i[1]}    #  and puts it into a dictionary,
        studentlist.append(student)                   #  and then into a list for easy parsing,
    return render_template("classroom.html", students=studentlist)    # this renders the classroom.html file when a student goes to the / web path


@app.route("/details")    # Web path for details.html file (127.0.0.1:5000/details)
def details():
    return render_template("details.html")    # this renders the details.html file


@app.route("/leaderboard")
def leaderboard():
    students = db.session.execute(text('SELECT studentname, hwCompletedPercent FROM student_homework ORDER BY hwCompletedPercent DESC'))    # Same as earlier table query but just sorts it
    studentlist = []
    for i in students:                                    # same stuff as in the home() function
        student = {"student":i[0],"progress":i[1]}
        studentlist.append(student)
    return render_template("leaderboard.html", students=studentlist)


@app.route("/create")  # navigating to this web page will insert all these values into your database
def create():
    sql = db.session.execute(text('UPDATE student_homework(studentname,hwCompletedPercent) VALUES ("Candice", 58), ("Dontrell", 63), ("Eren", 28), ("Faith", 48), ("Gordon", 68), ("Harry", 55), ("Jonathan", 64)'))
    db.session.commit()
    return "Done"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)