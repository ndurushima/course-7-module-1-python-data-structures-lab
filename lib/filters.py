# This module contains functions for filtering student data.
from lib.data_processing import display_students
from lib.student_data import students

def filter_students_by_major(student_list, major):
    filtered = [student for student in student_list if student[2] == major]
    
    if filtered:
        print(f"\nStudents majoring in {major}:")
        display_students(filtered)
    else:
        print(f"\nNo students found in {major}.")

filter_students_by_major(students, "Computer Science")


