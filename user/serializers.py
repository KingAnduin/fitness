from rest_framework import serializers
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'  # ָ�����л��ֶ�(ȫ��)
        model = UserInfo   # ָ�����л�ģ��
