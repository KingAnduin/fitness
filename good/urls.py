from django.urls import path
from good.views import *


urlpatterns = [
    path('goodInfo/', GoodInfo.as_view()),
    path('getUnavailablePeriod/', get_unavailable_period),
]