from django.urls import path
from order.views import *


urlpatterns = [
    path('orderInfo/', OrderInfo.as_view()),
    # path('addOrder/', addOrder),
]