import mysql.connector

# STEP 1: Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cursor = conn.cursor()

# STEP 2: Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")

# STEP 3: Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50),
    marks FLOAT
)
""")

print("Database & Table Ready")

# -------- FUNCTIONS -------- #

def add_student():
    name = input("Name: ")
    age = int(input("Age: "))
    course = input("Course: ")
    marks = float(input("Marks: "))

    sql = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, age, course, marks))
    conn.commit()
    print("Student Added")

def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    print("\nID | Name | Age | Course | Marks")
    print("-" * 40)
    for row in data:
        print(row)

def update_student():
    sid = int(input("Student ID: "))
    new_marks = float(input("New Marks: "))
    cursor.execute("UPDATE students SET marks=%s WHERE id=%s", (new_marks, sid))
    conn.commit()
    print("Record Updated")

def delete_student():
    sid = int(input("Student ID: "))
    cursor.execute("DELETE FROM students WHERE id=%s", (sid,))
    conn.commit()
    print("🗑️ Record Deleted")

def search_student():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM students WHERE name LIKE %s", ('%' + name + '%',))
    for row in cursor.fetchall():
        print(row)

# -------- MAIN MENU -------- #

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        search_student()
    elif choice == "6":
        print("Program Closed")
        break
    else:
        print("Invalid Choice")
