import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Samu@2210",
        database="student_management"
    )

    return conn