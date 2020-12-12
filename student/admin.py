from django.contrib import admin
from student.models import Classroom, Student


# Register your models here.

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

admin.site.register(Classroom, ClassroomAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'user', 'status']
    list_filter = ['status']

admin.site.register(Student, StudentAdmin)