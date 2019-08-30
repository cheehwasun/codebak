#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-20 14:58:11
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

#遍历文件夹 生成序列化JS 或者sqlite3

import os
import json
import sqlite3

from itertools import *



#chain迭代器文件多时方便
class dirtree(object):
    """docstring for dirtree2"""
    def __init__(self, dira):
        self.dira = [dira]
        self.files=[]
        self.i=len(dira)
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
                        self.files.append(each)
            except Exception as e:
                print(e)
    #序列化json
    def serial(self,file):
        self.run()
        self.dic={}
        for each in self.files:
            self.dic[each.path[self.i:]]=(each.stat().st_size,each.stat().st_mtime)
        try:
            with open(file,'w+') as f:
                json.dump(self.dic,f,ensure_ascii=False,indent=2)
                f.close()
        except Exception as e:
            print(e)
        # with open(file,'w+') as f:
        #     yaml.safe_dump(self.dic,f)
        #     f.close()

    #sqlite3 存储
    def dbin(self,t):
        self.cursor.execute('insert into files values(?,?,?)',t)
    def dbquery(self):
        self.cursor.execute('select * from files order by path')
    def mktable(self):
        try:
            self.cursor.execute('DROP TABLE files')
        except Exception as e:
            pass
        self.cursor.execute('create table files (path text primary key,size real,mtime real)')

    def conndb(self,db):
        self.conn=sqlite3.connect(db)
        self.cursor=self.conn.cursor()
    def closedb(self):
        self.cursor.close()
        self.conn.close()   

    def mkdb(self,db):
        self.run()
        try:
            self.conndb(db)
            self.mktable()
            for each in self.files:
                t=(each.path[self.i:],each.stat().st_size,each.stat().st_mtime)
                self.dbin(t)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.closedb()

    def showdb(self,db):
        try:
            self.conndb(db)
            self.dbquery()
            i=0
            for each in self.cursor.fetchall():
                # print(each)
                i+=1
            print(i)
            self.cursor.close()
        except Exception as e:
            print(e)
        finally:
            self.closedb()
            
if __name__ == '__main__':
    import time
    t1=time.time()
    db='files.sqlite3'
    dira=r'd:\test'
    t=dirtree(dira)
    # t.serial('1.json')
    #asdlk
    # i=0
    # for each in t.files:
    #     i+=1
    # print(i)
    # t.mkdb(db)
    # t.showdb(db)
        

    # t.showdb(db)
    t2=time.time()
    print(t2-t1)