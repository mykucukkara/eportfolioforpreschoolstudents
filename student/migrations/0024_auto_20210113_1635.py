# Generated by Django 3.0.4 on 2021-01-13 13:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_auto_20210108_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
