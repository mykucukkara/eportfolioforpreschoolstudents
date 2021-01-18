# Generated by Django 3.0.4 on 2021-01-17 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gelisim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kazanim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kazanim_Adi', models.CharField(blank=True, max_length=1000)),
                ('detail', models.TextField(blank=True, max_length=1000)),
                ('gostergeler', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=60), default=list, size=250)),
                ('degerler', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5), default=list, size=250)),
                ('status', models.CharField(choices=[('New', 'Yeni'), ('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('gelisim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Gelisim')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
