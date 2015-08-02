# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'
from django.conf.urls import *
from simpleform.views import *

urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^add/$', add, name='add'),
                       url(r'^djangoform/$', djangoform),
                       )