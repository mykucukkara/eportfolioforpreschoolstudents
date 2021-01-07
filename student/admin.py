from django.contrib import admin
from django_better_admin_arrayfield.forms.fields import DynamicArrayField

from student.models import Classroom, Student, Images


# Register your models here.

class StudentImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

admin.site.register(Classroom, ClassroomAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'user', 'status']
    list_filter = ['status']


admin.site.register(Student, StudentAdmin)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Images,ImagesAdmin)