from django.urls import path
from user.views import *


urlpatterns = [
    path('login/', UserLogin.as_view()),
    path('register/', UserRegister.as_view()),
    path('userInfo/', UserInfo.as_view()),
    path('changePassword/', ChangePassword.as_view()),
]