# Generated by Django 3.0.5 on 2024-03-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0024_auto_20240323_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherextra',
            name='subjects',
            field=models.CharField(choices=[('Discrete maths', 'Discrete maths'), ('data structure', 'data structure'), ('computer networks', 'computer networks'), ('UNIX', 'UNIX'), ('software engineering', 'software engineering')], default='Branch', max_length=40),
        ),
    ]
