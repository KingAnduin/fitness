# -*-coding:utf-8 -*-
from django.db import models


class NewsInfo(models.Model):
    news_title = models.CharField(max_length=50,blank=True,null=True,verbose_name="健身资讯标题")
    news_type = models.CharField(max_length=50,blank=True,null=True,verbose_name="类型")
    news_level = models.CharField(max_length=50,blank=True,null=True,verbose_name="级别")
    news_major_muscle = models.CharField(max_length=50, blank=True,null=True,verbose_name="主要肌肉群")
    news_other_muscle = models.CharField(max_length=50, blank=True,null=True,verbose_name="其他肌肉")
    news_equipment = models.CharField(max_length=50, blank=True,null=True,verbose_name="器械要求")
    news_gif = models.CharField(max_length=200, blank=True,null=True,verbose_name="gif")
    news_image = models.CharField(max_length=200, blank=True, null=True, verbose_name="预览图")
    news_url = models.CharField(max_length=200, verbose_name="网址")
    news_essentials = models.CharField(max_length=200, blank=True, null=True, verbose_name="动作要领")



