# Generated by Django 2.0.5 on 2018-06-23 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='类型')),
            ],
            options={
                'verbose_name': '电影类型',
                'verbose_name_plural': '电影类型',
            },
        ),
        migrations.CreateModel(
            name='Honor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=255, verbose_name='所属奖')),
                ('name', models.CharField(default='', max_length=255, verbose_name='奖项')),
                ('person', models.CharField(default='', max_length=255, verbose_name='获奖者')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
                ('result', models.CharField(choices=[('hj', '获奖'), ('tm', '提名')], default='tm', max_length=255, verbose_name='结果')),
            ],
            options={
                'verbose_name': '电影奖',
                'verbose_name_plural': '电影奖',
            },
        ),
        migrations.CreateModel(
            name='HonorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='名称')),
            ],
            options={
                'verbose_name': '电影奖名称',
                'verbose_name_plural': '电影奖名称',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, unique=True, verbose_name='电影名')),
                ('ename', models.CharField(default='', max_length=255, verbose_name='英文名')),
                ('yiming', models.CharField(default='', max_length=255, verbose_name='译名')),
                ('jianjie', models.TextField(default='', verbose_name='汉语简介')),
                ('juqing', models.TextField(default='', verbose_name='汉语剧情')),
                ('ejianjie', models.TextField(default='', verbose_name='英语简介')),
                ('ejuqing', models.TextField(default='', verbose_name='英语剧情')),
                ('jibie', models.TextField(default='', verbose_name='电影级别')),
                ('daoyan', models.CharField(default='', max_length=255, verbose_name='导演')),
                ('bianju', models.CharField(default='', max_length=255, verbose_name='编剧')),
                ('category', models.CharField(default='', max_length=255, verbose_name='电影类型')),
                ('chupingongsi', models.CharField(default='', max_length=255, verbose_name='出品公司')),
                ('zhipiangongsi', models.CharField(default='', max_length=255, verbose_name='制片公司')),
                ('shichang', models.CharField(default='', max_length=255, verbose_name='时长')),
                ('zhipiandiqu', models.CharField(default='', max_length=255, verbose_name='制片地区')),
                ('chengben', models.CharField(default='', max_length=255, verbose_name='制片成本')),
                ('year', models.CharField(default='', max_length=255, verbose_name='年代')),
                ('paishedi', models.CharField(default='', max_length=255, verbose_name='拍摄地点')),
                ('duibai', models.CharField(default='', max_length=255, verbose_name='对白语言')),
                ('paisheriqi', models.CharField(default='', max_length=255, verbose_name='拍摄日期')),
                ('secai', models.CharField(default='', max_length=255, verbose_name='色彩')),
                ('imdb', models.CharField(default='', max_length=255, verbose_name='IMDB编码')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='收录时间')),
                ('misuc', models.CharField(default='', max_length=255, verbose_name='电影原声')),
                ('db_fen', models.IntegerField(default=0, verbose_name='豆瓣评分')),
                ('imdb_fen', models.IntegerField(default=0, verbose_name='IMDB评分')),
                ('youku', models.TextField(default='', verbose_name='优酷地址')),
                ('bilibili', models.TextField(default='', verbose_name='bilibili地址')),
                ('aiqiyi', models.TextField(default='', verbose_name='爱奇艺')),
            ],
            options={
                'verbose_name': '电影',
                'verbose_name_plural': '电影',
            },
        ),
        migrations.CreateModel(
            name='PiaoFang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default='', verbose_name='收入')),
                ('address', models.CharField(default='', max_length=255, verbose_name='国家/地区')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
            ],
            options={
                'verbose_name': '票房',
                'verbose_name_plural': '票房',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='角色名')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
                ('yanyuan', models.CharField(default='', max_length=255, verbose_name='演员')),
                ('desc', models.TextField(default='', verbose_name='角色描述')),
                ('fengmian', models.ImageField(default='', upload_to='image/%Y/%m/%d', verbose_name='角色封面')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
            },
        ),
        migrations.CreateModel(
            name='Shanging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shijian', models.CharField(default='', max_length=255, verbose_name='时间')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
            ],
            options={
                'verbose_name': '上映时间',
                'verbose_name_plural': '上映时间',
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(default=datetime.datetime.now, max_length=255, verbose_name='上映时间')),
                ('address', models.CharField(default='', max_length=255, verbose_name='国家/地区')),
                ('film', models.CharField(default='', max_length=255, verbose_name='所属电影')),
            ],
            options={
                'verbose_name': '上映时间',
                'verbose_name_plural': '上映时间',
            },
        ),
        migrations.CreateModel(
            name='ZhaiYao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', verbose_name='摘要内容')),
            ],
            options={
                'verbose_name': '摘要',
                'verbose_name_plural': '摘要',
            },
        ),
    ]
