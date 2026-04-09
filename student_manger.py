def load_students(filename):
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                students.append({"name": name, "score": int(score)})
    except FileNotFoundError:
        print("No existing file found. Starting fresh.")
    return students

def add_student(students):
    name = input("Enter student name: ")
    score = input("Enter student score: ")
    students.append({"name": name, "score": int(score)})
    print(f"{name} added successfully!")

def view_students(students):
    if len(students) == 0:
        print("No students on record yet.")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print(f"{student['name']} - {student['score']}")
        print("--------------")

def save_students(filename, students):
    with open(filename, "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['score']}\n")
    print("Data saved successfully.")

def main():
    filename = "student.txt"
    students = load_students(filename)
    while True:
        print("\n---Student Manager ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Choose and option (1-3): ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            save_students(filename, students)
            print("Goodbye!")
            break 
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()
