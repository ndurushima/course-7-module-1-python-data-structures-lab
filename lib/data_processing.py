# This module contains functions to process student data.
from lib.student_data import students
from lib.student_data import student_dict

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    """
    # TODO: Implement this function
    pass

def display_students(student_list):
    print("\nStudent Records:")
    for sid, name, major in student_list:
        print(f"ID: {sid} | Name: {name} | Major: {major}")

display_students(students)

def display_student_details(student_db):
    """Display student details from a dictionary"""
    print("\nStudent Details:")
    for sid, details in student_db.items():
        print(f"ID: {sid} | Name: {details['name']} | Major: {details['major']} | Courses: {details['courses']}")

display_student_details(student_dict)

def student_generator(student_list, major):
    """Generate student records lazily for memory efficiency"""
    return (student for student in student_list if student[2] == major)

# Creating a generator for Mathematics students
math_students = student_generator(students, "Mathematics")

# Retrieving student records lazily
print(next(math_students))  # Output: (102, "Bob Smith", "Mathematics")
print(next(math_students))  # Output: (105, "Eve Lewis", "Mathematics")