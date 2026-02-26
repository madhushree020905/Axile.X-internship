import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

print("Table created successfully!")

students_data = [
    ("Madhu Shree", 20, "Python"),
    ("Rahul", 22, "Java"),
    ("Ananya", 19, "C++"),
    ("Vikram", 21, "Web Development"),
    ("Sneha", 23, "Data Science")
]

cursor.executemany(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    students_data
)

conn.commit()
print("Multiple records inserted successfully!")

print("\nStudent Records:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("UPDATE students SET age = ? WHERE name = ?", (24, "Rahul"))
conn.commit()
print("\nRahul's age updated!")

cursor.execute("DELETE FROM students WHERE name = ?", ("Ananya",))
conn.commit()
print("Ananya's record deleted!")

print("\nFinal Student Records:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()