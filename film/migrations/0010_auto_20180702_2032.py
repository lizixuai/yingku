# Generated by Django 2.0.5 on 2018-07-02 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0009_auto_20180702_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='ejianjie',
        ),
        migrations.RemoveField(
            model_name='info',
            name='ejuqing',
        ),
        migrations.AlterField(
            model_name='info',
            name='jianjie',
            field=models.TextField(default='', verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='info',
            name='juqing',
            field=models.TextField(default='', verbose_name='剧情'),
        ),
    ]