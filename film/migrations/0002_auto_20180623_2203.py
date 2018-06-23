# Generated by Django 2.0.5 on 2018-06-23 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='db_fen',
            field=models.FloatField(default=0, verbose_name='豆瓣评分'),
        ),
        migrations.AlterField(
            model_name='info',
            name='imdb_fen',
            field=models.FloatField(default=0, verbose_name='IMDB评分'),
        ),
    ]
