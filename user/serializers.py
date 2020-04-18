from rest_framework import serializers
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'  # 指定序列化字段(全部)
        model = UserInfo   # 指定序列化模型
