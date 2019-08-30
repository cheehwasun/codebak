#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:13:52
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# copydemo.py copy深和浅拷贝
# 深浅拷贝区别:
# 1.浅拷贝:创建新的复合对象，然后将'引用'拷贝到该复合对象中。
# 2.深拷贝:创建新的复合对象，然后'递归地将原始对象'拷贝到该复合对象中

import copy


class Ls:
    def __init__(self, name):
        self.name = name

    @property
    def setname(self, name):
        self.name = name

    def __str__(self):
        return self.name

    __repr__ = __str__

    def __iter__(self):
        return self


list_0 = ["A", "B", ["C", "D"], Ls("E")]


def demo():
    # --- 浅拷贝的拷贝方式 ---
    list_1 = copy.copy(list_0)
    list_2 = list_0.copy()
    list_3 = list_0[:]
    list_4 = list(list_0)

    # --- 深拷贝的拷贝方式 ---
    lists_d = copy.deepcopy(list_0)

    # --- 深浅拷贝的区别 ---
    # 1. 对第一层数据进行赋值
    list_0[0] = "X0"
    list_1[0] = "X1"
    list_2[0] = "X2"
    list_3[0] = "X3"
    list_4[0] = "X4"
    lists_d[0] = "Xd"

    # 打印结果: 理所当然,所有列表都发生了变化
    # list_0: ['X0', 'B', ['C', 'D'], E]
    # list_1: ['X1', 'B', ['C', 'D'], E]
    # list_2: ['X2', 'B', ['C', 'D'], E]
    # list_3: ['X3', 'B', ['C', 'D'], E]
    # list_4: ['X4', 'B', ['C', 'D'], E]
    # list_d: ['Xd', 'B', ['C', 'D'], E]

    # 2. 对第二层的list引用进行赋值
    list_0[2][0] = "Y0"
    list_1[2][0] = "Y1"
    list_2[2][0] = "Y2"
    list_3[2][0] = "Y3"
    list_4[2][0] = "Y4"
    lists_d[2][0] = "Yd"

    # 打印结果: 0-1都被改成了同一个值,这说明浅拷贝只拷贝了第二层list的引用;而深拷贝则拷贝了数据结构
    # list_0: ['X0', 'B', ['Y4', 'D'], E]
    # list_1: ['X1', 'B', ['Y4', 'D'], E]
    # list_2: ['X2', 'B', ['Y4', 'D'], E]
    # list_3: ['X3', 'B', ['Y4', 'D'], E]
    # list_4: ['X4', 'B', ['Y4', 'D'], E]
    # list_d: ['Xd', 'B', ['Yd', 'D'], E]

    # 3. 对第三层的Ls对象引用进行赋值
    list_0[3].name = "Z0"
    list_1[3].name = "Z1"
    list_2[3].name = "Z2"
    list_3[3].name = "Z3"
    list_4[3].name = "Z4"
    lists_d[3].name = "Zd"

    # 执行结果: 继续验证了上方论点
    # list_0: ['X0', 'B', ['Y4', 'D'], Z4]
    # list_1: ['X1', 'B', ['Y4', 'D'], Z4]
    # list_2: ['X2', 'B', ['Y4', 'D'], Z4]
    # list_3: ['X3', 'B', ['Y4', 'D'], Z4]
    # list_4: ['X4', 'B', ['Y4', 'D'], Z4]
    # list_d: ['Xd', 'B', ['Yd', 'D'], Zd]

    print("list_0: {}".format(list_0))
    print("list_1: {}".format(list_1))
    print("list_2: {}".format(list_2))
    print("list_3: {}".format(list_3))
    print("list_4: {}".format(list_4))
    print("list_d: {}".format(lists_d))


if __name__ == "__main__":
    demo()
