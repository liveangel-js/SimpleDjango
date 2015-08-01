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

"""
#url name参数作用
使用
>>> reverse('add2', args=(44,5555))
u'/blog/add/44/5555/'
获得URL的地址，避免了硬编码

在模板中的使用
不带参数的：
{% url 'name' %}
带参数的：参数可以是变量名
{% url 'name' 参数 %}

<a href="{% url 'add2' 4 5 %}">link</a>
等同
<a href="/add/4/5/">link</a>
"""
urlpatterns += patterns('',
                        url(r'^add/$', add, name='add'),
                        url(r'^add/(\d+)/(\d+)/$', add2, name='add2'),
                        )