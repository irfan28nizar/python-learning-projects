students={}
def show():
    if not students:
        print("No students found")
    else:
        print("Student_name : Score")
        for name, score in students.items():
            print(f"{name} : {score}")
def add_student(name, score):
    students[name] = score
    print(f"{name} added with score {score}")
def remove_student(name):
    if name in students:
        del students[name]
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
            if not name:
                print("Invalid name. Please enter a non-empty name.")
                continue
            elif not name.isalpha():
                print("Invalid name. Please enter alphabetic characters only.")
                continue
            elif name in students:
                print("Student already exists.")
                continue
            else:
                score = input("Enter student score: ")
                if not score.isdigit():
                    print("Invalid score. Please enter a numeric value.")
                    continue
                else:
                    add_student(name, int(score))
        elif choice == '3':
            name = input("Enter student name to remove: ")
            remove_student(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")
main()

