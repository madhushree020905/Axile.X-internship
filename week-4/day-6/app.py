from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
""")
conn.commit()
conn.close()

@app.route("/")
def view():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("view.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
            (name, age, course)
        )
        conn.commit()
        conn.close()
        return redirect("/")

    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    ).fetchone()

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        conn.execute(
            "UPDATE students SET name=?, age=?, course=? WHERE id=?",
            (name, age, course, id)
        )
        conn.commit()
        conn.close()
        return redirect("/")

    conn.close()
    return render_template("edit.html", student=student)

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    conn = get_db_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    ).fetchone()

    if request.method == "POST":
        conn.execute("DELETE FROM students WHERE id=?", (id,))
        conn.commit()
        conn.close()
        return redirect("/")

    conn.close()
    return render_template("delete.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)