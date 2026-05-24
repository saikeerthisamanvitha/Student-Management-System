# Student Management System (Python + MySQL)

A console-based Student Management System built using Python and MySQL.  
This project manages student data, attendance, marks, and generates student reports.

---

## Features

- User Login Authentication
- Add / View / Search / Update / Delete Students
- Attendance Management with Percentage Calculation
- Marks Management (Add, View, Search)
- Individual Student Report (Student + Attendance + Marks)
- Exception Handling for safe input
- Clean Table-based output (PrettyTable)
- Modular Python file structure

---

## Tech Stack

- Python
- MySQL
- mysql-connector-python
- PrettyTable

---

## Database Tables

- students
- attendance
- marks
- users

---

## How to Run

1. Install requirements:
```
pip install mysql-connector-python prettytable
```

2. Setup MySQL database using your SQL commands

3. Run project:
```
python main.py
```

---

## Default Login

- Username: admin
- Password: admin123

---

## Project Structure

```
main.py
student.py
attendance.py
marks.py
login.py
db.py
```

---

## Author

First Python + SQL project for learning purposes.