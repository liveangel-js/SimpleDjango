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
    print request.session.session_key
    print request.session.get(request.session.session_key)
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

"""
Session示例
比如写一个不让用户评论两次的应用：
"""
def post_comment(request):
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')

"""
Session示例
一个简化的登陆认证：
"""
def login(request):
    id = 1
    password = 2
    if password == int(request.GET['password']):
        request.session['member_id'] = id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")


def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

