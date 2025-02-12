# Generated by Django 3.0.5 on 2024-03-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0015_auto_20240318_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='course',
        ),
        migrations.RemoveField(
            model_name='project',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='score',
            new_name='assignment_grade',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='student',
            new_name='student_name',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='project',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.AddField(
            model_name='grade',
            name='exam_grade',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grade',
            name='project_grade',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
