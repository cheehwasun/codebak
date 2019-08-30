#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:11:50
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

#coding=utf-8
# pickledemo.py Pickle
# 用于对Python对象进行序列化和反序列化的二进制协议

import pickle

def demo():
    # --- 序列化 ---
    f = open("pickle.txt", "wb+")
    lists = [123, "中文", [456]]
    strs = "字符串"
    num = 123

    # 写入
    pickle.dump(lists, f) # 序列化到文件
    pickle.dump(strs, f)
    pickle.dump(num, f)

    # 关闭
    f.close()


    # --- 反序列化 ---
    f = open("pickle.txt", "rb+")

    # 读取
    data = pickle.load(f) # 从文件反序列化
    print (data)
    data = pickle.load(f)
    print(data)
    data = pickle.load(f)
    print(data)

    f.close()


def pickle_funs():
    lists = [123, "中文", [456]]
    f = open("pickle.txt", "wb+") # (注:wb+二进制读写)

    num = pickle.HIGHEST_PROTOCOL # 目前最高的酸洗协议(4)
    num = pickle.DEFAULT_PROTOCOL # 默认的酸洗协议(3) {3:明确支持bytes对象; 4:更多种类的对象和数据格式优化的支持}

    # --- 序列化 ---
    # dump(obj, file, protocol=None, *, fix_imports=True) // 将obj写入文件
    pickle.dump(lists, f)
    # dumps(obj, protocol=None, *, fix_imports=True) // 将obj写入bytes
    bytes = pickle.dumps(lists)

    # --- 反序列化 ---
    # load(file, *, fix_imports=True, encoding="ASCII", errors="strict") // 从file读取obj对象
    lists = pickle.load(f)
    # loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict") // 从bytes读取obj对象
    lists = pickle.loads(bytes)

    # --- 异常 ---
    try:
        pass
    except pickle.PicklingError: # 序列化时异常
        pass
    except pickle.UnpicklingError: # 反序列化时异常
        pass
    except pickle.PickleError: # pickling异常的公共基类
        pass



if __name__ == "__main__":
    demo()
    pickle_funs()




# shelve_demo.py 持久性字典:Python对象的持久化
# 键值对形式, 将内存数据通过文件持久化, 值支持任何pickle支持的Python数据格式
# 与pickle的主要区别是键值对方式, 并且在目录下生成三个文件

import shelve


class Person(object):
    def __init__(self):
        self.name = "luzhuo"
        self.age = 21

    def __str__(self):
        return "name: {}, age: {}".format(self.name, self.age)

path = "file.txt"


def shelve_write():
    '''
    序列化
    '''

    with shelve.open(path) as write: # 打开
        write["nums"] = [1, 2, 3, 4, 5]  # 写
        write["obj"] = Person()


def shelve_read():
    '''
    反序列化
    '''

    with shelve.open(path) as read:  # 打开
        nums = read.get("nums")  # 读取
        print(nums)
        clazz = read["obj"]
        print(clazz)

        del read["obj"]  # 删除
        print("obj" in read)

        keys = list(read.keys())  # 所有key
        print(keys)


def shelve_func():
    # 打开, filename:文件名, writeback:是否回写(True回写,耗内存), 返回Shelf对象
    # shelve.open(filename, flag='c', protocol=None, writeback=False)
    d = shelve.open(path)

    # Shelf
    # 支持字典支持的所有方法
    # get(self, key, default=None) // 获取 == data = shelf["key"]
    data = d.get("key")
    d.sync()  # 同步(清空缓存,同步磁盘)
    d.close()  # 同步并关闭


    # class shelve.Shelf(dict, protocol=None, writeback=False, keyencoding='utf-8')
    # class shelve.BsdDbShelf(dict, protocol=None, writeback=False, keyencoding='utf-8') // Shelf的子类
    # class shelve.DbfilenameShelf(filename, flag='c', protocol=None, writeback=False) // Shelf的子类


if __name__ == "__main__":
    shelve_write()
    shelve_read()

    # shelve_func()
