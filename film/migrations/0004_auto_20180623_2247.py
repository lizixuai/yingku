# Generated by Django 2.0.5 on 2018-06-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_auto_20180623_2225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shanging',
            options={'verbose_name': '国家/地区', 'verbose_name_plural': '国家/地区'},
        ),
        migrations.RemoveField(
            model_name='shanging',
            name='film',
        ),
        migrations.RemoveField(
            model_name='shanging',
            name='shijian',
        ),
        migrations.AddField(
            model_name='info',
            name='guojia',
            field=models.CharField(default='', max_length=255, verbose_name='国家/地区'),
        ),
        migrations.AddField(
            model_name='shanging',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='国家/地区'),
        ),
    ]