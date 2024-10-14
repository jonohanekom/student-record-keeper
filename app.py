import csv
import pandas as pd

# CSV file path
CSV_FILE = 'students.csv'

# Read CSV file
df = pd.read_csv(CSV_FILE)

# Function to get valid marks
def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} mark: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid mark. Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Add a new student and save to CSV
def add_student():
    student_name = input("Name: ")
    student_age = int(input("Age: "))

    math_score = get_valid_mark("Math")
    english_score = get_valid_mark("English")
    afrikaans_score = get_valid_mark("Afrikaans")
    geography_score = get_valid_mark("Geography")
    life_orientation_score = get_valid_mark("Life Orientation")

    # Calculate the average of the new student
    average_score = round((math_score + english_score + afrikaans_score + geography_score + life_orientation_score) / 5, 2)

    # Append the student directly to the CSV file
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_name, student_age, math_score, english_score, afrikaans_score, geography_score, life_orientation_score, average_score])

    print(f"Student '{student_name}' has been added and saved.")

# View all students from CSV file
def view_students():
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    print("----------------------------")
                    print(f"Name: {row[0]}\nAge: {row[1]}\nMath: {row[2]}\nEnglish: {row[3]}\nAfrikaans: {row[4]}\nGeography: {row[5]}\nLife Orientation: {row[6]}\nAverage: {row[7]}%")
                    print("----------------------------")
    except FileNotFoundError:
        print("No student records found.")

# Update a student
def update_student():
    student_name = input("Enter the name of the student you want to update: ")
    updated = False

    try:
        with open(CSV_FILE, mode='r') as file:
            students = list(csv.reader(file))
        
        for row in students:
            if row and row[0] == student_name:
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
                    row[0] = input("Enter a new name: ")
                elif choice == "2":
                    row[1] = int(input("Enter a new age: "))
                elif choice == "3":
                    row[2] = get_valid_mark("Math")
                elif choice == "4":
                    row[3] = get_valid_mark("English")
                elif choice == "5":
                    row[4] = get_valid_mark("Afrikaans")
                elif choice == "6":
                    row[5] = get_valid_mark("Geography")
                elif choice == "7":
                    row[6] = get_valid_mark("Life Orientation")

                # Recalculate the average score
                row[7] = round((float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6])) / 5, 2)

                updated = True
                break

        if updated:
            # Rewrite the CSV with the updated data
            with open(CSV_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(students)
            print(f"Student '{student_name}' has been updated.")
        else:
            print(f"Student '{student_name}' not found.")
    
    except FileNotFoundError:
        print("No student records found.")

# Delete a student
def delete_student():
    student_name = input("Enter the name of the student to delete: ")
    deleted = False

    try:
        with open(CSV_FILE, mode='r') as file:
            students = list(csv.reader(file))

        new_students = [row for row in students if row and row[0] != student_name]

        if len(new_students) < len(students):
            deleted = True
            with open(CSV_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_students)
            print(f"Student '{student_name}' deleted.")
        else:
            print(f"Student '{student_name}' not found.")

    except FileNotFoundError:
        print("No student records found.")

# Show basic statistics from the CSV
def show_statistics():
    try:
        # with open(CSV_FILE, mode='r') as file:
        #     reader = csv.reader(file)
        #     students = list(reader)[1:]  # Skip the header row
        
        # if not students:
        #     print("No students found in the database.")
        #     return
        
        # total_students = len(students)
        # total_age = sum(int(row[1]) for row in students)
        # average_age = round(total_age / total_students, 2)

        # total_math_score = sum(float(row[2]) for row in students)
        # average_math_score = round(total_math_score / total_students, 2)

        # total_english_score = sum(float(row[3]) for row in students)
        # average_english_score = round(total_english_score / total_students, 2)

        # total_afrikaans_score = sum(float(row[4]) for row in students)
        # average_afrikaans_score = round(total_afrikaans_score / total_students, 2)

        # total_geography_score = sum(float(row[5]) for row in students)
        # average_geography_score = round(total_geography_score / total_students, 2)

        # total_life_orientation_score = sum(float(row[6]) for row in students)
        # average_life_orientation_score = round(total_life_orientation_score / total_students, 2)

        # print(f"Total number of students: {total_students}")
        # print(f"Average age: {average_age}")
        # print(f"Average Math Score: {average_math_score}%")
        # print(f"Average English Score: {average_english_score}%")
        # print(f"Average Afrikaans Score: {average_afrikaans_score}%")
        # print(f"Average Geography Score: {average_geography_score}%")
        # print(f"Average Life Orientation Score: {average_life_orientation_score}%")


        if df.empty:
            print("No students found in the database")
            return
        
        # Total number of students
        total_students = len(df)

        # Calculates averages
        average_age = df["age"].mean().round(2)
        average_math_score = df["math_score"].mean().round(2)
        average_english_score = df["english_score"].mean().round(2)
        average_afrikaans_score = df["afrikaans_score"].mean().round(2)
        average_geography_score = df["geography_score"].mean().round(2)
        average_life_orientation_score = df["life_orientation_score"].mean().round(2)
        
        print(f"Total number of students: {total_students}")
        print(f"Average age: {average_age}")
        print(f"Average Math Score: {average_math_score}%")
        print(f"Average English Score: {average_english_score}%")
        print(f"Average Afrikaans Score: {average_afrikaans_score}%")
        print(f"Average Geography Score: {average_geography_score}%")
        print(f"Average Life Orientation Score: {average_life_orientation_score}%")
        print("------------------")

    except FileNotFoundError:
        print(f"File '{CSV_FILE}' not found")

# Main program loop
def main_menu():
    # Ensure the CSV has headers if it doesn't exist
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "age", "math_score", "english_score", "afrikaans_score", 
                             "geography_score", "life_orientation_score", "average_score"])
    except FileExistsError:
        pass  # File already exists, no need to do anything

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
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")

main_menu()
