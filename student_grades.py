def add_student(grades):
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    grades[name] = grade

def display_grades(grades):
    print("Student Grades:")
    for name, grade in grades.items():
        print(f"{name}: {grade}")

def main():
    grades = {}
    while True:
        print("1. Add Student")
        print("2. Display Grades")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_student(grades)
        elif choice == "2":
            display_grades(grades)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")

main()
