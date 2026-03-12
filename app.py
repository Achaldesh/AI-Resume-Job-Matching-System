from flask import Flask, render_template, request
from matcher import match_resumes

app = Flask(__name__)

resumes = [
    "Python developer with machine learning and data analysis skills using pandas numpy and sklearn",
    "Java backend developer with spring boot microservices and API development"
]

@app.route("/", methods=["GET","POST"])
def index():
    scores = []

    if request.method == "POST":
        job_desc = request.form["job"]
        scores = match_resumes(job_desc, resumes)
        scores = list(scores)

    return render_template("index.html", scores=scores)

if __name__ == "__main__":
    app.run(debug=True)