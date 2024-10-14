import random 
from faker import Faker
import csv

fake = Faker()

def generate_students(num_students=1000):
    
    grades = ['A', 'B', 'C', 'D', 'E', 'F']
    students = []
    
    for _ in range(num_students):
        student = {
            'name': fake.name(),
            'age': random.randint(18, 25),
            'math_score': round(random.uniform(0, 100),2),
            'english_score': round(random.uniform(0, 100),2),
            'afrikaans_score': round(random.uniform(0, 100),2),
            'geography_score': round(random.uniform(0, 100),2),
            'life_orientation_score': round(random.uniform(0, 100),2),
            'grade': random.choice(grades)
        }
        students.append(student)
        
    return students

def write_students_to_csv(students, filename="students.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'age', 'math_score', 'english_score', 'afrikaans_score', 
                      'geography_score', 'life_orientation_score', 'average_score', 'grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
            
if __name__ == "__main__":
    students = generate_students()
    write_students_to_csv(students)