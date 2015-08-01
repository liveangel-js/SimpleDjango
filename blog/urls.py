# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'
from django.conf.urls import *
from blog.views import *

urlpatterns = patterns('',
                       url(r'^$', archive),
                       )

urlpatterns +=patterns('',
                       url(r'^new_archive$', new_archive),
                       )

urlpatterns += patterns('blog.views',
                        url(r'^view1/$',views,{'template_name':'view1.html'}),
                        url(r'^view2/$',views,{'template_name':'view2.html'}),
                        )
#渲染VIEW前先进行公共处理，如权限检测，安全控制
urlpatterns += patterns('blog.views',
                        (r'^commonview1/$',commonviews(view1)),
                        url(r'^commonview2/$',commonviews(view2)),
                        )