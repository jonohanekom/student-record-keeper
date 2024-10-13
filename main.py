def get_valid_mark(subject):
    while True:
        mark = float(input(f"Enter {subject} mark: "))
        if 0 <= mark <= 100:
            return mark
        else:
            print("Invalid mark. Please enter a mark between 0 and 100.")

def add_student(students):
    student_name = input("Name: ")
    student_age = int(input("Age: "))

    score_math = get_valid_mark("Math")
    score_english = get_valid_mark("English")
    score_afrikaans = get_valid_mark("Afrikaans")
    score_geography = get_valid_mark("Geography")
    score_life_orientation = get_valid_mark("Life Orientation")

    #Hard coded average formula
    average_score = round(((score_math + score_english + score_afrikaans + score_geography + score_life_orientation) / 5), 2)

    student = {
        "name" : student_name,
        "age" : student_age,
        "score_math" : score_math,
        "score_english" : score_english,
        "score_afrikaans" : score_afrikaans,
        "score_geography" : score_geography,
        "score_life_orientation" : score_life_orientation,
        "average_score" : average_score
    }

    students.append(student)

def view_student(students):
    
    if not students:
        print("No students available.\n")
        return

    for student in students:
        print("----------------------------")
        print(
                f"Name: {student['name']}\n"
                f"Age: {student['age']}\n"
                f"Math: {student['score_math']}\n"
                f"English: {student['score_english']}\n"
                f"Afrikaans: {student['score_afrikaans']}\n"
                f"Geography: {student['score_geography']}\n"
                f"Life Orientation: {student['score_life_orientation']}\n"
                f"{student['name']}'s average is {student['average_score']}%"
            )
        print("----------------------------")


def update_student(students):
    if not students:
        print("No students available.\n")
        return

    student_name = input("Enter the name of the student you want to update: ")

    for student in students:
        if student["name"] == student_name:
            print(f"Found student '{student_name}'")

            print("\n")
            print("----------------------------")
            print("What would you like to update?")
            print("1: Name")
            print("2: Age")
            print("3: Math Score")
            print("4: English Score")
            print("5: Afrikaans Score")
            print("6: Geography Score")
            print("7: Life Orientation Score")
            print("----------------------------")

            choice = input("Select an option (1-7): ")

            if choice == "1":
                new_student_name = input("Enter a new name: ")
                student["name"] = new_student_name
            elif choice == "2":
                new_student_age = int(input("Enter a new age: "))
                student["age"] = new_student_age
            elif choice == "3":
                student["score_math"] = get_valid_mark("Math")
            elif choice == "4":
                student["score_english"] = get_valid_mark("English")
            elif choice == "5":
                student["score_afrikaans"] = get_valid_mark("Afrikaans")
            elif choice == "6":
                student["score_geography"] = get_valid_mark("Geography")
            elif choice == "7":
                student["score_life_orientation"] = get_valid_mark("Life Orientation")
            else:
                print("Invalid option.")
                return

            # Recalculate the average score after update
            student["average_score"] = round(
                (student["score_math"] + student["score_english"] + student["score_afrikaans"] +
                 student["score_geography"] + student["score_life_orientation"]) / 5, 2
            )

            print(f"Student '{student_name}' has been updated!")
            return

def delete_student(students):
    
    if not students:
        print("No students available.\n")
        return

    
    student_name = input("Enter the name of the student to delete: ")
    
    # Finds the student in the dict and deletes them
    for i, student in enumerate(students):
          if student["name"] == student_name:
               del students[i]
               print(f"Student '{student_name}' deleted.")
               return
    print(f"Student '{student_name}' not found.")

def sort_students(students):
    if not students:
        print("No students available.\n")
        return

     
    print("Available sorting parameters:")
    print("1. Name")
    print("2. Age")
    print("3. Average mark")

    sort_parameter = input("Select a parameter to sort by (1-3): ")

    if sort_parameter == "1":
        sorted_students = sorted(students, key=lambda x: x["name"])
        view_student(sort_students)
    elif sort_parameter == "2":
        sorted_students = sorted(students, key=lambda x: x["age"])
        view_student(sort_students)
    elif sort_parameter == "3":
         sorted_students = sorted(students, key=lambda x: x["average_score"])
         view_student(sort_students)
    else:
         print("Invalid option.")

# Main program loop
def main_menu():

    students = []
    while True:
        print("------------------")
        print("1: Add a new student")
        print("2: View all students")
        print("3: Update a student")
        print("4: Delete a student")
        print("5: Sort students")
        print("6: Calculate statistics")
        print("7: Exit")
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
            sort_students(students)
        elif choice == "7":
             print("exiting application")
             break
        else:
             print("Invalid option. Please try again.")

main_menu()

