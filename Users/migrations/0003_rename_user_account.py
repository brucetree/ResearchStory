# Generated by Django 3.2.5 on 2021-07-13 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_user_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Account',
        ),
    ]