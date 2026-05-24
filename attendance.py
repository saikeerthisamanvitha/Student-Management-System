from db import connect_db
from prettytable import PrettyTable

def add_attendance():

    conn = connect_db()
    cursor = conn.cursor()

    try:
        student_id = int(input("Enter Student ID: "))
        total_classes = int(input("Enter Total Classes: "))
        attended_classes = int(input("Enter Attended Classes: "))

    except ValueError:
        print("Please Enter Numbers Only")
        conn.close()
        return

    percentage = (attended_classes / total_classes) * 100

    query = """
    INSERT INTO attendance
    (student_id, total_classes, attended_classes, percentage)
    VALUES(%s, %s, %s, %s)
    """

    values = (
        student_id,
        total_classes,
        attended_classes,
        percentage
    )

    cursor.execute(query, values)

    conn.commit()

    print("Attendance Added Successfully")

    conn.close()
    from prettytable import PrettyTable

def view_attendance():

    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM attendance"

    cursor.execute(query)

    records = cursor.fetchall()

    table = PrettyTable()

    table.field_names = [
        "Attendance ID",
        "Student ID",
        "Total Classes",
        "Attended Classes",
        "Percentage"
    ]

    for row in records:
        table.add_row(row)

    print(table)

    conn.close()