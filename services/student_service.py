from datetime import datetime
from pathlib import Path
from validators import validator
from models.student_model import Student
def add_student(name, marks,students):
    validator.validate_name(name)
    validator.validate_duplicate(name, students)
    if not marks:
        raise ValueError("Marks cannot be empty.")
    for mark in marks:
        validator.validate_marks(mark)
    student = Student(name, marks)
    students.append(student)
    return student
def find_topper(students):
    if not students:        
        return
    topper = max(students, key=lambda s: s.average())
    return topper
def find_student(name,students):
    found_students = [student for student in students if student.name.lower() == name.lower()]
    if found_students:
        return found_students
    else:
        return [] 
def calculate_class_avg(students):
    return sum(student.average() for student in students) / len(students)
def del_Student(name,students):
    for i, student in enumerate(students):
            if student.name.lower() == name.lower():
                del students[i]
                return True
            else:
                return False
def sorted_students(students):
    sort_success =  students.sort(key=lambda s: s.name)
    return True
def highest_student(students):
    return max(students, key=lambda s: s.average())
def lowest_student(students):
    return min(students, key=lambda s: s.average())
def updated_student(name,new_name,new_marks_input,students):
    for student in students:
        if student.name.lower() == name.lower():
            try:
                if new_name:
                    validator.validate_name(new_name)
                    for s in students:
                        if (s != student and s.name.lower() == new_name.lower()):
                            return 1
                    student.name = new_name
                if new_marks_input:
                    new_marks = list(map(float, new_marks_input.split()))
                    for mark in new_marks:
                        validator.validate_marks(mark)
                    student.marks = new_marks
                    return 2
            except ValueError as e:
                return e
            return
def generate_rpt(students):
    folder_path = Path("reports")
    folder_path.mkdir(parents=True, exist_ok=True)
    time = datetime.now()
    formatted = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename = folder_path / f"report_{formatted}.txt"
    total_students_count = len(students)
    total_class_average = sum(student.average() for student in students) / len(students)
    topper_student = max(students, key=lambda s: s.average())
    lowest_student = min(students, key=lambda s: s.average())
    with open(filename, "w") as file:
        file.write("Student Performance Report \n")
        file.write("========================== \n \n")
        file.write(f"Total Students :  {total_students_count} \n")
        file.write(f"Class Average :  {total_class_average:.2f} \n\n")
        file.write(f"Top Student :  {topper_student.name} \n")
        file.write(f"Top Average :  {topper_student.average():.2f} \n")
        file.write(f"Lowest Student :  {lowest_student.name} \n")
        file.write(f"Lowest Average :  {lowest_student.average():.2f} \n")
        file.write("\n\nStudent Details\n")
        file.write("----------------\n")
        for student in students:
            file.write(str(student) + "\n")
        file.write(f"Generated On : {formatted}")
        return filename