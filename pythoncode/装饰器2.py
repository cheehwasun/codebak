#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-10 18:52:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from functools import wraps

def a_new_decorator(func):
	@wraps(func) 	#重写名字和注释文档
	def wrapFunc():
		print('aa')
		func()
		print('bb')
	return wrapFunc

@a_new_decorator
def test_func():
	print('func')

test_func()

# outputs:aa
# 		func
# 		bb

# @本质就是把函数作为参数传到装饰器函数里，在函数之前或者之后做一些验证或者是记录


# 装饰器的应用

# 一.授权

from functools import wraps

def require_auth(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		auth=request.authorization
		#没有验证身份或者验证失败就继续验证
		if not auth or not check_auth(auth.name,auth.password):
			authenticate()
		return f(*args,**kwargs)

	return decorated

# 二。日志记录

from functools import wraps

def logit(func):
	@wraps(func)
	def with_logging(*args,**kwargs):
		print(func.__name__+'was called')
		return func(*args,**kwargs)
	return with_logging

@logit
def addition_func(x):
	return x+x


r=addition_func(4)




