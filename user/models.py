# -*-coding:utf-8 -*-
from django.db import models


class UserAccount(models.Model):
    phone = models.CharField(max_length=11, verbose_name="电话", unique=True)
    password = models.CharField(max_length=16, verbose_name="密码")

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = '用户账户'


class UserInfo(models.Model):
    # 一个联系人要对应一个账户
    user_account = models.OneToOneField(UserAccount,on_delete=models.CASCADE)
    # 当前表中的字段
    name = models.CharField(max_length=20,verbose_name="名字")
    nickname = models.CharField(max_length=10,blank=True,null=True,verbose_name="昵称")
    sex = models.CharField(max_length=1,blank=True,null=True,verbose_name="性别")
    birthday = models.DateField(blank=True,null=True,verbose_name="生日")
    head_image = models.CharField(max_length=255,blank=True,null=True,verbose_name="头像")
    contact_phone = models.CharField(max_length=11, blank=True, null=True,verbose_name="联系人电话")

    class Meta:
        verbose_name = '用户信息'


class UserToken(models.Model):
    # 一个账户要对应一个token
    user_account = models.OneToOneField(to='UserAccount', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

    class Meta:
        verbose_name = '用户token'
