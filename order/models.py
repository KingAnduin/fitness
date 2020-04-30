# -*-coding:utf-8 -*-
from django.db import models
from user.models import *
from good.models import *


class OrderStatus(models.Model):
    order_status = models.CharField(max_length=10,verbose_name='状态')

    def __str__(self):
        return self.order_status

    class Meta:
        db_table = 'order_state'
        verbose_name = '订单状态'


class OrderTimePeriod(models.Model):
    order_time_period = models.CharField(max_length=100,verbose_name='可用时间段')

    def __str__(self):
        return self.order_time_period

    class Meta:
        db_table = 'order_time_period'
        verbose_name = '预约可用时间段'


class Order(models.Model):
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    order_date = models.DateField(verbose_name='预约日期')
    order_is_comment = models.CharField(max_length=50,default='评价一下',blank=True,null=True,verbose_name='是否已评论')
    order_time_period = models.ForeignKey(OrderTimePeriod, on_delete=models.CASCADE, verbose_name='预约时间段')
    order_status = models.ForeignKey(OrderStatus,on_delete=models.CASCADE, verbose_name='订单状态')
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name='用户账户')
    good_id = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='商品ID')