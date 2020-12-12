from django.contrib import admin
from student.models import Classroom


# Register your models here.

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

admin.site.register(Classroom, ClassroomAdmin)
