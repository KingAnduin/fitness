# -*-coding:utf-8 -*-
from django.http import JsonResponse
from rest_framework.utils import json
from rest_framework.views import APIView
from news import models
from news.serializers import NewsInfoSerializers
from utils.Page import *


class NewsInfo(APIView):

    # 分页获取
    def get(self, request):
        ret = {'code': 200, 'msg': '查询信息成功'}
        queryset = models.NewsInfo.objects.all().order_by('-id')

        result = NewsInfoSerializers(queryset, many=True)
        paginator = PageSetting()

        # 计算总页数
        total_count = len(result.data)
        ret['total_page'] = paginator.cal_total_page(total_count=total_count)

        page_news = paginator.paginate_queryset(queryset=result.data, request=request, view=self)
        ret['count'] = len(page_news)
        ret['data'] = page_news
        return JsonResponse(ret, json_dumps_params={'ensure_ascii':False})

    # 新增
    def post(self, request):
        ret = {'code': 200, 'msg': '新增信息成功'}
        try:
            news = NewsInfoSerializers(data=request.data)
            if news.is_valid():
                news.save()
                # 先save()，再调用
                ret['data'] = news.data
            else:
                ret['code'] = 202
                ret['msg'] = '数据格式错误:' + str(news.errors)
        except Exception as e:
            ret['code'] = 203
            ret['msg'] = '新增失败:' + str(e)
        return JsonResponse(ret, json_dumps_params={'ensure_ascii':False})

    # 编辑 (news_id)
    def put(self, request):
        ret = {'code': 200, 'msg': '编辑信息成功'}
        try:
            result = json.loads(request.body)
            news_obj = models.NewsInfo.objects.get(pk=int(result.get('news_id')))
            # instance=要更新的对象
            news = NewsInfoSerializers(instance=news_obj, data=request.data)
            if news.is_valid():
                news.save()
                ret['msg'] = '编辑成功'
            else:
                ret['code'] = 201
                ret['msg'] = '数据格式错误: ' + str(news.errors)
        except Exception as e:
            ret['code'] = 203
            ret['msg'] = '编辑失败:' + str(e)
        return JsonResponse(ret, json_dumps_params={'ensure_ascii':False})

    # 删除(news_id)
    def delete(self, request):
        ret = {'code': 200, 'msg': '删除信息成功'}
        try:
            result = json.loads(request.body)
            # 删除商品模型
            models.NewsInfo.objects.get(pk=int(result.get('news_id'))).delete()
            ret['msg'] = '删除成功'
        except Exception as e:
            ret['code'] = 201
            ret['msg'] = '删除失败:' + str(e)
        return JsonResponse(ret, json_dumps_params={'ensure_ascii':False})