# Generated by Django 3.0.5 on 2024-04-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0030_auto_20240328_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='by',
            field=models.CharField(default='school', max_length=20, null=True),
        ),
    ]