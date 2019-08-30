#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-31 16:06:32
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# 自定义__len__ 和__getitem__ 可以记录某个值的访问次数


class M1(object):
    """docstring for M1"""

    def __init__(self, *args)：
        self.values = [x for x in args]
        self.dic = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.dic[key] += 1
        return self.values[key]
