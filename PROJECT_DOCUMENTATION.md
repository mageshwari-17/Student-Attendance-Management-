# STUDENT ATTENDANCE MANAGEMENT SYSTEM

## Project Documentation

## 1. Project Title

Student Attendance Management System (Attendify)

## 2. Project Introduction

The Student Attendance Management System is a web-based application developed using Python Django and MySQL.

It helps administrators manage student information, record daily attendance, monitor attendance performance, and generate attendance reports.

The system reduces manual work and provides an organized way to maintain student attendance records.

## 3. Project Objectives

- To maintain student information digitally.
- To record daily student attendance.
- To search, edit and delete student details.
- To prevent duplicate student roll numbers.
- To calculate student attendance percentages.
- To generate and download attendance reports.
- To provide a simple and user-friendly interface.

## 4. Technologies Used

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend

- Python
- Django Framework

### Database

- MySQL

### Development Tools

- Visual Studio Code
- MySQL Workbench
- Web Browser

## 5. System Requirements

### Hardware Requirements

- Computer or Laptop
- Minimum 4 GB RAM
- Sufficient storage space
- Internet connection for Bootstrap CDN

### Software Requirements

- Windows Operating System
- Python
- Django
- MySQL Server
- MySQL Workbench
- Visual Studio Code
- Web Browser

## 6. Database Design

The application uses a MySQL database named `student_attendance_db`.

It contains two main tables.

### Student Table

Stores student information:

- Student ID
- Student Name
- Roll Number
- Department
- Academic Year
- Email

### Attendance Table

Stores daily attendance information:

- Attendance ID
- Student ID
- Attendance Date
- Attendance Status

The Attendance table is connected to the Student table using a foreign key.

One student can have multiple attendance records.

## 7. Module Description

### 7.1 Login and Logout Module

Provides administrator authentication to access the system.

### 7.2 Dashboard Module

Displays:

- Total number of students.
- Present student count.
- Absent student count.
- Attendance analytics chart.

### 7.3 Student Management Module

Allows the administrator to:

- Add new students.
- View student details.
- Manage student records.

### 7.4 Attendance Management Module

Allows the administrator to:

- Select a student.
- Choose an attendance date.
- Mark Present or Absent.
- Save attendance records.

### 7.5 Search Module

Searches student information using the student name.

### 7.6 Edit Module

Updates existing student information.

### 7.7 Delete Module

Deletes student records after confirmation.

### 7.8 Attendance Report Module

Displays:

- Total classes.
- Number of classes attended.
- Attendance percentage.

### 7.9 Download Report Module

Exports attendance reports into CSV format.

## 8. System Workflow

1. Administrator logs into the application.
2. Dashboard displays student and attendance information.
3. Administrator adds student details.
4. Administrator marks daily attendance.
5. Attendance information is stored in MySQL.
6. Administrator searches or updates student records.
7. Attendance reports are generated.
8. Reports can be downloaded as CSV files.

## 9. Screenshots

The following screenshots are included in the project screenshots folder:

1. Login Page
2. Dashboard
3. Add Student Page
4. Student Management Page
5. Edit Student Page
6. Delete Confirmation Page
7. Mark Attendance Page
8. Attendance Report Page

## 10. Testing

The application should be tested for:

- Administrator login and logout.
- Adding student records.
- Searching student records.
- Editing student information.
- Deleting student records.
- Marking Present and Absent.
- Generating attendance reports.
- Downloading CSV files.
- Form validation.
- Database connectivity.

## 11. Future Enhancements

- Student login functionality.
- PDF report generation.
- Email notifications.
- Advanced attendance analytics.
- Student profile management.

## 12. Conclusion

The Student Attendance Management System simplifies student information management and daily attendance tracking.

It reduces manual work, maintains organized records, calculates attendance percentages, and generates downloadable reports.

The project demonstrates the practical use of Python Django, MySQL, HTML, CSS, Bootstrap, and JavaScript in developing a full-stack web application.

## 13. Developed By

Individual Python Full Stack Development Project

Project Name: Attendify
