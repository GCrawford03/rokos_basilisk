# Generated by Django 2.2 on 2020-09-30 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_app', '0005_auto_20200929_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_input',
        ),
    ]
