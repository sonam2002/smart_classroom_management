# Generated by Django 3.0.5 on 2024-03-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0018_auto_20240323_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('Branch', 'Branch'), ('ME', 'ME'), ('CSE', 'CSE')], default='one', max_length=10),
        ),
    ]