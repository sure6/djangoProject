# -*- coding: UTF-8 -*-
"""
@File: urls.py
@Description:
@Author: Xuan Li(6732409)
@DateTime: 18/12/2022 18:50 
@Project_name: djangoProject
@IDE: PyCharm 
"""
from django.urls import path

from . import views

app_name='demo'
urlpatterns=[
    path("",views.index, name="demo"),
    path("addinfo/", views.addInfo, name="addinfo"),
    path("saveinfo/", views.saveInfo, name="saveinfo"),
    path("deteteinfo/<int:id>", views.deteteinfo, name="deteteinfo"),
    path("updateinfo/<int:id>", views.updateInfo, name="updateinfo"),
]