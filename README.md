# 🎓 Student Management System (Python + MySQL)

## 📌 Overview
This is a **console-based Student Management System** built using **Python** and **MySQL**.  
It allows users to **add, view, update, delete, and search student records** stored in a MySQL database.

The program demonstrates:
- Database connectivity using `mysql.connector`
- SQL CRUD operations
- Modular programming using functions
- Menu-driven command-line interaction

---

## 🛠️ Technologies Used
- **Python 3**
- **MySQL Server**
- **mysql-connector-python** library

---

## ⚙️ Program Initialization (Header Section)

### Purpose
The header section is responsible for:
1. Connecting to the MySQL server
2. Creating a database if it does not exist
3. Selecting the database
4. Creating the required table

### Explanation
- Establishes a connection to the local MySQL server using credentials
- Ensures the database `student_db` exists
- Ensures the table `students` exists with appropriate columns

### Database Schema
| Column | Type | Description |
|------|------|------------|
| id | INT (AUTO_INCREMENT) | Unique student ID |
| name | VARCHAR(50) | Student name |
| age | INT | Student age |
| course | VARCHAR(50) | Course enrolled |
| marks | FLOAT | Student marks |

---

## 📦 Function Documentation

---

## ➕ `add_student()`

### Description
Adds a new student record to the database.

### Input
- Name (string)
- Age (integer)
- Course (string)
- Marks (float)

### Process
- Takes user input
- Executes an `INSERT` SQL query
- Commits the transaction to the database

### Output
- Confirmation message: **"Student Added"**

### Use Case
Used when a new student needs to be registered in the system.

---

## 👀 `view_students()`

### Description
Displays all student records stored in the database.

### Input
- None

### Process
- Executes a `SELECT *` query
- Fetches all rows
- Prints them in a readable format

### Output
- List of all students with ID, Name, Age, Course, and Marks

### Use Case
Used to review all existing student records.

---

## ✏️ `update_student()`

### Description
Updates the marks of an existing student using their ID.

### Input
- Student ID (integer)
- New Marks (float)

### Process
- Executes an `UPDATE` SQL query
- Commits changes to the database

### Output
- Confirmation message: **"Record Updated"**

### Use Case
Used when a student's marks need correction or update.

---

## 🗑️ `delete_student()`

### Description
Deletes a student record from the database using student ID.

### Input
- Student ID (integer)

### Process
- Executes a `DELETE` SQL query
- Commits the transaction

### Output
- Confirmation message: **"Record Deleted"**

### Use Case
Used when a student record is no longer needed.

---

## 🔍 `search_student()`

### Description
Searches for students by name (supports partial matches).

### Input
- Name or partial name (string)

### Process
- Uses `LIKE` keyword in SQL query
- Fetches and displays matching records

### Output
- Matching student records

### Use Case
Used to quickly find students without knowing their exact ID.

---

## 🧭 Main Menu Logic

### Description
Implements an infinite loop to display options and execute user-selected actions.

### Menu Options
1. Add Student
2. View Students
3. Update Marks
4. Delete Student
5. Search Student
6. Exit

### Behavior
- Takes user choice as input
- Calls the corresponding function
- Terminates the program when option `6` is selected

---

## ✅ Key Features
- Persistent data storage using MySQL
- Modular and readable code structure
- Safe SQL execution using parameterized queries
- Beginner-friendly and extensible

---

## 🚀 Possible Enhancements
- Input validation and error handling
- Authentication system
- GUI using Tkinter / PyQt
- Export data to CSV or PDF
- Sorting and pagination

---

## 🧠 Learning Outcome
This project helps understand:
- Python–MySQL integration
- CRUD operations
- Structured program design
- Real-world database interaction