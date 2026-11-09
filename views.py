
import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import Student, Attendance


# Dashboard
@login_required
def home(request):
    today = timezone.localdate()

    total_students = Student.objects.count()

    present_count = Attendance.objects.filter(
        date=today,
        status='Present'
    ).count()

    absent_count = Attendance.objects.filter(
        date=today,
        status='Absent'
    ).count()

    chart_present = Attendance.objects.filter(
        status='Present'
    ).count()

    chart_absent = Attendance.objects.filter(
        status='Absent'
    ).count()

    context = {
        'total_students': total_students,
        'present_count': present_count,
        'absent_count': absent_count,
        'chart_present': chart_present,
        'chart_absent': chart_absent,
    }

    return render(request, 'dashboard.html', context)


# Attendance Report
def attendance_report(request):
    students = Student.objects.all()
    report_data = []

    for student in students:
        total = Attendance.objects.filter(
            student=student
        ).count()

        present = Attendance.objects.filter(
            student=student,
            status='Present'
        ).count()

        percentage = (present / total * 100) if total > 0 else 0

        report_data.append({
            'student': student,
            'total': total,
            'present': present,
            'percentage': round(percentage, 2)
        })

    return render(request, 'attendance_report.html', {
        'report_data': report_data
    })


# Export Attendance as CSV
def export_attendance(request):
    students = Student.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = (
        'attachment; filename="attendance_report.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
        'Student',
        'Total Classes',
        'Present',
        'Attendance %'
    ])

    for student in students:
        total = Attendance.objects.filter(
            student=student
        ).count()

        present = Attendance.objects.filter(
            student=student,
            status='Present'
        ).count()

        percentage = (present / total * 100) if total > 0 else 0

        writer.writerow([
            student.name,
            total,
            present,
            round(percentage, 2)
        ])

    return response


# Search Student
def search_student(request):
    query = request.GET.get('q', '').strip()

    students = Student.objects.filter(
        name__icontains=query
    )

    return render(request, 'search_student.html', {
        'students': students,
        'query': query
    })


# Edit Student
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        roll_number = request.POST.get('roll_number', '').strip()
        department = request.POST.get('department', '').strip()
        year = request.POST.get('year', '').strip()
        email = request.POST.get('email', '').strip()

        error = None

        if not all([name, roll_number, department, year, email]):
            error = 'All fields are required!'

        elif not year.isdigit() or not 1 <= int(year) <= 4:
            error = 'Year must be between 1 and 4.'

        elif Student.objects.filter(
            roll_number=roll_number
        ).exclude(id=student.id).exists():
            error = 'Roll number already exists!'

        else:
            try:
                validate_email(email)
            except ValidationError:
                error = 'Enter a valid email address.'

        if error:
            return render(request, 'edit_student.html', {
                'student': student,
                'error': error
            })

        student.name = name
        student.roll_number = roll_number
        student.department = department
        student.year = int(year)
        student.email = email

        student.save()

        return redirect('search_student')

    return render(request, 'edit_student.html', {
        'student': student
    })


# Delete Student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('search_student')

    return render(request, 'delete_student.html', {
        'student': student
    })


# Add Student
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        roll_number = request.POST.get('roll_number', '').strip()
        department = request.POST.get('department', '').strip()
        year = request.POST.get('year', '').strip()
        email = request.POST.get('email', '').strip()

        error = None

        if not all([name, roll_number, department, year, email]):
            error = 'All fields are required!'

        elif not year.isdigit() or not 1 <= int(year) <= 4:
            error = 'Year must be between 1 and 4.'

        elif Student.objects.filter(
            roll_number=roll_number
        ).exists():
            error = 'Roll number already exists!'

        else:
            try:
                validate_email(email)
            except ValidationError:
                error = 'Enter a valid email address.'

        if error:
            return render(request, 'add_student.html', {
                'error': error
            })

        Student.objects.create(
            name=name,
            roll_number=roll_number,
            department=department,
            year=int(year),
            email=email
        )

        return redirect('search_student')

    return render(request, 'add_student.html')


# Mark Attendance
def mark_attendance(request):
    students = Student.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        date_value = request.POST.get('date')
        status = request.POST.get('status')

        error = None

        if not student_id or not date_value or not status:
            error = 'Please fill all attendance fields.'

        elif status not in ['Present', 'Absent']:
            error = 'Please select a valid attendance status.'

        else:
            attendance_date = parse_date(date_value)

            if attendance_date is None:
                error = 'Please enter a valid date.'

            else:
                student = get_object_or_404(
                    Student,
                    id=student_id
                )

                Attendance.objects.update_or_create(
                    student=student,
                    date=attendance_date,
                    defaults={'status': status}
                )

                return render(request, 'mark_attendance.html', {
                    'students': students,
                    'today': attendance_date,
                    'success': 'Attendance marked successfully!'
                })

        return render(request, 'mark_attendance.html', {
            'students': students,
            'today': timezone.localdate(),
            'error': error
        })

    return render(request, 'mark_attendance.html', {
        'students': students,
        'today': timezone.localdate()
    })
