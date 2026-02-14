file=input("Enter file name to read: ")

try:
    file=open(file, "r")

except FileNotFoundError:
    print("File does not exist!")

else:
    content=file.read()
    print("File Content:")
    print(content)
    file.close()
