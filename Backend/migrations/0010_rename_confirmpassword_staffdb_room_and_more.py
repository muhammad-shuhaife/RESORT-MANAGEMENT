# Generated by Django 4.1.5 on 2023-01-22 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_rename_username_admindb_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffdb',
            old_name='Confirmpassword',
            new_name='Room',
        ),
        migrations.RemoveField(
            model_name='staffdb',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='staffdb',
            name='Password',
        ),
    ]