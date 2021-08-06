# coding=utf-8
"""
date: 2021/6/27 19:02
author: lee sure
"""
from django.urls import path

from . import views

# 在根 URLconf 中添加命名空间。在 polls/urls.py 文件中稍作修改，
# 加上 app_name 设置命名空间：为了区分重名url
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('specifics/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]