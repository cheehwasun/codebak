#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-20 14:58:11
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

#遍历文件夹 生成序列化JS 或者sqlite3

import os


def gitrun(path,origin='origin',branch='dev'):
    os.chdir(path)
    cmd=['git add .','git commit -m "auto"','git push %s %s'%(origin,branch)]
    for each in cmd:
        p=os.popen(each)
        p.read()


            
if __name__ == '__main__':
    import time
    t1=time.time(70000)
    time.sleep()
    path=r'd:\文档\sublime3\code'
    gitrun(path)

    t2=time.time()
    print(t2-t1)