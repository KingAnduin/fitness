from rest_framework import serializers
from .models import *


class NewsInfoSerializers(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'  # 指定序列化字段(全部)
        model = NewsInfo  # 指定序列化模型