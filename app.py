from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/tasks")
def tasks():
    return render_template("tasks.html")


@app.route("/subjects")
def subjects():
    return render_template(
        "placeholder.html",
        page_title="Subjects",
        description="Manage your college subjects here."
    )


@app.route("/timetable")
def timetable():
    return render_template(
        "placeholder.html",
        page_title="Timetable",
        description="Your weekly class schedule will appear here."
    )


@app.route("/attendance")
def attendance():
    return render_template(
        "placeholder.html",
        page_title="Attendance",
        description="Track your class attendance here."
    )


@app.route("/exams")
def exams():
    return render_template(
        "placeholder.html",
        page_title="Exams",
        description="Manage your upcoming examinations here."
    )


if __name__ == "__main__":
    app.run(debug=True)
