import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"students": {}}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_student():
    name = input("Enter student name: ")
    subjects = {}

    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == "done":
            break
        marks = int(input(f"Enter marks for {subject}: "))
        subjects[subject] = marks

    data = load_data()
    data["students"][name] = subjects
    save_data(data)

    print("\nStudent data added successfully!\n")

def analyze_student():
    data = load_data()
    name = input("Enter student name to analyze: ")

    if name not in data["students"]:
        print("\nStudent not found.\n")
        return

    subjects = data["students"][name]
    total = sum(subjects.values())
    average = total / len(subjects)

    highest = max(subjects, key=subjects.get)
    lowest = min(subjects, key=subjects.get)

    print(f"\nReport for {name}")
    print("-------")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Scoring Subject: {highest} ({subjects[highest]})")
    print(f"Lowest Scoring Subject: {lowest} ({subjects[lowest]})\n")

def view_all_students():
    data = load_data()
    if not data["students"]:
        print("\nNo student records found.\n")
        return

    print("\nStudents:")
    for student in data["students"]:
        print("-", student)
    print()

def menu():
    while True:
        print(" STUDENT GRADE ANALYZER ")
        print("1. Add Student Marks")
        print("2. Analyze Student Performance")
        print("3. View All Students")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            analyze_student()
        elif choice == "3":
            view_all_students()
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
