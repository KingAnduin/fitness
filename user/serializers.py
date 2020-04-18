from rest_framework import serializers
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):

    user_account_pk = serializers.CharField(source='user_account.pk',read_only=True, required=False, allow_null=True)

    class Meta:
        fields = '__all__'  # 指定序列化字段(全部)
        model = UserInfo   # 指定序列化模型
