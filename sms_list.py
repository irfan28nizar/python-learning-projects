students=[]
def show():
    if not students:
        print("No students found")
    else:
        print(students)
def add_student(name):
    students.append(name)
    print(f"{name} added")
def remove_student(name):
    if name in students:
        students.remove(name)
        print(f"{name} removed")
    else:
        print(f"{name} not found")
def main():
    while True:
        print("1. Show students")
        print("2. Add student")
        print("3. Remove student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            show()
        elif choice == '2':
            name = input("Enter student name to add: ")
            add_student(name)
        elif choice == '3':
            name = input("Enter student name to remove: ")
            remove_student(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")
main()