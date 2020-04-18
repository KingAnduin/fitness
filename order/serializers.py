from rest_framework import serializers
from .models import Order, OrderTimePeriod


class OrderTimePeriodSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'  # 指定序列化字段(全部)
        model = OrderTimePeriod   # 指定序列化模型


class OrderSerializer(serializers.ModelSerializer):
    good_name = serializers.CharField(source='good_id.good_name',read_only=True, required=False)
    # 第一个order_time_period代表OrderInfo中的属性，第二个order_time_period为OrderTimePeriod中的属性
    # 不要与Order中的属性重名，否则反序列会报错
    # Eg: If you need to access data before committing to the database then inspect 'serializer.validated_data' instead.
    order_time_period_name = serializers.CharField(source='order_time_period.order_time_period',read_only=True,required=False)
    order_status_name = serializers.CharField(source='order_status.order_status',read_only=True,required=False)

    class Meta:
        fields = '__all__'  # 指定序列化字段(全部)
        model = Order   # 指定序列化模型
