# Generated by Django 3.0.5 on 2024-03-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0020_auto_20240323_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherextra',
            name='status',
            field=models.CharField(max_length=40),
        ),
    ]
