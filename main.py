def add_student(students):
    student_name = input("Name: ")
    student_age = int(input("Age: "))
    score_math = float(input("Enetr Math mark: "))
    score_english = float(input("Enter English mark: "))
    score_afrikaans = float(input("Enter Afrikaans mark: "))
    score_geography = float(input("Enter Geography mark: "))
    score_life_orentation = float(input("Enter Life Orenation mark: "))

    student = {
        "name" : student_name,
        "age" : student_age,
        "score_math" : score_math,
        "score_english" : score_english,
        "score_afrikaans" : score_afrikaans,
        "score_geography" : score_geography,
        "score_life_orentation" : score_life_orentation
    }

    students.append(student)

def view_student(students):
        for student in students:
            print("----------------------------")
            print(f"Name: {student['name']}\n"
                f"Age: {student['age']}\n"
                f"Math: {student['score_math']}\n"
                f"English: {student['score_english']}\n"
                f"Afrikaans: {student['score_afrikaans']}\n"
                f"Geography: {student['score_geography']}\n"
                f"Life Orientation: {student['score_life_orentation']}\n")
            print("----------------------------")

def delete_student(students):
     student_name = input("Enter the name of the student to delete: ")
    
    # Finds the student in the dict and deletes them
     for i, student in enumerate(students):
          if student["name"] == student_name:
               del student[i]
               print(f"Student '{student_name}' deleted.")
               return
     print(f"Student '{student_name}' not found.")

def update_student(students):
     student_name = input("Enter the name of the student you want to update: ")

     for student in students:
          if student["name"] == student_name:
                print(f"Found student '{student_name}")

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
                    new_student_age = input("Enter a new age: ")
                    student["age"] = new_student_age
                elif choice == "3":
                    new_score_math = input("Enter a new Math mark: ")
                    student["score_math"] = new_score_math
                elif choice == "4":
                    new_score_english = input("Enter a new English mark: ")
                    student["score_english"] = new_score_english
                elif choice == "5":
                    new_score_afrikaans = input("Enter a new Afrikaans mark: ")
                    student["score_afrikaans"] = new_score_afrikaans
                elif choice == "6":
                    new_score_geography = input("Enter a new Geography mark: ")
                    student["score_geography"] = new_score_geography
                elif choice == "7":
                    new_score_life_orientation = input("Enter a new Life Orentation mark: ")
                    student["score_life_orentation"] = new_score_life_orientation
                else:
                    print("Invalid option.")
                print(f"Student '{student_name}' has been updated!")

                print(f"Student '{student_name}' not found.")
                return
                

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
        elif choice == "7":
             print("exiting application")
             break
        else:
             print("Invalid option. Please try again.")

main_menu()

