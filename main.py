from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("classroom.html", content=["one","another"])

if __name__ == "__main__":
    app.run()