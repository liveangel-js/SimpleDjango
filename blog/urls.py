# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'
from django.conf.urls import *
from blog.views import archive

urlpatterns = patterns('',
                       url(r'^$', archive),
                       )