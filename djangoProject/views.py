# coding=utf-8
"""
date: 2021/6/27 14:45
author: lee sure
"""
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'runoob.html', context)
