# Generated by Django 2.1.2 on 2019-01-16 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0007_auto_20190116_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='tags',
        ),
    ]
