#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:02:43
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

import sys  # 导入模块
sys.setrecursionlimit(5000)  # 修改函数递归次数限制(默认为1000)


# === 函数 ===
def function1():  # 无参函数
    print("×参数 ×返回")  # 无返回


def function2(arg1, arg2):  # 带参函数(位置参数)
    return "√参数 √返回"  # 有返回


def function2_1(arg1, arg2):
    return arg1, arg2  # 元组形式返回多个值


def function3(*args):  # 不定长参数(位置参数),把位置参数(*args)转成元组
    print("function3: ", args)


def function3_1(**kwargs):  # 不定长参数(关键字参数), 把关键字参数(**kwargs)转成字典
    print("function3_1: ", kwargs)


def function4(arg1=5):  # 缺省参数(不传参将使用默认值)(注意:Python不支持函数重载,该方式解决了重载问题)
    print("function4:%s" % arg1)


def function5(arg1):
    print("function5:%d" % arg1)
    if(arg1 >= 10):
        return
    arg1 += 1
    return function5(arg1)  # 递归函数(默认递归次数限制为1000), 递归层次太多可能会导致栈溢出(递归效率不高)


def none(): return print("none")  # 匿名函数 (无参 无返回)


def add(arg1, arg2): return arg1 + arg2  # 匿名函数 (带参 有返回)


# === 位置参数 和 关键字参数 的混合使用 ===
def function6(arg, *args):
    print("function6: ", arg)
    print("function6: ", args)


def function7(arg, age=21, **kwargs):
    print("function7: ", arg)
    print("function7: ", age)
    print("function7: ", kwargs)


def function8(arg, age=21, *args, **kwargs):  # 位置参数 只能写在 关键字参数 前面
    print("function8: ", arg)
    print("function8: ", age)
    print("function8: ", args)
    print("function8: ", kwargs)



# === 变量 ===
global_var = 123  # 全局变量,作用域整个程序
global_var_c = 321


def localvariable():
    local_var = 456  # 局部变量, 作用域在子程序
    global_var_c = 123  # 子程序不能修改全局变量(引用(如:list,class)除外)
    print("global_var: {}; global_var_c: {}; local_var: {}".format(
        global_var, global_var_c, local_var))  # => 123, 123, 456


localvariable()
print("global_var: {}; global_var_c: {}".format(
    global_var, global_var_c))  # => 123, 321


# === 修改全局变量 ===
global_list = {"num": 123}


def localvariable_cg():
    global_list["num"] = 321
    print("global_list: {}".format(global_list))  # => {'num': 321}


localvariable_cg()
print("global_list: {}".format(global_list))  # => {'num': 321}


# === 修改全局变量的作死写法 (不建议使用这种写法, 容易造成全局变量使用混乱) ===
global_err = 123


def localvariable_err():
    global global_err
    global_err = 321
    print("global_err: {}".format(global_err))  # => 321


localvariable_err()
print("global_err: {}".format(global_err))  # => 321


if __name__ == "__main__":
    # --- 普通函数 ---
    function1()
    print(function2("a", "b"))
    print(function2_1("a", "b"))
    function3(1, 2, 3)
    function3(*[1, 2, 3])
    function3_1(a="A", b="B", c="C")
    function3_1(**{"a": "A", "b": "B", "c": "C"})
    function4(3)
    function5(1)
    # --- 匿名函数 ---
    none()
    print(add(1, 5))
    print((lambda arg1, arg2: arg1 + arg2)(1, 2))  # 匿名函数的另一种调用方式

    # --- 位置参数 和 关键字参数 的混合使用 ---
    function6(1, 2, 3, 4, 5)
    function6(1, *[2, 3, 4, 5])
    function7(1, num=12, age=21)
    function8(1, 22, 2, 3, num=12)


# ===========================================================
# === 调用自定义模块 ===

# 导入模块并调用 (三种导入模块方式,选择其中一种)
import time  # 第一种, 引入单个模块
import time as t  # 引入并重命名
import time
import calendar  # 第二种, 引入多个模块
from mymodule import myfunction  # 第三种, 导入模块指定函数(*引入所有)
print(myfunction())


# === 动态导入模块 ===
import importlib
modulename = "os"

# 方式1
obj = __import__(modulename)  # 不推荐
# 方式2
obj = importlib.import_module(modulename)  # 推荐使用

print(obj.getcwd())
