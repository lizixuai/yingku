# Generated by Django 2.0.5 on 2018-06-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0005_auto_20180618_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honor',
            name='result',
            field=models.CharField(choices=[('hj', '获奖'), ('tm', '提名')], max_length=255, verbose_name='结果'),
        ),
    ]
