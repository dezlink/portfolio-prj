# Generated by Django 5.0.6 on 2024-05-22 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_title_project_titleman'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='titleman',
            new_name='title',
        ),
    ]
