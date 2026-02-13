file=open("students.txt", "w")

name=input("Enter the student name: ")
usn=input("Enter student USN: ")
course=input("Enter the course: ")
dept=input("Enter the department:")

file.write("Name: " + name + "\n")
file.write("USN: " + usn + "\n")
file.write("Course: " + course + "\n")
file.write("Department: " + dept + "\n")

file.close()

print("Student record saved successfully.")
