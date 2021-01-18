import django
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.forms import ModelForm
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_better_admin_arrayfield.forms.fields import DynamicArrayField
from django_better_admin_arrayfield.models.fields import ArrayField
from django.core.validators import int_list_validator
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.utils.safestring import mark_safe


class Classroom(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/', null=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Student(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/', null=True)
    detail = RichTextUploadingField(null=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Images(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    detail = RichTextUploadingField(blank=True)
    kavram = RichTextUploadingField(blank=True)
    surec = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Gelisim(models.Model):
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
class Kazanim(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gelisim = models.ForeignKey(Gelisim, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, on_delete=models.CASCADE, default='')
    Kazanim_Adi = models.CharField(max_length=1000, blank=True)
    detail = models.TextField(max_length=1000, blank=True)
    gostergeler = ArrayField(base_field=models.CharField(blank=True, max_length=60), size=250, default=list)
    degerler = ArrayField(base_field=models.CharField(blank=True, max_length=5), size=250, default=list)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Kazanim_Adi

    def ikontrol(self):
        if self.gostergeler.db_index == self.degerler.db_index:
            return True
        else:
            return False


class KazanimForm(ModelForm):
    class Meta:
        model = Kazanim
        fields = ['Kazanim_Adi', 'detail', 'gostergeler', 'degerler']

