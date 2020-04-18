from rest_framework import serializers
from .models import Order, OrderTimePeriod


class OrderTimePeriodSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'  # 指定序列化字段(全部)
        model = OrderTimePeriod   # 指定序列化模型


class OrderSerializer(serializers.ModelSerializer):
    good_name = serializers.CharField(source='good_id.good_name')
    # 第一个order_time_period代表OrderInfo中的属性，第二个order_time_period为OrderTimePeriod中的属性
    order_time_period = serializers.CharField(source='order_time_period.order_time_period')
    order_status = serializers.CharField(source='order_status.order_status')

    class Meta:
        fields = '__all__'  # 指定序列化字段(全部)
        model = Order   # 指定序列化模型
