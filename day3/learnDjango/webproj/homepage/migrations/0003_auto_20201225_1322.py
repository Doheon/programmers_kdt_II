# Generated by Django 3.1.4 on 2020-12-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20201225_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lol',
            name='is_ice',
        ),
        migrations.AddField(
            model_name='lol',
            name='position',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='lol',
            name='role',
            field=models.CharField(default='', max_length=30),
        ),
    ]
