from student import add_student, view_students, search_student, update_student, delete_student, student_report
from attendance import add_attendance, view_attendance
from marks import add_marks, view_marks,search_marks
from login import login
if login() == False:
    exit()

while True:

    print("\n----- STUDENT MANAGEMENT SYSTEM -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add Attendance")
    print("6. Add Attendance")
    print("7. View Attendance")
    print("6. Add Attendance")
    print("7. View Attendance")
    print("8. Add Marks")
    print("9. View Marks")
    print("10. Search Marks")
    print("10. Search Marks")
    print("11. Student Report")
    print("12. Exit")

    try:
        choice = int(input("Enter Choice: "))

    except ValueError:
        print("Please Enter Numbers Only")
        continue

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        add_attendance()

    elif choice == 7:
        view_attendance()

    elif choice == 8:
        add_marks()

    elif choice == 9:
        view_marks()

   
    elif choice == 10:
        search_marks()

    elif choice == 11:
        student_report()

    elif choice == 12:
        print("Thank You")
    break
else:
        print("Invalid Choice")
