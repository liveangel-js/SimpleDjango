# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from JsonPractice.models import *
import json


def home(request):
    a = ['json1', 'json2']
    print 'aaa'
    print json.dumps(a)
    a_json = json.dumps(a)

    return HttpResponse('Hello I am app JsonPractice homepage'+a_json)


def jsontest(request):
    Lista = ['json1', 'json2', 'json3']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'json.html', {
            'List': json.dumps(Lista),
            'Dict': json.dumps(Dict)
        })