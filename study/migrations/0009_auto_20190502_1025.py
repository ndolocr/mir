# Generated by Django 2.1.2 on 2019-05-02 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0008_auto_20190425_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subtheme',
            name='theme',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
        migrations.DeleteModel(
            name='SubTheme',
        ),
    ]
