#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-30 00:10:41
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

from django.conf.urls import url
from . import views

# 反斜杠很重要
    # url(r'^$', views.index),
    # url(r'^article/(?P<article_id>[0-9]+)$', views.article,name='a1'),
    # url(r'^edit/$', views.edit,name='edit'),
    # url(r'^edit/action/$', views.edit_action,name='edit_action'),
    # url(r'^ok.html$', views.ok),
urlpatterns = [
    # url(r'^$', views.cache),
    url(r'^$', views.test),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^home/$', views.home),

    url(r'^deltest/$', views.deltest),
    url(r'^ajaxtest/$', views.ajaxtest),
    url(r'^uploadtest/$', views.uploadtest),
    
    url(r'^ajaxpagetest/(?P<param>[0-9]+)/$', views.ajaxpagetest,name='ajaxpagetest'),
    url(r'^ajax_list/$', views.ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', views.ajax_dict, name='ajax-dict'),
]
