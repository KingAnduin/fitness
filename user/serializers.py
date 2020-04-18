from rest_framework import serializers
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):

    user_account_pk = serializers.CharField(source='user_account.pk',read_only=True, required=False, allow_null=True)

    class Meta:
        fields = '__all__'  # ָ�����л��ֶ�(ȫ��)
        model = UserInfo   # ָ�����л�ģ��
