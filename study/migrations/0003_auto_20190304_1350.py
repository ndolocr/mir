# Generated by Django 2.1.2 on 2019-03-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_auto_20190304_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='category',
        ),
        migrations.AddField(
            model_name='study',
            name='category',
            field=models.ManyToManyField(to='study.Category'),
        ),
        migrations.RemoveField(
            model_name='study',
            name='theme',
        ),
        migrations.AddField(
            model_name='study',
            name='theme',
            field=models.ManyToManyField(to='study.Theme'),
        ),
    ]
