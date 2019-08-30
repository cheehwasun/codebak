#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 13:57:05
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# 描述符实例 温度转换的。temperature不用管cel 和fah
# 之间市如何转换的。cel和fah两个描述符可以随时改变
# 他们之间的关系 instance 表示实例化cel和fah的那个类


class Celsius:
    def __init__(self, value=26.2):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Fahrenheit:
    def __init__(self, value=80):
        self.value = float(value)

    def __get__(self, instance, owner):
        return (instance.cel * 1.8) + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

    def __init__(self, value):
        self.cel = value
