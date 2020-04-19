from django.urls import path
from comments.views import *


urlpatterns = [
    path('CommentsInfo/', CommentsInfoView.as_view()),
    path('commentsByUser/', get_comment_by_user),
    path('commentsByGood/', get_comment_by_good),
]