# Generated by Django 4.2 on 2023-05-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_address_alter_employee_emp_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
