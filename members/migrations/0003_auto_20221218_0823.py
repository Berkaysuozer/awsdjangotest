# Generated by Django 3.2 on 2022-12-18 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20221218_0821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='lastname',
            new_name='tweet',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='firstname',
            new_name='username',
        ),
    ]