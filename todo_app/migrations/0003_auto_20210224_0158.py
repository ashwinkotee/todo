# Generated by Django 3.1.7 on 2021-02-23 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20210224_0150'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Table',
            new_name='Task_Table',
        ),
    ]