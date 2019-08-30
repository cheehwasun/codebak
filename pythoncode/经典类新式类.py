#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:15:38
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# class_newold # 新式类 和 经典类(旧式类) 的演示
# 他们的区别主要体现在继承上
# Python2.x 找父类初始化函数时, 经典类 按深度优先查找 新式类 按广度优先查找
# Python3.x 找父类初始化函数时, 经典类 和 新式类 都是广度优先查找


# === 经典类 ===
class Ao:
    def __init__(self):
        print("Ao")

    def show(self):
        print("s Ao")


class Bo(Ao):
    def __init__(self):
        print("Bo")

    def show(self):
        Ao.show(self)  # 经典类写法(执行指定的父类函数)
        print("s Bo")


class Co(Ao):
    def __init__(self):
        print("Co")

    def show(self):
        Ao.show(self)
        print("s Co")


class Do(Bo, Co):
    def show(self):
        Bo.show(self)
        Co.show(self)
        print("s Do")




# === 新式类 ===
class An(object):
    def __init__(self):
        print("An")

    def show(self):
        print("s An")


class Bn(An):
    def __init__(self):
        print("Bn")

    def show(self):
        super(Bn, self).show()  # 新式类写法(按父类顺序自己执行)
        print("s Bn")


class Cn(An):
    def __init__(self):
        print("Cn")

    def show(self):
        super(Cn, self).show()
        print("s Cn")


class Dn(Bn, Cn):

    def show(self):
        super(Dn, self).show()
        print("s Dn")



if __name__ == "__main__":
    # 创建对象
    # 初始化 __init__(self)时,只要找到一个就执行初始化,不会再继续执行第二个
    do = Do()  # => Bo
    dn = Dn()  # => Bn

    # 初始化查找顺序为:
    # Python2.x: Bo -> Ao -> Co / Bn -> Cn -> An
    # Python3.x: Bo -> Co -> Ao / Bn -> Cn -> An
    # Python2.x 找父类初始化函数时, 经典类 按深度优先查找 新式类 按广度优先查找
    # Python3.x 找父类初始化函数时, 经典类 和 新式类 都是广度优先查找

    do.show()  # s Ao => s Bo => s Ao => s Co => s Do (自行决定调用)
    dn.show()  # s An => s Cn => s Bn => s Dn (深度优先调用)
