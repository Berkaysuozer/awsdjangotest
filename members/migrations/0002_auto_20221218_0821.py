# Generated by Django 3.2 on 2022-12-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='firstname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='members',
            name='lastname',
            field=models.CharField(max_length=140),
        ),
    ]
