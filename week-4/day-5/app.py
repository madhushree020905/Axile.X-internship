from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create users table
conn = get_db_connection()
conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# Insert a default user (only once)
conn.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
             ("admin", "1234"))
conn.commit()
conn.close()

# Login page
@app.route("/")
def login():
    return render_template("login.html")

# Handle login
@app.route("/login", methods=["POST"])
def handle_login():
    username = request.form["username"]
    password = request.form["password"]

    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    ).fetchone()
    conn.close()

    if user:
        return redirect("/dashboard")
    else:
        return render_template("login.html", error="Invalid Username or Password")

# Dashboard page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)