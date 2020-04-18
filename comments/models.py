# -*-coding:utf-8 -*-
from django.db import models
from user.models import UserAccount
from good.models import Good
from order.models import Order


class CommentsInfo(models.Model):
    comment_content = models.CharField(max_length=500,blank=True,null=True,verbose_name="评论内容")
    comment_create_time = models.DateTimeField(auto_now=True,verbose_name='创建时间')
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name='订单')
