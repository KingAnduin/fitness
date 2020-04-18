
from user import models
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework.utils import json


# rest framework 自定义token验证
class Authtication(BaseAuthentication):
    # 自定义token验证
    def authenticate(self, request):
        # token = request._request.GET.get('token')

        # token放在请求体body中
        # result = json.loads(request.body)
        # token = result.get('token')
        # print('token', result.get('token'))

        # token放在请求头headers的Authorization中
        result = request.headers
        token = result.get('Authorization')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        # rest framework 内部重新赋值给request，方便日后使用
        # 即request.user = token_obj.user_account  request.auth = token_obj
        return token_obj.user_account, token_obj

    # 不常用，函数内容基本为空
    def authenticate_header(self, request):
        pass