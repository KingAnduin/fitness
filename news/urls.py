from django.urls import path
from news.views import *


urlpatterns = [
    path('newsInfo/', NewsInfo.as_view()),

]