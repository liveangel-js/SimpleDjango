# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'
from django.conf.urls import *
from JsonPractice.views import *

"""
该练习是输出静态输出json到js上
"""

urlpatterns = patterns('',
                       url(r'^$', home),
                       url(r'^json$', jsontest),
                       )