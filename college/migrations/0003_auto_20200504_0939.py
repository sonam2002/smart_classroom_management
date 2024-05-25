# Generated by Django 3.0.5 on 2020-05-04 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_teacherextra_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentextra',
            name='branch',
        ),
        migrations.AddField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'), ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten')], default='one', max_length=10),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cl', models.CharField(max_length=10)),
                ('present_status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.StudentExtra')),
            ],
        ),
    ]