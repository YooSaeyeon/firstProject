# Generated by Django 4.2.1 on 2023-05-17 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacted', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='contact',
        ),
    ]