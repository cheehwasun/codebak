#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:14:11
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# decorator.py 装饰器
# 装饰器: 本质是函数, 用于装饰其他函数, 附加一些本身所没有的功能


# 函数就是变量
def num():
    print("num")

num()
num = 1  # 函数就是变量
# num()  # num的引用被指向1,不能再调用

# ========================================


# 高阶函数
def func_1():
    print("func_1")


def func_2(func):  # 接收函数变量
    func()

func_2(func_1)  # => func_1

# ========================================


# 闭包
def func_3(line):
    # 闭包: 用于代码封装 和 复用
    def comp(value):  # 嵌套函数: 函数里再嵌套一个函数
        # 函数set_line执行完(生命周期结束), 自由变量(line)仍存活于包裹内
        if value >= line:
            print("{} >= {}".format(value, line))
        else:
            print("{} < {}".format(value, line))

    return comp

f = func_3(60)  # 调用函数A(set_line()),返回函数B(cmp()),这个函数B就叫闭包
f(89)  # => 89 >= 60
f(59)  # => 59 < 60

# ========================================


# 装饰器, 在不修改my_average()代码的情况下,为其添加了一些功能(wrapper())
def dec_1(func):
    def wrapper(num1, num2):

        # --- 附加功能 ---
        if num2 == 0:
            print("num2 值不能为0")

        return func(num1, num2)
    return wrapper


# 普通调用方式
def average_1(num1, num2):
    return num1 / num2

average_1 = dec_1(average_1)
print(average_1(5, 3))  # => 1.6666666666666667


# 使用@语法糖的方式
@dec_1  # (sum = dec(sum))
def sum_1(num1, num2):
    return num1 + num2

print(sum_1(5, 3))  # => 8

# ========================================


# 能接收任何参数的通用装饰器
def dec_2(func):
    def wrapper(*arg, **kwargs):

        # --- 附加功能 ---
        print("loging i ...")

        return func(*arg, **kwargs)
    return wrapper


@dec_2
def average_2(num1, num2):
    return num1 / num2

print(average_2(5, 3))  # => loging i ... => 1.6666666666666667


@dec_2
def sum_2(*args):
    return sum(args)

print(sum_2(5, 3, 2, 1))  # => loging i ... => 11

# ========================================


# 能接收不同参数的装饰器
def auth(auth_type): # 在外面套一层
    def dec_3(func):
        def wrapper(*arg, **kwargs):
            # --- 附加功能 ---
            if auth_type == "admin":
                print("你是管理员")
            elif auth_type == "user":
                print("你是普通用户")
            else:
                print("你是外星人吗?")

            return func(*arg, **kwargs)
        return wrapper
    return dec_3


# 普通调用方式
@auth(auth_type="admin")
def average_3(*arg):
    return sum(arg) / len(arg)

print(average_3(1, 2, 3, 4, 5))  # => 你是管理员 => 3.0


@auth(auth_type="user")
def sum_3(*arg):
    return sum(arg)

print(sum_3(5, 3, 2, 1))  # => 你是普通用户 => 11


# ========================================


# 使用多个装饰器
@dec_1
@dec_2
@auth(auth_type="admin")
def average_2(num1, num2):
    return num1 / num2

# 执行顺序dec_1 => dec_2 => auth => average_2
print(average_2(5, 3))  # => loging i ... => 你是管理员 => 1.6666666666666667
