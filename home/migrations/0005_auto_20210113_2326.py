# Generated by Django 3.0.4 on 2021-01-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contactformmessage_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='status',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Read', 'Read')], default='New', max_length=10),
        ),
    ]
