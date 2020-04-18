# -*-coding:utf-8 -*-
from rest_framework import serializers
from .models import Good


class GoodSerializer(serializers.ModelSerializer):

    # 新增字段用于处理外键 TODO
    # source对应数据库中的字段
    # 第一个good_type代指GoodType对象，第二个good_type指GoodType对象属性中的id
    # good_type = serializers.CharField(source="good_type.pk")
    # 第一个good_owner代指UserAccount对象，第二个good_owner指UserAccount对象中属性中的id
    # good_owner = serializers.CharField(source="good_owner.pk")

    class Meta:
        fields = '__all__'  # 指定序列化字段(全部)
        model = Good   # 指定序列化模型
