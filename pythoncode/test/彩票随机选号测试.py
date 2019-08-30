#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 随机模拟彩票选号

import random
import sys


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


def choiceType():
    while True:
        s = input("请选择彩票类型:\n1: 大乐透\n2: 双色球\n按Q退出:")
        if s == 'q':
            isquit()
        elif s != '1'and s != '2':
            print("选择错误,没有该选项\n")
            continue
        else:
            return int(s)


def choiceNums():
    while True:
        s = input("请选择投注注数：")
        if s == 'q':
            isquit()
        try:
            return int(s)
        except:
            print("注数错误\n")
            continue


def isquit():
    try:
        sys.exit()
    except SystemExit as e:
        raise e


if __name__ == '__main__':
    l = lottery(choiceType(), choiceNums())
    l.run()
