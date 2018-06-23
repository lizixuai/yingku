from django.db import models
from person.models import Info as PersonInfo
from datetime import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='类型', max_length=255, unique=True)

    class Meta:
        verbose_name = '电影类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Info(models.Model):
    name = models.CharField(verbose_name='电影名', max_length=255, unique=True,default='')
    ename = models.CharField(verbose_name='英文名', max_length=255,default='')
    yiming = models.CharField(verbose_name='译名', max_length=255,default='')
    jianjie = models.TextField(verbose_name='汉语简介',default='')  # 短
    juqing = models.TextField(verbose_name='汉语剧情',default='')  # 长
    ejianjie = models.TextField(verbose_name='英语简介',default='')  # 短
    ejuqing = models.TextField(verbose_name='英语剧情',default='')  # 长
    jibie = models.TextField(verbose_name='电影级别',default='')
    daoyan = models.CharField(verbose_name='导演', max_length=255,default='')
    bianju = models.CharField(verbose_name='编剧', max_length=255,default='')
    yanyuan = models.TextField(verbose_name='演员', max_length=255,default='')
    category = models.CharField(verbose_name='电影类型',max_length=255,default='')
    guojia = models.CharField(verbose_name='国家/地区',max_length=255,default='')
    chupingongsi = models.TextField(verbose_name='出品公司', max_length=255,default='')
    zhipiangongsi = models.TextField(verbose_name='制片公司', max_length=255,default='')
    shichang = models.CharField(verbose_name='时长', max_length=255,default='')
    zhipiandiqu = models.CharField(verbose_name='制片地区', max_length=255,default='')
    chengben = models.CharField(verbose_name='制片成本', max_length=255,default='')
    year = models.CharField(verbose_name='年代', max_length=255,default='')
    paishedi = models.CharField(verbose_name='拍摄地点', max_length=255,default='')
    duibai = models.CharField(verbose_name='对白语言', max_length=255,default='')
    paisheriqi = models.CharField(verbose_name='拍摄日期', max_length=255,default='')
    secai = models.CharField(verbose_name='色彩', max_length=255,default='')
    imdb = models.CharField(verbose_name='IMDB编码', max_length=255,default='')
    add_time = models.DateField(verbose_name='收录时间', default=datetime.now)
    misuc = models.CharField(verbose_name='电影原声', max_length=255,default='')
    db_fen = models.FloatField(verbose_name='豆瓣评分',default=0)
    imdb_fen = models.FloatField(verbose_name='IMDB评分',default=0)
    youku = models.TextField(verbose_name='优酷地址',default='')
    bilibili = models.TextField(verbose_name='bilibili地址',default='')
    aiqiyi = models.TextField(verbose_name='爱奇艺',default='')

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(verbose_name='角色名', max_length=255,default='')
    film = models.CharField(verbose_name='所属电影',max_length=255,default='')
    yanyuan = models.CharField(verbose_name='演员',max_length=255,default='')
    desc = models.TextField(verbose_name='角色描述',default='')
    fengmian = models.ImageField(verbose_name='角色封面', upload_to='image/%Y/%m/%d',default='')

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class HonorCategory(models.Model):
    name = models.CharField(verbose_name='名称', max_length=255,default='')

    class Meta:
        verbose_name = '电影奖名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Honor(models.Model):
    RESULT = (
        ('hj', '获奖'),
        ('tm', '提名'),
    )
    category = models.CharField(verbose_name='所属奖',max_length=255,default='')
    name = models.CharField(verbose_name='奖项', max_length=255,default='')
    person = models.CharField(verbose_name='获奖者',max_length=255,default='')#?
    film = models.CharField(verbose_name='所属电影',max_length=255,default='')
    result = models.CharField(verbose_name='结果', choices=RESULT, max_length=255,default='tm')

    class Meta:
        verbose_name = '电影奖'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Show(models.Model):
    time = models.DateField(verbose_name='上映时间', max_length=255,default=datetime.now)
    address = models.CharField(verbose_name='国家/地区', max_length=255,default='')
    film = models.CharField(verbose_name='所属电影',max_length=255,default='')

    class Meta:
        verbose_name = '上映时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.time)


class PiaoFang(models.Model):
    num = models.IntegerField(verbose_name='收入',default='')
    address = models.CharField(verbose_name='国家/地区', max_length=255,default='')
    film = models.CharField(verbose_name='所属电影',max_length=255,default='')

    class Meta:
        verbose_name = '票房'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.num)

#电影介绍摘要
class ZhaiYao(models.Model):
    models.CharField(verbose_name='所属电影', max_length=255,default='')
    content = models.TextField(verbose_name='摘要内容',default='')

    class Meta:
        verbose_name = '摘要'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.film.name

#上映时间
class Shanging(models.Model):
    shijian = models.CharField(verbose_name='时间', max_length=255,default='')
    film = models.CharField(verbose_name='所属电影',max_length=255,default='')

    class Meta:
        verbose_name = '上映时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.shijian


#国家/地区
class Shanging(models.Model):
    name = models.CharField(verbose_name='国家/地区', max_length=255,default='',unique=True)

    class Meta:
        verbose_name = '国家/地区'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name