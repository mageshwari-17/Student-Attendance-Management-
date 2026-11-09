# Attendify - Student Attendance Management System

## 1. Project Description

Attendify is a web-based Student Attendance Management System developed using Python Django and MySQL.

The application helps administrators manage student information, record daily attendance, monitor attendance performance, and generate attendance reports.

## 2. Project Objectives

- To maintain student information digitally.
- To record daily student attendance.
- To reduce manual attendance work.
- To search and update student records easily.
- To calculate student attendance percentages.
- To generate downloadable attendance reports.

## 3. Technologies Used

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend

- Python
- Django

### Database

- MySQL

### Development Tools

- Visual Studio Code
- MySQL Workbench
- Web Browser

## 4. Main Features

1. Admin Login and Logout
2. Student Dashboard
3. Add New Student
4. View Student Details
5. Search Students
6. Edit Student Details
7. Delete Student Details
8. Mark Daily Attendance
9. Attendance Analytics
10. Calculate Attendance Percentage
11. Download Attendance Report as CSV
12. Responsive User Interface

## 5. Project Modules

### Admin Module

- Secure admin login.
- Manage student records.
- Access attendance information.

### Student Management Module

- Add student information.
- View student details.
- Search student records.
- Edit and delete student details.

### Attendance Module

- Select a student.
- Choose attendance date.
- Mark Present or Absent.
- Save attendance records.

### Report Module

- Display total classes.
- Display present count.
- Calculate attendance percentage.
- Download CSV reports.

## 6. Database Design

### Student Table

- id
- name
- roll_number
- department
- year
- email

### Attendance Table

- id
- student_id
- date
- status

Relationship:
One student can have multiple attendance records.

## 7. Installation Requirements

Install Python and MySQL on your system.

Open the project folder in Visual Studio Code.

Open the terminal and install the required packages:

```bash
pip install -r requirements.txt
```

## 8. Database Configuration

1. Open MySQL Workbench.
2. Create a database named `student_attendance_db`.
3. Configure the MySQL username and password in `settings.py`.
4. Save the settings file.

## 9. Run the Project

Run database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin account:

```bash
python manage.py createsuperuser
```

Start the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

Admin panel:

http://127.0.0.1:8000/admin/

## 10. Project Outcome

Attendify provides an easy and efficient way to manage student information and daily attendance records.

It reduces manual work, improves record management, and generates attendance reports for better monitoring.

## 11. Future Enhancements

- Student login functionality.
- PDF attendance report generation.
- Email notifications.
- Advanced attendance analytics.

## 12. Developed By

Student Attendance Management System

Project Name: Attendify
