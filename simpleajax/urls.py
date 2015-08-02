# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'
from django.conf.urls import *
from simpleajax.views import *

urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^ajax_list/$', ajax_list, name='ajax-list'),
                       url(r'^ajax_dict/$', ajax_dict, name='ajax-dict'),
                       url(r'^ajaxshow/$', ajaxshow)

                       )