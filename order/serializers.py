from rest_framework import serializers
from .models import Order, OrderTimePeriod


class OrderTimePeriodSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'  # ָ�����л��ֶ�(ȫ��)
        model = OrderTimePeriod   # ָ�����л�ģ��


class OrderSerializer(serializers.ModelSerializer):
    good_name = serializers.CharField(source='good_id.good_name')
    # ��һ��order_time_period����OrderInfo�е����ԣ��ڶ���order_time_periodΪOrderTimePeriod�е�����
    order_time_period = serializers.CharField(source='order_time_period.order_time_period')
    order_status = serializers.CharField(source='order_status.order_status')

    class Meta:
        fields = '__all__'  # ָ�����л��ֶ�(ȫ��)
        model = Order   # ָ�����л�ģ��
