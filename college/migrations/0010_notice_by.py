# Generated by Django 3.0.5 on 2020-05-08 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0009_auto_20200507_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='by',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
