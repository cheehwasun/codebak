#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-06 12:01:46
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

#yield 用法 相当与return 不过函数变成迭代器generator 需要next调用或者用于for in 中
#迭代器各个实例之间不冲突
def fib(max=1000):
        a=0
        b=1
        while True:
                a,b=b,a+b
                if a>max:
                        break
                yield a
