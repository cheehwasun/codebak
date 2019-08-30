#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-20 14:58:11
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

#遍历文件夹几种方法，前三种scandir明显好于45 的listdir

import os
import pickle,json,datetime

path=r"d:\test\code"
from itertools import *
#scandir 方便比较
class dirtree1(object):
    """docstring for scan"""
    def __init__(self, dira):
        self.dira = [dira]
        #0存文件名和文件的信息，1存目录
        self.ret={}
    def run(self):
        while True:
            try:
                #堆栈式获得目录
                path=self.dira.pop()
            except Exception as e:
                break
            try:
                for each in os.scandir(path):
                    if each.is_dir():
                        self.dira.append(each.path)
                    if each.is_file():
                        self.ret[each.path]=each
            except Exception as e:
                print(e)

#chain迭代器文件多时方便
class dirtree2(object):
    """docstring for dirtree2"""
    def __init__(self, dira):
        self.dira = [dira]
        self.ret=[]
    def run(self):
        while True:
            try:
                #堆栈式获得目录
                path=self.dira.pop()
            except Exception as e:
                break
            try:
                for each in os.scandir(path):
                    if each.is_dir():
                        self.dira.append(each.path)
                    if each.is_file():
                        self.ret.append(each)
                self.files=chain(self.ret)
            except Exception as e:
                print(e)


#递归式 递归对象 利用chain生成器加速
import os
from itertools import *
class dirtree3():
    def __init__(self, dira):
        self.dira = dira
        self.res = {}
        # self.files={}

    def _scan(self):
        self.subdirs = []
        try:
            for each in os.scandir(self.dira):
                if each.is_dir():
                    #子目录对象组
                    self.subdirs.append(dirtree3(each.path))
                if each.is_file():
                    self.res[each.path]=each
            self.files=chain(self.res)

        except Exception as e:
            print(e)

    def run(self):
        self._scan()
        for each in self.subdirs:
            each.run()
            self.files = chain(self.files, each.files)


#利用chain 和listdir dirtree5变通
import os
from itertools import *
from stat import*
class dirtree4(object):
    """docstring for dirtree4"""
    def __init__(self, dira):
        self.dira = dira
        self.ret={}
    def _scan(self,dira):
        self.subdirs=[]
        try:
            for each in os.listdir(dira):
                path=os.path.join(dira,each)
                info=self._sig(os.stat(path))
                if S_ISDIR(info[0]):
                    self.subdirs.append(dirtree4(path))
                elif S_ISREG(info[0]):
                    self.ret[path]=info
                else:
                    print("unknowfile")
            self.files=chain(self.ret)
        except Exception as e:
            print(e)

    def run(self):
        self._scan(self.dira)
        for each in self.subdirs:
            each.run()
            self.files=chain(self.files,each.files)

    def _sig(self,st):
        return (st.st_mode,st.st_size,st.st_mtime)

#recursively listdir
import os
from stat import *
class dirtree5(object):
    """docstring for dirtree2"""
    def __init__(self, dira):
        self.dira = dira
        self.i=len(dira)
        self.files={}
        # self.ret=({},[])
    def run(self):
        return self._scan(self.dira)
    #扫描目录
    def _scan(self,dira):
        try:
            for each in os.listdir(dira):
                path=os.path.join(dira,each)
                info=self._sig(os.stat(path))
                if S_ISDIR(info[0]):
                    #目录看需求
                    # self.ret[1].append(path)
                    #递归扫描
                    self._scan(path)
                elif S_ISREG(info[0]):
                    #相对路径 方便比较生成Json
                    self.files[path[self.i:]]=info
                    # 绝对路径
                    # self.ret[0][path]=info
                else:
                    print('unknowfile')
        except Exception as e:
            print(e)

    def _sig(self,st):
        return (st.st_mode,st.st_size,st.st_mtime)

if __name__ == '__main__':
    import time
    t1=time.time()
    a=r'd:\test\code'
    b=dirtree1(a)
    b.run()
    t2=time.time()
    print(t2-t1)