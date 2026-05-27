students = []
def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course Name: ")

    student = {
        "name":name,
        "age":age,
        "course":course
    }
    students.append(student)
    print("Student Added Successfully\n")
def view_students():
    if len(students) == 0:
        print("No Students found\n")
    else:
        print("\nStudents List")
        for i,Student in enumerate(students,start=1):
            print(f"{i}.Name: {Student['name']}, Age: {Student['age']}, Course: {Student['course']}")
            print()

def search_student():
    search_name = input("Enter Student Name to search:")
    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print("Student Found")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}\n")
            found = True

        if not found:
            print("Student Not Found\n")
def delete_student():
    delete_name= input("Enter Student Name to delete:")
    for student in students:
        if student["name"].lower() == delete_name.lower():
            students.remove(student)
            print("Student Deleted Successfully\n")
            return

        print("Student Not Found\n")

while True:
    print("===== Student Management System =====")
    print("1.Add Student")
    print("2.View Student")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("program closed")
        break
    else:
        print("Invalid Choice")
