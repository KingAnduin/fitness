from rest_framework import serializers
from .models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'  # 指定序列化字段(全部)
        model = Music   # 指定序列化模型
