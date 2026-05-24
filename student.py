from db import connect_db
from prettytable import PrettyTable

def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = int(input("Enter Year: "))
    phone = input("Enter Phone: ")

    query = """
    INSERT INTO students(name, branch, year, phone)
    VALUES(%s, %s, %s, %s)
    """

    values = (name, branch, year, phone)

    cursor.execute(query, values)

    conn.commit()

    print("Student Added Successfully")

    conn.close()

def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    table = PrettyTable()

    table.field_names = [
        "Student ID",
        "Name",
        "Branch",
        "Year",
        "Phone"
    ]

    for student in students:
        table.add_row(student)

    print(table)

    conn.close()

def search_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID to Search: "))

    query = "SELECT * FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if student:

        table = PrettyTable()

        table.field_names = [
            "Student ID",
            "Name",
            "Branch",
            "Year",
            "Phone"
        ]

        table.add_row(student)

        print(table)

    else:
        print("Student Not Found")

    conn.close()
def update_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID to Update: "))

    new_phone = input("Enter New Phone Number: ")

    query = """
    UPDATE students
    SET phone = %s
    WHERE student_id = %s
    """

    values = (new_phone, student_id)

    cursor.execute(query, values)

    conn.commit()

    if cursor.rowcount > 0:
        print("Student Updated Successfully")

    else:
        print("Student Not Found")

    conn.close()
def delete_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID to Delete: "))

    query = "DELETE FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))

    conn.commit()

    if cursor.rowcount > 0:
        print("Student Deleted Successfully")

    else:
        print("Student Not Found")

    conn.close()  
def student_report():

    conn = connect_db()
    cursor = conn.cursor()

    try:
        student_id = int(input("Enter Student ID: "))

    except ValueError:
        print("Please Enter Numbers Only")
        conn.close()
        return

    # Student Details
    student_query = """
    SELECT * FROM students
    WHERE student_id = %s
    """

    cursor.execute(student_query, (student_id,))
    student = cursor.fetchone()

    if not student:
        print("Student Not Found")
        conn.close()
        return

    print("\n----- STUDENT DETAILS -----")
    print(student)

    # Attendance Details
    attendance_query = """
    SELECT total_classes, attended_classes, percentage
    FROM attendance
    WHERE student_id = %s
    """

    cursor.execute(attendance_query, (student_id,))
    attendance = cursor.fetchone()

    print("\n----- ATTENDANCE -----")

    if attendance:
        print(attendance)

    else:
        print("No Attendance Record")

    # Marks Details
    marks_query = """
    SELECT subject, marks
    FROM marks
    WHERE student_id = %s
    """

    cursor.execute(marks_query, (student_id,))
    marks = cursor.fetchall()

    print("\n----- MARKS -----")

    if marks:
        for row in marks:
            print(row)

    else:
        print("No Marks Record")

    conn.close()