from django.http import JsonResponse
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart import models
from quickstart.serializers import MusicSerializer


# uuid加密字符串
def md5():
    import uuid
    return uuid.uuid4().hex


# 通用视图函数APIView
class MusicList(APIView):
    def get(self, request):
        queryset = models.Music.objects.all()
        ret = MusicSerializer(queryset, many=True)
        return Response(ret.data)

    # 新增
    def post(self, request):
        music = MusicSerializer(data=request.data)
        if music.is_valid():
            music.save()
            return Response(music.data)
        else:
            return Response(music.errors)


# 用户登录认证并生成或更新token
class AuthView(APIView):
    # 登录操作不需要token认证
    authentication_classes = []
    # 登录操作不需要权限认证
    permission_classes = []

    def post(self, request, *args, **kwargs):
        ret = {'code': 100, 'msg': None}
        try:
            name = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            # 筛选出用户
            obj = models.UserInfos.objects.filter(username=name, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
            # 为用户创建token,并更新或创建UserToken
            # update_or_create() 返回两个值
            token = md5()
            token_obj, value = models.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            token_obj.save()
            ret['token'] = token
        except Exception as e:
            print(e)
            ret['code'] = 1002
            ret['msg'] = '请求异常' + str(e)

        return JsonResponse(ret)
