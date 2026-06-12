import logging
import csv
from models.student_model import Student
def csv_write_dict(students, filename="students.csv"):
    try:
        with open(filename, "w", newline="") as file:
            fieldnames = ["name", "marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                marks_str = ",".join(str(mark) for mark in student.marks)
                writer.writerow({"name": student.name, "marks": marks_str})
            logging.info("Data exported successfully.")
    except Exception as e:
        logging.error(f"Error writing CSV: {e}")
def csv_reader_dict(students, filename="students.csv"):
    try:
        students.clear()
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                marks_str = row["marks"].split(",")
                marks = [float(mark) for mark in marks_str]
                student = Student(name, marks)
                students.append(student)
            logging.info("Data imported successfully.")
    except Exception as e:
        logging.error(f"Error Reading CSV: {e}")
