import logging
from validators import validator
from services import student_service
from stotage import json_storage
from stotage import csv_storage
def show_menu(students):
    print("\nStudent Grade Analyzer")
    print("1. Add Students")
    print("2. View Students")
    print("3. Topper")
    print("4. Save Students")
    print("5. Load Students")
    print("6. Search Students")
    print("7. Total Students")
    print("8. Class Average")
    print("9. Delete Students")
    print("10. Update Students")
    print("11. Sort Students by Name")
    print("12. Highest and Lowest Averages")
    print("13. Export Students to CSV")
    print("14. Import Students from CSV")
    print("15. Generate Report")
    print("16. Save and Exit")
    get_menu_choice(students)
def get_menu_choice(students):
    while True:
        try:
            choice = input("Enter your choice: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= 16:
                call_menu_funct(choice,students)
                continue  
            print("Invalid choice. Please enter a number between 1 and 16.")
        except ValueError as e:
            print(e)
def call_menu_funct(choice,students):
    if choice == '1':
        add_students(students)
    elif choice == '2':
        view_students(students)
    elif choice == '3':
        topper(students)
    elif choice == '4':
        json_storage.save_students(students)
    elif choice == '5':
        json_storage.load_students(students)
    elif choice == '6':
        search_student(students)
    elif choice == '7':
        total_students(students)
    elif choice == '8':
        class_average(students)
    elif choice == '9':
        delete_student(students)
    elif choice == '10':
        update_student(students)
    elif choice == '11':
        sort_students(students)
    elif choice == '12':
        highest_lowest(students)
    elif choice == '13':
        csv_storage.csv_write_dict(students)
    elif choice == '14':
        csv_storage.csv_reader_dict(students)
    elif choice == '15':
        generate_report(students)
    elif choice == '16':
        json_storage.save_students(students)
        print("Exiting the program.")
        exit()
    else:
        print("Invalid choice. Please try again.")
def add_students(students):
    try:
        n = int(input("How many students do you want to add? "))
    except ValueError:
        print("Please enter a valid number.")
        return
    for _ in range(n):
        try:
            name = input("Enter student name: ")
            marks = list(map(float, input("Enter marks separated by space: ").split()))
            student_service.add_student(name, marks,students)
            logging.info(f"Student {name} added successfully.")
        except (ValueError, TypeError) as e:
            print(f"Input error: {e}")
def view_students(students):
    if not students:
        print("No students to display.")
        return
    for student in students:
        display(student)
def topper(students):
    top_student = student_service.find_topper(students)
    if top_student is None:              # handle None from service
        print("No students exist.")
        return
    print("Topper:")
    display(top_student)
def search_student(students):
    name = input("Enter student name to search: ").strip()
    find_students_result = student_service.find_student(name,students)
    if find_students_result:
        for student in find_students_result:
            display(student)
    else:
        print("Student not found.")
def total_students(students):
    print(f"Total number of students: {len(students)}")
def class_average(students):
    if not students:
        print("No students to calculate average.")
        return
    else:
        total_avg = student_service.calculate_class_avg(students)
    print(f"Class Average: {total_avg:.2f}")
def delete_student(students):
    try:
        name = input("Enter student name to delete: ").strip()
        validator.validate_name(name)  
        del_std_staus =  student_service.del_Student(name,students)
        if del_std_staus:
            logging.info(f"Student {name} deleted successfully.")
        else:    
            print("Student not found.")
    except ValueError as e:
        print(e)
def sort_students(students):
    if not students:
        print("No students to sort.")
        return
    sort_stdnts = student_service.sorted_students(students)
    if sort_stdnts:
        print("Students sorted by name successfully.")
def highest_lowest(students):
    if not students:
        print("No students to evaluate.")
        return
    top_student = student_service.highest_student(students)
    print("Highest Average:")
    display(top_student)
    low_student = student_service.lowest_student(students)
    print("Lowest Average:")
    display(low_student)
def update_student(students):
    try:
        name = input("Enter student name to update: ").strip()
        validator.validate_name(name)
        new_name = input("Enter new name (leave blank to keep current): ").strip()
        new_marks_input = input("Enter new marks separated by space (leave blank to keep current): ").strip()
        upd_std = student_service.updated_student(name,new_name,new_marks_input,students)
        if upd_std == 1:
            print("Student Name Already Exist. ")
        elif upd_std == 2:
            print("Student Updated Successfully .")
        else:
            print(upd_std)        
    except ValueError as e:
        print(e)
        return
def generate_report(students):
    try:
        if not students:
            print("No students available.")
            return
        rpt_generate = student_service.generate_rpt(students)
        if rpt_generate:
            print(f"Report generated successfully: {rpt_generate}")
    except Exception as e:
        logging.error(f'Error generating report: {e}')
def display(student):
        print(str(student))