from django.contrib import admin
from django_better_admin_arrayfield.forms.fields import DynamicArrayField

from student.models import Classroom, Student, Images


# Register your models here.

class StudentImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'user','image_tag', 'status']
    list_filter = ['status']
    readonly_fields = ('image_tag',)
    #inlines = [StudentImageInline] açılması durumunda admin de her öğrenci altında reismlerini gösterir

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Images,ImagesAdmin)