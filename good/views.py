# -*-coding:utf-8 -*-
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.utils import json
from rest_framework.views import APIView
from good import models
from good.serializers import GoodSerializer
from order.views import getOrderByKey
from order.models import OrderTimePeriod
from order.serializers import *


# 配合订单表查询商品不可用时间段(good_id, order_date)
def get_unavailable_period(request):
    # 可用时间段
    queryset = OrderTimePeriod.objects.all()
    period = OrderTimePeriodSerializer(queryset, many=True).data

    if request.method == 'POST':
        ret = {'code': 200, 'msg': '获取信息成功', 'unavailable_period': [], "period":period}
        body = json.loads(request.body)
        order_list, ret['unavailable_period'] = getOrderByKey(good_id=body.get('good_id'), order_date=body.get('order_date'))
        ret['data'] = order_list
        return JsonResponse(ret, json_dumps_params={'ensure_ascii':False})
    else:
        pass


# 商品信息删改查
class GoodInfo(APIView):

    # 按类型获取商品列表
    def get(self, request):
        ret = {'code': 200, 'msg': '获取信息成功'}
        try:
            queryset = models.Good.objects.filter(good_type_id=request.data.get('good_type')).all().order_by('good_number')
            result = GoodSerializer(queryset, many=True)
            ret['count'] = queryset.count()
            ret['data'] = result.data
        except Exception as e:
            ret['code'] = 201
            ret['msg'] = '获取信息失败' + str(e)
        return JsonResponse(ret, json_dumps_params={'ensure_ascii':False})

    # 编辑
    def put(self, request):
        ret = {'code': 200, 'msg': None}
        try:
            result = json.loads(request.body)
            good_obj = models.Good.objects.get(pk=int(result.get('good_id')))
            # instance=要更新的对象, partial为True表示可以只传修改的那部分值
            new_good = GoodSerializer(instance=good_obj, data=request.data,partial=True)
            if new_good.is_valid():
                new_good.save()
                ret['msg'] = '编辑成功'
            else:
                ret['code'] = 201
                ret['msg'] = '数据错误: ' + str(new_good.errors)
        except Exception as e:
            ret['code'] = 202
            ret['msg'] = '编辑失败' + str(e)
        return JsonResponse(ret, json_dumps_params={'ensure_ascii':False})

    # 删除
    def delete(self, request):
        ret = {'code': 200, 'msg': None}
        try:
            result = json.loads(request.body)
            # 删除商品模型
            models.Good.objects.get(pk=int(result.get('good_id'))).delete()
            ret['msg'] = '删除成功'
        except Exception as e:
            ret['code'] = 201
            ret['msg'] = '删除失败' + str(e)
        return JsonResponse(ret, json_dumps_params={'ensure_ascii':False})



