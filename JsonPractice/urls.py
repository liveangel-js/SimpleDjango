# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'
from django.conf.urls import *
from JsonPractice.views import *

urlpatterns = patterns('',
                       url(r'^$', home),
                       url(r'^json$', jsontest),
                       )