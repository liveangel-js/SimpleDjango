# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
# Create your views here.


"""
这里用 Django 表单 第一节 中的一个例子，我们要实现的是在不刷新的情况下显示计算结果到页面上。
"""
def index(request):
    return render(request, 'indexajax.html')


"""
更复杂的例子，传递一个数组或字典到网页，由JS处理，再显示出来。
"""


def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)

def ajax_dict(request):
    name_dict = {'twz': 'Love python 我 Django'.decode('utf8').encode('utf8'), 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

def ajaxshow(request):
    if request.session.get('times', False):
        request.session['times'] += 1
    else:
        request.session['times'] = 0

    return render(request, 'indexajaxlist.html')