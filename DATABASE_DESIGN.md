# Database Design

## Student Attendance Management System - Attendify

## 1. Database Information

- Database Name: student_attendance_db
- Database Type: MySQL
- Backend Framework: Django ORM

## 2. Student Table

The Student table stores student personal and academic information.

| Field Name  | Data Type    | Constraints                 | Description   |
| ----------- | ------------ | --------------------------- | ------------- |
| id          | Integer      | Primary Key, Auto Increment | Student ID    |
| name        | Varchar(100) | NOT NULL                    | Student Name  |
| roll_number | Varchar(20)  | UNIQUE, NOT NULL            | Roll Number   |
| department  | Varchar(50)  | NOT NULL                    | Department    |
| year        | Integer      | NOT NULL                    | Academic Year |
| email       | Varchar(254) | NOT NULL                    | Student Email |

## 3. Attendance Table

The Attendance table stores daily attendance details for each student.

| Field Name | Data Type   | Constraints                 | Description       |
| ---------- | ----------- | --------------------------- | ----------------- |
| id         | Integer     | Primary Key, Auto Increment | Attendance ID     |
| student_id | Integer     | Foreign Key                 | Student Reference |
| date       | Date        | NOT NULL                    | Attendance Date   |
| status     | Varchar(20) | NOT NULL                    | Present or Absent |

## 4. Primary Key

- Student table: id
- Attendance table: id

Primary keys uniquely identify each record.

## 5. Foreign Key

The student_id field in the Attendance table references the id field in the Student table.

This establishes a relationship between students and their attendance records.

## 6. Relationship

One-to-Many Relationship:

One student can have multiple attendance records.

Each attendance record belongs to one student.

## 7. Database Constraints

- Student roll numbers must be unique.
- Student name, department, year and email are required.
- Attendance status must be Present or Absent.
- A student should have only one attendance record per date.

## 8. Database Operations

The application supports:

- INSERT: Add student and attendance records.
- SELECT: View and search student records.
- UPDATE: Edit student details and attendance.
- DELETE: Remove student records.

## 9. Conclusion

The database design provides an organized way to store student information and attendance records. The relationship between the Student and Attendance tables helps maintain accurate attendance data.
