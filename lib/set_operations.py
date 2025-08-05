# This module contains operations related to sets.
from lib.student_data import student_dict
from lib.data_processing import display_student_details


def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    # TODO: Implement this function
    pass

def add_course(student_db, student_id, new_course):
    """Add a new course to a student's course set"""
    if student_id in student_db:
        student_db[student_id]["courses"].add(new_course)
        print(f"\nAdded {new_course} to {student_db[student_id]['name']}'s courses.")
    else:
        print("\nStudent not found.")

add_course(student_dict, 101, "CS201")


display_student_details(student_dict)