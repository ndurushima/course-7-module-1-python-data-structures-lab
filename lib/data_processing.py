# This module contains functions to process student data.
from lib.student_data import students

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
