# Generated by Django 2.1.7 on 2019-03-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_teacherinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherinfo',
            name='gender',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='qualification',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='shortBio',
            field=models.CharField(max_length=85),
        ),
    ]
