# Generated by Django 3.0.5 on 2024-03-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0029_auto_20240328_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='sem',
            field=models.IntegerField(choices=[(1, '1st Semester'), (2, '2nd Semester'), (3, '3rd Semester'), (4, '4th Semester'), (5, '5th Semester'), (6, '6th Semester'), (7, '7th Semester'), (8, '8th Semester')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentextra',
            name='year',
            field=models.IntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')], default=1),
            preserve_default=False,
        ),
    ]
