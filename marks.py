from db import connect_db
from prettytable import PrettyTable

def add_marks():

    conn = connect_db()
    cursor = conn.cursor()

    try:
        student_id = int(input("Enter Student ID: "))
        marks = int(input("Enter Marks: "))

    except ValueError:
        print("Please Enter Numbers Only")
        conn.close()
        return

    subject = input("Enter Subject Name: ")

    query = """
    INSERT INTO marks(student_id, subject, marks)
    VALUES(%s, %s, %s)
    """

    values = (
        student_id,
        subject,
        marks
    )

    cursor.execute(query, values)

    conn.commit()

    print("Marks Added Successfully")

    conn.close()


def view_marks():

    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM marks"

    cursor.execute(query)

    records = cursor.fetchall()

    table = PrettyTable()

    table.field_names = [
        "Mark ID",
        "Student ID",
        "Subject",
        "Marks"
    ]

    for row in records:
        table.add_row(row)

    print(table)

    conn.close()


def search_marks():

    conn = connect_db()
    cursor = conn.cursor()

    try:
        student_id = int(input("Enter Student ID: "))

    except ValueError:
        print("Please Enter Numbers Only")
        conn.close()
        return

    query = """
    SELECT * FROM marks
    WHERE student_id = %s
    """

    cursor.execute(query, (student_id,))

    records = cursor.fetchall()

    if records:

        table = PrettyTable()

        table.field_names = [
            "Mark ID",
            "Student ID",
            "Subject",
            "Marks"
        ]

        for row in records:
            table.add_row(row)

        print(table)

    else:
        print("No Marks Found")

    conn.close()