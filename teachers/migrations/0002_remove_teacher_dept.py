# Generated by Django 2.1.7 on 2019-03-19 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='dept',
        ),
    ]
