# Generated by Django 2.0.5 on 2018-06-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_lunbo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lunbo',
            name='img',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='图片'),
        ),
    ]
