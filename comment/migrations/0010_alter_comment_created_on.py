# Generated by Django 3.2.4 on 2021-07-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]