import csv
import pandas as pd

# CSV file path
CSV_FILE = 'students.csv'

# sets pandas to read from students.csv 
students_stats = pd.read_csv('students.csv')

# Load students from CSV file
def load_students():
    students = []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields back to appropriate types
                row["age"] = int(row["age"])
                row["math_score"] = float(row["math_score"])
                row["english_score"] = float(row["english_score"])
                row["afrikaans_score"] = float(row["afrikaans_score"])
                row["geography_score"] = float(row["geography_score"])
                row["life_orientation_score"] = float(row["life_orientation_score"])
                students.append(row)
    except FileNotFoundError:
        print(f"No existing data. A new file '{CSV_FILE}' will be created.")
    return students

# Save students to CSV file
def save_students(students):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ["name", "age", "math_score", "english_score", "afrikaans_score", 
                      "geography_score", " life_orientation_score", "average_score"]
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

# Add a new student and save to CSV
def add_student(students):
    student_name = input("Name: ")
    student_age = int(input("Age: "))

    math_score = get_valid_mark("Math")
    english_score = get_valid_mark("English")
    afrikaans_score = get_valid_mark("Afrikaans")
    geography_score = get_valid_mark("Geography")
    life_orientation_score = get_valid_mark("Life Orientation")

    average_score = round(((math_score + english_score + afrikaans_score + geography_score + life_orientation_score) / 5), 2)

    student = {
        "name": student_name,
        "age": student_age,
        "math_score": math_score,
        "english_score": english_score,
        "afrikaans_score": afrikaans_score,
        "geography_score": geography_score,
        "life_orientation_score": life_orientation_score,
        "average_score": average_score
    }

    students.append(student)
    save_students(students)  # Save after adding
    print(f"Student '{student_name}' has been added and saved.")

# View all students
def view_student(students):
    for student in students:
        print("----------------------------")
        print(
                f"Name: {student['name']}\n"
                f"Age: {student['age']}\n"
                f"Math: {student['math_score']}\n"
                f"English: {student['english_score']}\n"
                f"Afrikaans: {student['afrikaans_score']}\n"
                f"Geography: {student['geography_score']}\n"
                f"Life Orientation: {student['score_life_orentation']}\n"
                f"{student['name']}'s average is {student['average_score']}%"
            )
        print("----------------------------")

# Update a student and save changes
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
                student["math_score"] = get_valid_mark("Math")
            elif choice == "4":
                student["english_score"] = get_valid_mark("English")
            elif choice == "5":
                student["afrikaans_score"] = get_valid_mark("Afrikaans")
            elif choice == "6":
                student["geography_score"] = get_valid_mark("Geography")
            elif choice == "7":
                student["score_life_orentation"] = get_valid_mark("Life Orientation")

            # Recalculate the average score after update
            student["average_score"] = round(
                (student["math_score"] + student["english_score"] + student["afrikaans_score"] +
                 student["geography_score"] + student["score_life_orentation"]) / 5, 2
            )

            save_students(students)  # Save the updated records
            print(f"Student '{student_name}' has been updated.")
            return

    print(f"Student '{student_name}' not found.")

# Delete a student and save changes
def delete_student(students):
    student_name = input("Enter the name of the student to delete: ")

    for i, student in enumerate(students):
        if student["name"] == student_name:
            del students[i]
            save_students(students)  # Save the changes after deletion
            print(f"Student '{student_name}' deleted.")
            return
    print(f"Student '{student_name}' not found.")
    
# Show some basic statistics for students in the database
def show_statistics(students):
    if not students:
        print("No students found in the database.")
        return

    total_students = len(students)
    total_age = sum(student["age"] for student in students)
    average_age = round(total_age / total_students, 2)

    total_math_score = sum(student["math_score"] for student in students)
    average_math_score = round(total_math_score / total_students, 2)

    total_english_score = sum(student["english_score"] for student in students)
    average_english_score = round(total_english_score / total_students, 2)

    total_afrikaans_score = sum(student["afrikaans_score"] for student in students)
    average_afrikaans_score = round(total_afrikaans_score / total_students, 2)
    
    total_geography_score = sum(student["geography_score"] for student in students)
    average_geography_score = round(total_geography_score / total_students, 2)
    
    total_life_orientation_score = sum(student["life_orientation_score"] for student in students)
    average_life_orientation_score = round(total_life_orientation_score / total_students, 2)
    
    
    
    print(f"Total number of students: {total_students}")
    print(f"Average age: {average_age}%")
    print(f"Average Math Score: {average_math_score}%")
    print(f"Average English Score: {average_english_score}%")
    print(f"Average Afrikaans Score: {average_afrikaans_score}%")
    print(f"Average Geography Score: {average_geography_score}%")
    print(f"Average Life Orientation Score: {average_life_orientation_score}%")
    

# Main program loop
def main_menu():
    students = load_students()  # Load students from CSV at the start
    while True:
        print("------------------")
        print("1: Add a new student")
        print("2: View all students")
        print("3: Update a student")
        print("4: Delete a student")
        print("5: Show statistics")
        print("6: Exit")
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
            show_statistics(students)
        elif choice == "6":
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")

main_menu()
