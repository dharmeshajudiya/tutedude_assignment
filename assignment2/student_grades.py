students = {
    "John": 'A',
    "Jane": 'B',
    "Jack": 'C',
    "Jill": 'D',
    "Joe": 'F'
}

for student, grade in students.items():
    print(f"{student}: {grade}")

print("Adding a new student")
name = input("Enter student name: ")
grade = input("Enter student grade: ")
students[name] = grade

print("Updated student list:")
for student, grade in students.items():
    print(f"{student}: {grade}")

print("Update a student's grade")
name = input("Enter student name to update: ")
grade = input("Enter new grade: ")
students[name] = grade

print("Final student list:")
for student, grade in students.items(): 
    print(f"{student}: {grade}")
