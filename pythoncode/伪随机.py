#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:13:17
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# coding=utf-8
# randomdemo.py random伪随机数
# 生成伪随机 整数 和 浮点数, 随机获取列表元素

import random  # 随机数模块

lists = [1, 2, 3, 4, 5]

# 常见的一些demo


def demo():

    random.seed()

    # 产生[0, 100]随机整数
    num = random.randint(0, 100)
    print(num)

    # 产生[0, 100)随机浮点数
    fnum = random.uniform(0, 100)
    print(fnum)

    # 随机获取元素
    elem = random.choice(lists)
    print(elem)

    # 从列表中随机获取3个元素
    elems = random.sample(lists, 3)
    # 打乱顺序
    random.shuffle(lists)
    print(lists)

# 模拟随机弄大乐透和双色球的案例


class lottery(object):
    """docstring for lottery"""
    # tuple(35,12,5,2)根据元组进行切片

    def __init__(self, choice=1, nums=1):
        self.list = [str('{0:0>2}'.format(x)) for x in range(1, 40)]
        self.nums = nums
        self.dic = {1: (35, 12, 5, 2), 2: (33, 16, 6, 1)}
        self.tuple = self.dic[choice]
        self.l = self.list[0:self.tuple[0]]
        self.r = self.list[0:self.tuple[1]]

    # 从list里随机选出个数
    def _format(self):

        self.red = random.sample(self.l, self.tuple[2])
        self.blue = random.sample(self.r, self.tuple[3])
        self.red.sort()
        self.blue.sort()

    # 创建一个迭代器可以控制选几个号
    def _makeIter(self):
        a = 0
        while a < self.nums:
            a += 1
            self._format()
            yield ('前区： ' + '--'.join(self.red) + '     后区：  ' + '--'.join(self.blue))

    def run(self):
        self._makeIter()
        for each in self._makeIter():
            print(each)


def funs():
    # seed(a=None, version=2) // 初始换生成器的随机数
    random.seed()
    random.getstate()  # 获取生成器内部状态
    random.setstate(random.getstate())  # 设置生成器内部状态

    # 获取随机数
    num = random.getrandbits(8)  # 获取x位(bit)随机整数
    # randrange(stop) / randrange(start, stop[, step]) // 生成随机整数
    num = random.randrange(0, 100, 2)  # [0,100)产生的随机整数+2
    # randint(a, b) == randrange（a， b + 1) // [a, b]
    num = random.randint(0, 1)
    fnum = random.random()  # 获取浮点随机数 [0.0, 1.0)
    fnum = random.uniform(1, 2)  # 获取指定范围内的浮点随机数 [1.0, 2.0)

    # triangular(low, high, mode) // 获取随机浮点数, low低边界(默认0),high高边界(默认1),模式(默认边界中点)
    fnum = random.triangular(0, 1, 1.5)
    # betavariate(alpha, beta) // Beta分布,[0.0, 1.0]
    fnum = random.betavariate(1, 1)
    # expovariate(lambd) // 指数分布, lambd返回整,值[0, +∞]; lanbd返回负,值[-∞, 0]
    fnum = random.expovariate(
        (lambda arg1, arg2: arg1 + arg2)(1, 2))  # lambd返回值越小,获得值越大
    # gammavariate(alpha, beta) // 伽玛分布
    fnum = random.gammavariate(1, 1)
    # gauss(mu, sigma) // 高斯分布 mu:平均值, sigma:标准偏差
    fnum = random.gauss(1, 1)
    # lognormvariate(mu, sigma) // 对数正态分布,获得平均值mu和标准偏差sigma的正态分布; mu:任何值,sigma:>0。
    fnum = random.lognormvariate(1, 1)
    # normalvariate(mu, sigma) // 正态分布, mu是平均值, sigma是标准偏差
    fnum = random.normalvariate(1, 1)
    # vonmisesvariate(mu, kappa) // 冯米塞斯分布的随机数。mu:平均角度(弧度[0, 2*pi]), kappa:集中程度>=0
    fnum = random.vonmisesvariate(1, 1)
    # paretovariate(alpha) // 帕累托分布, alpha:形状
    fnum = random.paretovariate(1)
    # weibullvariate(alpha, beta) // 韦伯分布, alpha:缩放, beta:形状
    fnum = random.weibullvariate(1, 1)

    elem = random.choice(lists)  # 非空序列中取出随机元素, 序列为空抛IndexError
    elems = random.sample(lists, 3)  # 从列表中随机获取3个元素, 范围>列表大小,抛ValueError

    # 打乱顺序
    random.shuffle(lists)  # 打乱序列


if __name__ == "__main__":
    demo()
