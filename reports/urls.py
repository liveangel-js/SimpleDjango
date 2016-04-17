# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'
from django.conf.urls import *
from . import views

urlpatterns = [
                url(r'^$', views.index),
                url(r'^charts$', views.charts),
                url(r'^table$', views.table)


                       ]