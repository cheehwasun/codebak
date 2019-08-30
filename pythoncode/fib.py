#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-05 10:05:37
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$


class Fibs(object):
    """docstring for Fibs"""

    def __init__(self, arg=100):
        self.a = 0
        self.b = 1
        self.max = arg

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.max:
            raise StopIteration
        return self.a


if __name__ == '__main__':
    fib = Fibs()
    for each in fib:
        print(each)
