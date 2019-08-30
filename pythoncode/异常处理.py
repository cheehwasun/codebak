#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:03:55
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

import sys

# === 捕获异常 (可灵活组合) ===
def excep():
    # - try except -
    try:
        print(ex)
    except: # 捕获所有异常
        print("捕获异常!")

    try:
        print(ex)
    except: # 通过函数获取异常信息
        types, value, back = sys.exc_info() # 捕获异常
        sys.excepthook(types, value, back)  # 打印异常

    try:
        print(ex)
    except NameError: # 捕获指定异常
        print("捕获名字未定义异常!")
    except IOError:
        print("捕获IO异常!")
    except:
        print("捕获所有异常!")

    try:
        print(ex)
    except (NameError, IOError) as e: # 同时捕获多个异常, 并告知异常原因
        print("捕获多个异常!")
        print(e)
    except:
        print("捕获所有异常!")


    # - try except else -
    try:
        pass
    except:
        print("捕获异常!")
    else: # 没有发生异常是执行该代码块
        print("运行正常.")

    # - try except else finally -
    try:
        pass
    except:
        print("捕获异常!")
    else:
        print("运行正常.")
    finally: # 不管是否发生异常都执行
        print("不管是否发生异常都执行")




# === 自定义异常 ===
# - 编写自定义异常 -
class MyError(Exception): # 继承 Exception

    # 重写并super构造
    def __init__(self, mes = "抛出一个异常."):
        Exception.__init__(self)
        self.message = mes

    def __str__(self):
        return self.message


# - 使用自定义异常 - 
def myerr():
    try:
        raise MyError("抛异常!") # 抛出异常
    except MyError as e: # 接住异常
        print(e)




# === 断言语句 ===
def assertdemo():
    # 断言一般用于测试, 如果测试结果为Flase,将抛出AssertionError异常
    assert 3 > 4

    assert 3 > 4, "抛AssertionError异常"

    assert type("string") is str





# ======= 函数调用 ======
if __name__ == "__main__":
    excep()
    myerr()
    assertdemo()
# ======= 函数调用 ======
