# Generated by Django 2.1.2 on 2018-11-20 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='position'),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]