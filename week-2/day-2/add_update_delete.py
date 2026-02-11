student={
     "name":"Madhu Shree R",
    "age":20,
    "usn":"1AH23CS076",
    "course":"Computer Science and Engineering",
    "class":"6th sem",
    "gender":"Female"
}

print("Original Dictionary:")
print(student)

student["usn"] = "1AH23CS076"
print("\nAfter Adding usn:")
print(student)

student["age"] = 21
print("\nAfter Updating age:")
print(student)

del student["course"]
print("\nAfter Deleting course:")
print(student)
