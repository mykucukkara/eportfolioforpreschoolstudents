# Generated by Django 3.0.4 on 2021-01-07 21:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_auto_20210108_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='gostergeler',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5), size=250),
        ),
    ]
