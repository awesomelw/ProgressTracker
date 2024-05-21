from flask import Flask, redirect, render_template
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.db'
# db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("classroom.html", content=["one","another"])

@app.route("/details")
def details():
    return render_template("details.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html", progress=80, players=3)

if __name__ == "__main__":
    app.run()