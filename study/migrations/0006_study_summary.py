# Generated by Django 2.1.2 on 2019-04-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_study_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='summary',
            field=models.TextField(blank=True, null=True, verbose_name='Expense Description'),
        ),
    ]
