from django.contrib import admin
from .models import Student, Attendance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'roll_number',
        'department',
        'year',
        'email',
    )

    search_fields = (
        'name',
        'roll_number',
        'department',
    )

    list_filter = (
        'department',
        'year',
    )

    class Media:
        js = ('js/student_validation.js',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student',
        'date',
        'status',
    )

    list_filter = (
        'date',
        'status',
    )

    search_fields = (
        'student__name',
        'student__roll_number',
    )
