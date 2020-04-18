from rest_framework import serializers
from .models import Order, OrderTimePeriod


class OrderTimePeriodSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'  # ָ�����л��ֶ�(ȫ��)
        model = OrderTimePeriod   # ָ�����л�ģ��


class OrderSerializer(serializers.ModelSerializer):
    good_name = serializers.CharField(source='good_id.good_name',read_only=True, required=False)
    # ��һ��order_time_period����OrderInfo�е����ԣ��ڶ���order_time_periodΪOrderTimePeriod�е�����
    # ��Ҫ��Order�е������������������лᱨ��
    # Eg: If you need to access data before committing to the database then inspect 'serializer.validated_data' instead.
    order_time_period_name = serializers.CharField(source='order_time_period.order_time_period',read_only=True,required=False)
    order_status_name = serializers.CharField(source='order_status.order_status',read_only=True,required=False)

    class Meta:
        fields = '__all__'  # ָ�����л��ֶ�(ȫ��)
        model = Order   # ָ�����л�ģ��
