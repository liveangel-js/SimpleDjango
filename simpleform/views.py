# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext  as _

# Create your views here.
"""
使用普通的HTML表单
"""
def index(request):
    return render(request, 'index.html')

def i18n(request):
    return HttpResponse(_(u'Invalid Captcha'))

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse(str(int(a)+int(b)))


"""
使用Django的form验证
"""
from simpleform.form import AddForm

def djangoform(request):
    if request.method == 'POST':# 当提交表单时

        form = AddForm(request.POST) # form 包含提交的数据

        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:# 当正常访问时
        form = AddForm()
    return render(request, 'djangoform.html', {'form': form})

