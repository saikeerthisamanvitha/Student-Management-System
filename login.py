from db import connect_db

def login():

    conn = connect_db()
    cursor = conn.cursor()

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    query = """
    SELECT * FROM users
    WHERE username = %s AND password = %s
    """

    values = (username, password)

    cursor.execute(query, values)

    user = cursor.fetchone()

    conn.close()

    if user:
        print("Login Successful")
        return True

    else:
        print("Invalid Username or Password")
        return False