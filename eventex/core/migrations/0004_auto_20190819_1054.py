# Generated by Django 2.0.6 on 2019-08-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='kind',
            field=models.CharField(choices=[('E', 'Email'), ('P', 'Telefone')], max_length=1),
        ),
    ]
