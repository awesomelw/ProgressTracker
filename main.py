from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class StudentHomework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String, unique=False, nullable=False)
    hwCompletedPercent = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self
    
@app.route("/")
def home():
    students = db.session.execute(text('SELECT studentname, hwCompletedPercent FROM student_homework'))
    studentlist = []
    for i in students:
        student = {"student":i[0],"progress":i[1]}
        studentlist.append(student)
    return render_template("classroom.html", students=studentlist)


@app.route("/details")
def details():
    return render_template("details.html")


@app.route("/leaderboard")
def leaderboard():
    students = db.session.execute(text('SELECT studentname, hwCompletedPercent FROM student_homework ORDER BY hwCompletedPercent DESC'))
    studentlist = []
    for i in students:
        student = {"student":i[0],"progress":i[1]}
        studentlist.append(student)
    # print(studentlist) # type list of dicts
    # print(studentlist[0]['student']) # type str 
    # print(studentlist[0]['progress']) # type str
    return render_template("leaderboard.html", students=studentlist)


@app.route("/create")
def create():
    sql = db.session.execute(text('INSERT INTO student_homework(studentname,hwCompletedPercent) VALUES ("John", 72)'))
    db.session.commit()
    return "Done"
<<<<<<< Updated upstream

@app.route("/cmd/<command>")
def command(command):
    yep = f'select {command} from student_homework'
    print("="*50)
    print(yep)
    sql = db.session.execute(text(yep))
    return sql
=======
>>>>>>> Stashed changes


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run()