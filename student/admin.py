from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_better_admin_arrayfield.forms.fields import DynamicArrayField
from django_better_admin_arrayfield.forms.widgets import DynamicArrayWidget

from student.models import Classroom, Student, Images, Kazanim, Gelisim


# Register your models here.

class StudentImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    readonly_fields = ('image_tag',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'user', 'status']
    list_filter = ['status']
    #readonly_fields = ('image_tag',)
    #inlines = [StudentImageInline] açılması durumunda admin de her öğrenci altında reismlerini gösterir



class ImagesAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ['title', 'image_tag']
    #readonly_fields = ('image_tag',)


class KazanimAdmin(admin.ModelAdmin,DynamicArrayMixin):
    list_display = ['Kazanim_Adi', 'detail','student', 'user', 'status']
    list_filter = ['status']

admin.site.register(Gelisim)
admin.site.register(Kazanim,KazanimAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Images,ImagesAdmin)