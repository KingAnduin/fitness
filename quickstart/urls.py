from django.urls import path
from quickstart.views import *


urlpatterns = [
    path('music/', MusicList.as_view()),
    path('auth/', AuthView.as_view()),
]