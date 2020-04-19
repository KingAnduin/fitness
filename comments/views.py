# -*-coding:utf-8 -*-
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.utils import json
from rest_framework.views import APIView
from comments.models import CommentsInfo
from comments.serializers import CommentsInfoSerializers
from utils.Page import *
from order.views import changeOrderStatus
from order.models import Order
from order.serializers import OrderSerializer
from user.util.auth import Authtication
from user import models
from user.serializers import UserInfoSerializer


# 获取用户所有评论
def get_comment_by_user(request):
    if request.method == 'POST':
        ret = {"code": 200, "msg":"获取用户评论成功"}
        try:
            # Authtication()要先实例化
            account, token_obj = Authtication().authenticate(request=request)
            # 获得用户的所有订单
            queryset = Order.objects.filter(user_account=account).all()
            order_list = OrderSerializer(queryset, many=True).data
            data = []
            for item in order_list:
                single = {}
                single['good_name'] = item.get('good_name')
                single['order_date'] = item.get('order_date')
                single['order_time_period_name'] = item.get('order_time_period_name')
                single['order_date'] = item.get('order_date')
                # 获取评论内容
                queryset = CommentsInfo.objects.filter(order=item.get('id')).first()
                if queryset is not None:
                    comment_obj = CommentsInfoSerializers(queryset)
                    single['comment_content'] = comment_obj.data.get('comment_content')
                    data.append(single)
            ret['count'] = len(data)
            ret['data'] = data
        except Exception as e:
            ret['code'] = 201
            ret['msg'] = '获取用户评论失败:' + str(e)
        return JsonResponse(ret)


# 获得商品的所有订单(good_id)
def get_comment_by_good(request):
    if request.method == 'POST':
        ret = {"code": 200, "msg": "获取商品评论成功"}
        body = json.loads(request.body)
        try:
            queryset = Order.objects.filter(good_id=body.get('good_id')).all()
            order_list = OrderSerializer(queryset, many=True).data
            data = []
            for item in order_list:
                single = {}
                # 获取评论内容
                queryset = CommentsInfo.objects.filter(order=item.get('id')).first()
                if queryset is not None:
                    # 获取用户信息
                    user_info_obj = models.UserInfo.objects.filter(pk=item.get('user_account')).first()
                    user_info_dic = model_to_dict(user_info_obj)
                    single['head_image'] = user_info_dic['head_image']
                    single['nickname'] = user_info_dic['nickname']

                    comment_obj = CommentsInfoSerializers(queryset)
                    single['comment_content'] = comment_obj.data.get('comment_content')
                    single['comment_create_time'] = comment_obj.data.get('comment_create_time')[0:10]
                    data.append(single)
            ret['count'] = len(data)
            ret['data'] = data
        except Exception as e:
            ret['code'] = 201
            ret['msg'] = '获取商品评论失败:' + str(e)
        return JsonResponse(ret)


class CommentsInfoView(APIView):

    # 分页获取登录用户的评论
    """
    def get(self, request):
        ret = {'code': 200, 'msg': '查询评论成功'}
        queryset = models.CommentsInfo.objects.filter(user_account=request.user).all().order_by('-comment_create_time')

        result = CommentsInfoSerializers(queryset, many=True)
        paginator = PageSetting()

        # 计算总页数
        total_count = len(result.data)
        ret['total_page'] = paginator.cal_total_page(total_count=total_count)

        page_news = paginator.paginate_queryset(queryset=result.data, request=request, view=self)
        ret['count'] = len(page_news)
        ret['data'] = page_news
        return JsonResponse(ret)
    """
    # 新增
    def post(self, request):
        ret = {'code': 200, 'msg': '新增评论成功'}
        changeOrderStatus()
        try:
            result = json.loads(request.body)
            order_obj = Order.objects.get(pk=int(result.get('order')))
            comment = CommentsInfoSerializers(data=request.data)
            if str(order_obj.order_status) == '已完成':
                if comment.is_valid():
                    comment.save()
                    # 先save()，再调用
                    ret['data'] = comment.data
                else:
                    ret['code'] = 202
                    ret['msg'] = '数据格式错误:' + str(comment.errors)
            else:
                ret['code'] = 203
                ret['msg'] = '订单尚未完成，不能评价！'
        except Exception as e:
            ret['code'] = 204
            ret['msg'] = '新增失败:' + str(e)
        return JsonResponse(ret)

    # 编辑 (comment_id)
    def put(self, request):
        ret = {'code': 200, 'msg': '编辑评论成功'}
        try:
            result = json.loads(request.body)
            comment_obj = CommentsInfo.objects.get(pk=int(result.get('order')))
            # instance=要更新的对象
            comment = CommentsInfoSerializers(instance=comment_obj, data=request.data)
            if comment.is_valid():
                comment.save()
                ret['msg'] = '编辑成功'
                ret['data'] = comment.data
            else:
                ret['code'] = 201
                ret['msg'] = '数据格式错误: ' + str(comment.errors)
        except Exception as e:
            ret['code'] = 203
            ret['msg'] = '编辑失败:' + str(e)
        return JsonResponse(ret)

    # 删除(order)
    def delete(self, request):
        ret = {'code': 200, 'msg': '删除评论成功'}
        try:
            result = json.loads(request.body)
            # 删除商品模型
            CommentsInfo.objects.get(pk=int(result.get('order'))).delete()
            ret['msg'] = '删除成功'
        except Exception as e:
            ret['code'] = 201
            ret['msg'] = '删除失败:' + str(e)
        return JsonResponse(ret)