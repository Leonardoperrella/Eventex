# Generated by Django 2.0.6 on 2019-08-22 21:38

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('core', '0009_auto_20190822_1834'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
    ]
