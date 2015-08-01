# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'
from django.conf.urls import *
from book.views import *

urlpatterns = patterns('',
                       url(r'^$', booklist),
                       )