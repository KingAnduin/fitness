# -*-coding:utf-8 -*-
from django.shortcuts import render
import datetime
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.utils import json
from rest_framework.views import APIView
from order import models
from order.serializers import OrderSerializer
from order.utils.Page import *


# 根据预约日期和当前时间更改订单状态 TODO 查询所有订单，消耗大
def changeOrderStatus():
    today = datetime.date.today()
    # today = datetime.date(2020, 4, 17)
    # order_list = models.Order.objects.filter(order_date__gte=today).all()
    order_list = models.Order.objects.all()
    for item in order_list:
        # print("order_data ", item.order_date)
        if today.__eq__(item.order_date):
            item.order_status_id = 2
        elif today.__gt__(item.order_date):
            item.order_status_id = 3
        elif today.__lt__(item.order_date):
            item.order_status_id = 1
        # print("order_status ", item.order_status_id)
        item.save()


# 通过good_id,order_date来查询订单，用于辅助查询商品可用时间段
def getOrderByKey(good_id, order_date):
    queryset = models.Order.objects.filter(Q(good_id_id=good_id) &
                                           Q(order_date=order_date)).all()
    result = OrderSerializer(queryset, many=True)
    unavailabe_period = []
    for item in result.data:
        unavailabe_period.append(item.get('order_time_period'))
    return result.data, unavailabe_period


# 新增订单 TODO
# 检查一：user + order_date + order_time_period
# (?)检查二：good_id + order_date + order_time_period
def addOrder(request):
    if request.method == 'POST':
        ret = {'code': 200, 'msg': '新增订单成功'}
        body = json.loads(request.body)

        return JsonResponse(ret)
    else:
        pass


class OrderInfo(APIView):
    changeOrderStatus()

    # 获取登录用户分页订单
    def get(self, request):
        ret = {'code': 200, 'msg': '查询信息成功'}
        request_body = json.loads(request.body)
        queryset = models.Order.objects.filter(user_account=request.user).all().order_by('-id')

        result = OrderSerializer(queryset, many=True)
        paginator = PageSetting()
        page_order_list = paginator.paginate_queryset(queryset=result.data,request=request,view=self)
        ret['count'] = len(page_order_list)
        ret['data'] = page_order_list
        return JsonResponse(ret)

    def put(self, request):
        ret = {'code': 200, 'msg': None}
        try:
            result = json.loads(request.body)
            order_obj = models.Order.objects.get(pk=int(result.get('order_id')))
            # instance=要更新的对象
            new_order = OrderSerializer(instance=order_obj, data=request.data)
            if new_order.is_valid():
                new_order.save()
                ret['msg'] = '编辑成功'
            else:
                ret['code'] = 201
                ret['msg'] = '数据错误: ' + str(new_order.errors)
        except Exception as e:
            ret['code'] = 202
            ret['msg'] = '编辑失败' + str(e)
        return JsonResponse(ret)

    def delete(self, request):
        ret = {'code': 200, 'msg': None}
        try:
            result = json.loads(request.body)
            # 删除商品模型
            models.Order.objects.get(pk=int(result.get('order_id'))).delete()
            ret['msg'] = '删除成功'
        except Exception as e:
            ret['code'] = 201
            ret['msg'] = '删除失败' + str(e)
        return JsonResponse(ret)