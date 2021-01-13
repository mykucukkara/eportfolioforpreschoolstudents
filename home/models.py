from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150, null=True)
    keywords = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=150, null=True)
    school = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    fax = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    smtpserver = models.CharField(max_length=150, null=True)
    smtpemail = models.CharField(max_length=150, null=True)
    smyppassword = models.CharField(max_length=150, null=True)
    smtpport = models.CharField(max_length=150, null=True)
    icon = models.ImageField(blank=True, upload_to='images/', null=True)
    facebook = models.CharField(max_length=150, null=True)
    twitter = models.CharField(max_length=150, null=True)
    instagram = models.CharField(max_length=150, null=True)
    aboutus = RichTextUploadingField(null=True)
    contact = RichTextUploadingField(null=True)
    references = RichTextUploadingField(null=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




