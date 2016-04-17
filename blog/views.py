# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import *

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts': posts})
    name = "Hi I am session"
    print name
    request.session["name"]=name
    request.session["process_view"]="dd"
    print __name__+"Set Session:"+name
    return HttpResponse(t.render(c))

def new_archive(request):
    posts = Archive.objects.all()
    t = loader.get_template("new_archive.html")
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))
def view1(request):
    return render_to_response('view1.html')

def view2(request):
    return render_to_response('view2.html')

def views(request,template_name):
    return render_to_response(template_name)

def session(request):
    name = request.session["name"]
    process = request.session["process_view"]
    return HttpResponse(name+"::"+process)

#处理GET请求
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)  + int(b)

    return HttpResponse(str(c))

#增加http://127.0.0.1:8000/blog/add/4/7/ 这种访问方式
def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

#在每个视图渲染前，进行公共处理的函数
def commonviews(func):
    def view(request):
        #do common something
        return func
    return view

def simple_angular(request):
    return render(request,'simple_angular.html')