# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'

class MyMiddleware(object):
    def __init__(self):
        print 'Hello, this is mymiddleware!'

    def process_view(self, request, func, args, kwargs):
        print func
