from rest_framework import serializers
from .models import *


class NewsInfoSerializers(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'  # ָ�����л��ֶ�(ȫ��)
        model = NewsInfo  # ָ�����л�ģ��