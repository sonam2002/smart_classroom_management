# Generated by Django 3.0.5 on 2020-05-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_auto_20200506_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='fee',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
