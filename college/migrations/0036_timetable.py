# Generated by Django 3.0.5 on 2024-04-04 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0035_auto_20240402_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=10)),
                ('period', models.CharField(choices=[('I', 'I (9:30-10:20)'), ('II', 'II (10:20-11:10)'), ('III', 'III (11:10-12:00)'), ('IV', 'IV (12:00-12:40)'), ('V', 'V (12:40-1:30)'), ('VI', 'VI (1:30-2:20)'), ('VII', 'VII (2:20-3:10)'), ('VIII', 'VIII (3:10-4:00)')], max_length=5)),
                ('teacher', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]
