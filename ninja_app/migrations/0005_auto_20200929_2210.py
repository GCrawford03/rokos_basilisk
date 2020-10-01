# Generated by Django 2.2 on 2020-09-30 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_app', '0004_remove_player_rations'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('user_input', models.CharField(max_length=45)),
            ],
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
