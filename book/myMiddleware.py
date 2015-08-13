# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'
from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import *


class MyMiddleware(object):
    def __init__(self):
        print 'Hello, this is mymiddleware!'

    def process_view(self, request, func, args, kwargs):

        print request
        print func
