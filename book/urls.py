# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'
from django.conf.urls import *
from book.views import *
from blog.views import *

urlpatterns = patterns('',
                       url(r'^$', booklist),
                       url(r'^new_session$', session)
                       )