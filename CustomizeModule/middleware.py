# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'



class CustomizeMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request):
        print "hello mymiddle::requets"
        print "request::path-"+request.path
        print "requets::body-"+request.GET.urlencode()
        print request.COOKIES.keys()
        print request.COOKIES.values()
        print request.META
        if request.user.is_authenticated():
            print "Hi, I have logged"
            # do someting for login
        else:
            # do something for anonymous
            print "Hi, I haven't login"
        print request.get_host()
        print request.get_full_path()
        print request.build_absolute_uri()
        print request.is_secure()


    def process_view(self,request, view_fun, view_args, view_kwargs):
        print "hello process::view"
        print view_args
        print view_kwargs

    def process_exception(self):
        print "hello process exception"

    # def process_template_response(self, request, response):
    #     print "hello process template"
    #     # return

    def process_response(self, request, response):
        print "hello process response"
        return response
