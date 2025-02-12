# Generated by Django 3.0.5 on 2024-04-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0042_auto_20240405_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimetableEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=20)),
                ('period_1', models.CharField(blank=True, max_length=100)),
                ('period_2', models.CharField(blank=True, max_length=100)),
                ('period_3', models.CharField(blank=True, max_length=100)),
                ('period_4', models.CharField(blank=True, max_length=100)),
                ('period_5', models.CharField(blank=True, max_length=100)),
                ('period_6', models.CharField(blank=True, max_length=100)),
                ('period_7', models.CharField(blank=True, max_length=100)),
                ('period_8', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='timetable',
            name='period',
            field=models.CharField(choices=[('I (9:30-10:20)', 'I (9:30-10:20)'), ('II (10:20-11:10)', 'II (10:20-11:10)'), ('III (11:10-12:00)', 'III (11:10-12:00)'), ('', '(12:00-12:40)'), ('IV (12:40-1:30)', 'IV (12:40-1:30)'), ('VI (1:30-2:20)', 'VI (1:30-2:20)'), ('VII (2:20-3:10)', 'VII (2:20-3:10)'), ('VIII (3:10-4:00)', 'VIII (3:10-4:00)')], max_length=20),
        ),
    ]
