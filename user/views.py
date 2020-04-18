# -*-coding:utf-8 -*-
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from rest_framework.utils import json
from rest_framework.views import APIView
from user import models
from user.serializers import UserInfoSerializer


# 根据uuid4生成随机字符串
def md5():
    import uuid
    return uuid.uuid4().hex


# 用户登录
class UserLogin(APIView):
    # 登录操作不需要token认证
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': None}
        try:
            result = json.loads(request.body)
            phone = result.get('phone')
            pwd = result.get('password')
            # phone = request._request.POST.get('phone')
            # pwd = request._request.POST.get('password')
            # 筛选出用户
            obj = models.UserAccount.objects.filter(phone=phone, password=pwd).first()
            if not obj:
                ret['code'] = 201
                ret['msg'] = '用户名或密码错误'
            else:
                # 为用户创建token,并更新或创建UserToken
                token = md5()
                # update_or_create 返回值有两个
                token_obj, value = models.UserToken.objects.update_or_create(user_account=obj, defaults={'token': token})
                token_obj.save()
                ret['token'] = token
                ret['msg'] = '登录成功'
        except Exception as e:
            ret['code'] = 202
            ret['msg'] = '请求异常' + str(e)

        return JsonResponse(ret)


# 用户注册
class UserRegister(APIView):
    # 注册操作不需要token认证
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        ret = {'code': 200, 'msg': None}
        try:
            result = json.loads(request.body)
            phone = result.get('phone')
            password = result.get('password')
            name = result.get('name')
            # phone = request._request.POST.get('phone')
            # password = request._request.POST.get('password')
            # 查询用户是否已注册
            if models.UserAccount.objects.filter(phone=phone).count() > 0:
                ret['code'] = 201
                ret['msg'] = '该用户已注册，请直接登录或更换手机号'
            else:
                # 新建用户
                user_account = models.UserAccount(phone=phone, password=password)
                try:
                    user_account.save()
                    # 注册该用户并创建一个一对一UserInfo对象
                    userinfo = models.UserInfo(user_account=user_account, name=name,
                                               sex=None, nickname=None, birthday=None)
                    userinfo.save()
                    ret['msg'] = '注册成功'
                except Exception as e:
                    print(e)
                    ret['code'] = 202
                    ret['msg'] = '注册失败' + str(e)

        except Exception as e:
            print(e)
            ret['code'] = 203
            ret['msg'] = '请求异常' + str(e)

        return JsonResponse(ret)


# 获取／编辑用户详细信息
class UserInfo(APIView):

    # 获取
    def get(self, request):
        ret = {'code': 200, 'msg': '成功'}
        queryset = models.UserInfo.objects.filter(user_account=request.user)
        result = UserInfoSerializer(queryset, many=True)
        ret['data'] = result.data
        return JsonResponse(ret)

    # 编辑
    def put(self, request):
        ret = {'code': 200, 'msg': None}
        try:
            # result = json.loads(request.body)
            # 获取关联用户模型
            # user_account = models.UserAccount.objects.get(phone=request.user)
            # user_info = models.UserInfo.objects.get(user_account=user_account)
            # 填充信息
            # user_info.nickname = result.get('nickname', None)
            # user_info.name = result.get('name', None)
            # user_info.sex = result.get('sex', None)
            # user_info.content_phone = result.get('content_phone', None)
            # if result.get('birthday', None) is not None:
            # 格式化日期
            # user_info.birthday = datetime.strptime(result.get('birthday'), '%Y-%m-%d')
            # user_info.head_image = result.get('head_image', None)

            # user_info.save()
            # ret['msg'] = '编辑成功'

            # TODO 保存照片至服务器
            user_account = models.UserAccount.objects.get(phone=request.user)
            user_info_obj = models.UserInfo.objects.get(user_account=user_account)
            # instance=要更新的对象
            user_info = UserInfoSerializer(instance=user_info_obj, data=request.data)
            if user_info.is_valid():
                user_info.save()
                ret['msg'] = '编辑成功'
            else:
                ret['code'] = 201
                ret['msg'] = '数据错误: ' + str(user_info.errors)
        except Exception as e:
            ret['code'] = 201
            ret['msg'] = '编辑失败' + str(e)
        return JsonResponse(ret)


# 修改密码
class ChangePassword(APIView):

    def post(self, request):
        ret = {'code': 200, 'msg': None}
        result = json.loads(request.body)
        # 获取关联用户模型
        user_account = models.UserAccount.objects.get(phone=request.user)
        try:
            user_account.password = result.get('password')
            user_account.save()
            ret['msg'] = '修改密码成功'
        except Exception as e:
            ret['code'] = 201
            ret['msg'] = '修改密码失败' + str(e)
        return JsonResponse(ret)