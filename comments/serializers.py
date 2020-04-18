from rest_framework import serializers
from .models import *


class CommentInfoSerializers(serializers.ModelSerializer):
    good_name = serializers.CharField(source='good_id.good_name', read_only=True, required=False)
    user_phone = serializers.CharField(source='user_account.phone', read_only=True, required=False)

    class Meta:
        fields = '__all__'  # ָ�����л��ֶ�(ȫ��)
        model = CommentInfo  # ָ�����л�ģ��