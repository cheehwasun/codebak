#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-01 21:00:40
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag  #自定义标签
#@register.filter #自定义filter
def func():
    return 123
    
def my_input():
	result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
	return mark_safe(result)