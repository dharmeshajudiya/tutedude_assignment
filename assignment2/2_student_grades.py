students = {}

is_running = True

while is_running:
    print("--------------------")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. View Students")
    print("4 Exit")
    print("--------------------")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print(f"Student {name} added with grade {grade}")
        print("--------------------")
    
    if choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"Student {name} updated with new grade {grade}")
            print("--------------------")
        else:
            print(f"Student {name} not found")
            print("--------------------")
    
    if choice == 3:
        print("Student Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")   
        print("--------------------")
    if choice == 4:
        is_running = False
        print("Exiting...")
        print("--------------------")
