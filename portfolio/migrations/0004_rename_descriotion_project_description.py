# Generated by Django 5.0.6 on 2024-05-23 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_titleman_project_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descriotion',
            new_name='description',
        ),
    ]
