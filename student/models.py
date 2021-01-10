from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import int_list_validator
from django.db import models


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
    detail = models.TextField(null=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Images(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    detail = models.TextField(max_length=200, null=True)
    status = models.CharField(max_length=10, choices=STATUS)
    gostergeler = ArrayField(base_field=models.CharField(blank=True, max_length=5), size=250, default=list)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'