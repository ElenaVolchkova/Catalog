# Generated by Django 3.1.7 on 2021-04-09 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='boss',
            new_name='chief',
        ),
    ]
