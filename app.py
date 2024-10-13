import csv

# CSV file path
CSV_FILE = 'students.csv'

# 1. Load students from CSV file
def load_students():
    students = []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields back to appropriate types
                row["age"] = int(row["age"])
                row["score_math"] = float(row["score_math"])
                row["score_english"] = float(row["score_english"])
                row["score_afrikaans"] = float(row["score_afrikaans"])
                row["score_geography"] = float(row["score_geography"])
                row["score_life_orentation"] = float(row["score_life_orentation"])
                row["average_score"] = float(row["average_score"])
                students.append(row)
    except FileNotFoundError:
        print(f"No existing data. A new file '{CSV_FILE}' will be created.")
    return students

# 2. Save students to CSV file
def save_students(students):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ["name", "age", "score_math", "score_english", "score_afrikaans", 
                      "score_geography", "score_life_orentation", "average_score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

# Function to get valid marks (no changes needed)
def get_valid_mark(subject):
    while True:
        mark = float(input(f"Enter {subject} mark: "))
        if 0 <= mark <= 100:
            return mark
        else:
            print("Invalid mark. Please enter a mark between 0 and 100.")

# 3. Add a new student and save to CSV
def add_student(students):
    student_name = input("Name: ")
    student_age = int(input("Age: "))

    score_math = get_valid_mark("Math")
    score_english = get_valid_mark("English")
    score_afrikaans = get_valid_mark("Afrikaans")
    score_geography = get_valid_mark("Geography")
    score_life_orentation = get_valid_mark("Life Orientation")

    average_score = round(((score_math + score_english + score_afrikaans + score_geography + score_life_orentation) / 5), 2)

    student = {
        "name": student_name,
        "age": student_age,
        "score_math": score_math,
        "score_english": score_english,
        "score_afrikaans": score_afrikaans,
        "score_geography": score_geography,
        "score_life_orentation": score_life_orentation,
        "average_score": average_score
    }

    students.append(student)
    save_students(students)  # Save after adding
    print(f"Student '{student_name}' has been added and saved.")

# 4. View all students
def view_student(students):
    for student in students:
        print("----------------------------")
        print(
                f"Name: {student['name']}\n"
                f"Age: {student['age']}\n"
                f"Math: {student['score_math']}\n"
                f"English: {student['score_english']}\n"
                f"Afrikaans: {student['score_afrikaans']}\n"
                f"Geography: {student['score_geography']}\n"
                f"Life Orientation: {student['score_life_orentation']}\n"
                f"{student['name']}'s average is {student['average_score']}%"
            )
        print("----------------------------")

# 5. Update a student and save changes
def update_student(students):
    student_name = input("Enter the name of the student you want to update: ")

    for student in students:
        if student["name"] == student_name:
            print(f"Found student '{student_name}'")

            print("\nWhat would you like to update?")
            print("1: Name")
            print("2: Age")
            print("3: Math Score")
            print("4: English Score")
            print("5: Afrikaans Score")
            print("6: Geography Score")
            print("7: Life Orientation Score")

            choice = input("Select an option (1-7): ")

            if choice == "1":
                student["name"] = input("Enter a new name: ")
            elif choice == "2":
                student["age"] = int(input("Enter a new age: "))
            elif choice == "3":
                student["score_math"] = get_valid_mark("Math")
            elif choice == "4":
                student["score_english"] = get_valid_mark("English")
            elif choice == "5":
                student["score_afrikaans"] = get_valid_mark("Afrikaans")
            elif choice == "6":
                student["score_geography"] = get_valid_mark("Geography")
            elif choice == "7":
                student["score_life_orentation"] = get_valid_mark("Life Orientation")

            # Recalculate the average score after update
            student["average_score"] = round(
                (student["score_math"] + student["score_english"] + student["score_afrikaans"] +
                 student["score_geography"] + student["score_life_orentation"]) / 5, 2
            )

            save_students(students)  # Save the updated records
            print(f"Student '{student_name}' has been updated.")
            return

    print(f"Student '{student_name}' not found.")

# 6. Delete a student and save changes
def delete_student(students):
    student_name = input("Enter the name of the student to delete: ")

    for i, student in enumerate(students):
        if student["name"] == student_name:
            del students[i]
            save_students(students)  # Save the changes after deletion
            print(f"Student '{student_name}' deleted.")
            return
    print(f"Student '{student_name}' not found.")

# 7. Main program loop
def main_menu():
    students = load_students()  # Load students from CSV at the start
    while True:
        print("------------------")
        print("1: Add a new student")
        print("2: View all students")
        print("3: Update a student")
        print("4: Delete a student")
        print("5: Exit")
        print("------------------")

        choice = input("Select an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")

main_menu()
