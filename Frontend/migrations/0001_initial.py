# Generated by Django 4.1.5 on 2023-02-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registrationdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.EmailField(blank=True, max_length=30, null=True)),
                ('Password', models.CharField(blank=True, max_length=30, null=True)),
                ('Confirmpassword', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]