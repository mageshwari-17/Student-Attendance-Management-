
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.attendance_report, name='attendance_report'),
    path('export/', views.export_attendance, name='export_attendance'),
    path('search/', views.search_student, name='search_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('add-student/', views.add_student, name='add_student'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
]
