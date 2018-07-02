# Generated by Django 2.0.5 on 2018-07-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0010_auto_20180702_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaiSheDi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
                ('address', models.CharField(default='', max_length=255, verbose_name='国家/地区')),
                ('changjing', models.CharField(default='', max_length=255, verbose_name='电影场景')),
            ],
            options={
                'verbose_name': '拍摄地',
                'verbose_name_plural': '拍摄地',
            },
        ),
        migrations.RemoveField(
            model_name='info',
            name='paishedi',
        ),
    ]