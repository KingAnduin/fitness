# -*-coding:utf-8 -*-
from django.db import models
from user.models import *


class GoodType(models.Model):
    good_type = models.CharField(max_length=10,verbose_name='状态')

    def __str__(self):
        return self.good_type

    class Meta:
        db_table = 'good_type'
        verbose_name = '商品类型'


class Good(models.Model):
    good_number = models.CharField(max_length=40, verbose_name='商品编号', blank=True,null=True, unique=True)
    good_name = models.CharField(max_length=40,verbose_name='商品名称',blank=True,null=True,)
    good_image = models.CharField(max_length=255, verbose_name='商品图片',blank=True,null=True,)
    good_content = models.CharField(max_length=255, verbose_name='商品简介',blank=True,null=True,)
    good_location = models.CharField(max_length=40, verbose_name='商品位置',blank=True,null=True,)
    # good_status = models.CharField(max_length=40, verbose_name='')
    good_type = models.ForeignKey(GoodType, on_delete=models.CASCADE, verbose_name='商品类型')
    good_owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name='发布者账户')