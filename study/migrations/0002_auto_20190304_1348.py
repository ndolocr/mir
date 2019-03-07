# Generated by Django 2.1.2 on 2019-03-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='category',
        ),
        migrations.AddField(
            model_name='study',
            name='category',
            field=models.CharField(choices=[('Digital Content', 'Digital Content'), ('Digital Literacy', 'Digital Literacy'), ('Internet Access and Use', 'Internet Access and Use'), ('Internet/Digital Safety', 'Internet/Digital Safety'), ('Internet/ICT for Democracy', 'Internet/ICT for Democracy'), ('Internet/Digital Governance', 'Internet/Digital Governance'), ('Internet Based Entrepreneurship', 'Internet Based Entrepreneurship'), ('Internet/Digital Rights and Freedoms', 'Internet/Digital Rights and Freedoms')], default='Low', max_length=60, verbose_name='Category'),
        ),
        migrations.RemoveField(
            model_name='study',
            name='theme',
        ),
        migrations.AddField(
            model_name='study',
            name='theme',
            field=models.CharField(choices=[('Digital Content', 'Digital Content'), ('Digital Literacy', 'Digital Literacy'), ('Internet Access and Use', 'Internet Access and Use'), ('Internet/Digital Safety', 'Internet/Digital Safety'), ('Internet/ICT for Democracy', 'Internet/ICT for Democracy'), ('Internet/Digital Governance', 'Internet/Digital Governance'), ('Internet Based Entrepreneurship', 'Internet Based Entrepreneurship'), ('Internet/Digital Rights and Freedoms', 'Internet/Digital Rights and Freedoms')], default='Low', max_length=60, verbose_name='Theme'),
        ),
    ]
