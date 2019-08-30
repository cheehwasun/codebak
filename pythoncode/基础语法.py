#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:01:57
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

def helloworld():
    # === Hello World ===
    print("Hello World!") # 字符串用`'`或者`"`包裹
    print("中文") # 代码中包含中文时(包含中文注释)需要在首行添加该注释(#coding=utf-8)


def explanatorynote():
    # === 注释 ===
    # 单行注释
    ''' 这是
        多行
        注释 ''' 


def variable():
    # === 变量 ===
    num1 = 123 # 定义变量, Python能够自动识别数字变量类型
    result = 2 * num1 # 赋值变量
    # 变量命名规则:
        # 允许组成字符: a-z A-Z _ 0-9
        # 不能以数字开头
        # 区分大小写
        # 小驼峰命名法: name / userName / userName123
        # 大驼峰命名法: Person / UserName
    # Python命名规范
        # 项目名(大驼峰): MyAge
        # 包 / 模块 (全小写): myage.py
        # 类(大驼峰): MyAge / __MyAge
        # 属性(全小写): myage / __myage
        # 方法(全小写): myage / __myage / __init__
        # 对象(全小写): myage
        # 形式参数(全小写): myage
        # 异常(大驼峰 + Error): MyAgeError
        # > 简单归纳为: 类、异常、项目名  用大驼峰;  其余全小写(名字不易识别可加_)


def typeconversion():
    # === 数据类型 ===
    ''' 数字 (int / float / comples[复数])
        布尔 (True / False)
        字符串
        列表
        元组
        字典 '''
        # Python能够自动识别数字变量类型

    # === 数据类型强转 ===
    int("123") # (对象)转为整数
    float("1.23") # (对象)转为浮点数
    complex(0.1, 0.2) # 创建复数(= 0.1+0.2j)(实部和虚部都是float)
    str(123) # (对象)转为字符串
    repr("123") # (对象)转为表达式字符串(机器)
    eval("123*4") # 计算字符串内Python表达式
    tuple([1, 2, 3]) # (序列)转为元组 (注:将字典转为元组会损失数据)
    dict([(1, "a"), (2, "b")]) # (序列)转为字典 (列表 / 字典 均可)
    list((1, 2, 3)) # (序列)转为列表 (注:将字典转为列表会损失数据)
    chr(123) # (整数)转为字符
    ord("{") # (字符)转为整数
    hex(123) # (整数)转为十六进制字符串('0x7b')
    oct(123) # (整数)转为八进制字符串('0o173')
    bin(123) # (整数)转为二进制字符串('0b1111011')
    int('0o173', 8) # 将其他进制数转为(十进制)整数


def inputoutput():
    # === 输入 ===
    inputData = input("输入内容:") # 获取输入值(字符串),阻塞式
    print("输入的内容为:%s"%inputData)

    # === 打印值 ===
    name = "柳岩"
    age = 21
    print(name) # 普通的打印
    # 拼接打印
    print("Name:%s"%name)
    print("Name:%s  Age:%d"%(name, age)) # %a为ascii字符串 %c为字符; %s为字符串; %o为八进制整数; %d为有符号十进制整数; %u为无符号十进制整数; %x为十六进制整数; %e为浮点数指数; %f为浮点实数(%.2f:2位浮点数)
    print('%-10s %s'%(10, 10)) # %-10s 字符末尾+10个空格 => 10         10

# === 运算符 ===
# 算数运算符(+*可用于字符串拼接:str1+str2; str*3): + - * / % **(幂:2**3=8) //(取整除:3//2=1)
    # 扩展知识: 2**10=1K / 2**20=1M / 2**30=1G / 2**40=1T / 2**50=1P / ...
# 赋值运算符: =
# 复合运算符(自运算): a+=b (a=a+b) / a*=b (a=a*b) / ... / a+=b*c (a=a+(b*c)) / ...
# 关系运算符: > < == >= <= != <>(两边不相等为true)
# 逻辑运算符: and or not
# 位运算符: &(0b1001&0b1101=0b1001) |(0b1001|0b1101=0b1101) ^(0b1001^0b1101=0b0100) ~(~0b1001=1... 0110) <<(左移1位等于乘以2:2<<3=16) >>(最高位不变)


def judge():
    # === 判断语句 ===
    age = 22
    beatiful = True

    # - if (可嵌套) -
    if age > 21: # true ; >为关系运算符
        print("The Age is greater than 21.") # 用制表符区分代码段
        print("My thanks to you is beyond measure!")

    if age < 21: # false
        print("The Age is less than 21.")
        print("My thanks to you is beyond measure!")

    print("我从来不污,只是污的搬运工.")

    # - if else -
    if age > 18 and age < 25 and beatiful: # and为逻辑运算符
        print("I am really into you!")
    else:
        print("Bye.")

    boolean = True if 5 > 10 else False # 三元运算符
    print(boolean) # => False

    # - if elif else -
    if age > 18 and age < 25 and beatiful: # and为逻辑运算符
        print("I am really into you!")
    elif age < 18 and beatiful:
        print("你妈妈喊你回家吃饭啦.")
    else:
        print("Bye.")

    # - ×分支 (Python没有分支(switch)判断) - 


def loop():
    # === 循环语句 ===
    number1 = 5

    # - while (可嵌套) -
    while number1 <= 10:
        print("number:%d"%number1)
        number1+=1

    while True:
        print("True")
    else:
        print("False")

    # - for (可嵌套) -
    for i in range(5): # 循环5次
        print("for:range:%d"%i)

    lis = ["a", "b", "c"]
    for i in lis: # 按列表中的值循环
        print("for:ray:%s"%i)

    for i in range(10): # 循环10次后没有课循环元素, 执行else语句
        print(i)
    else:
        print("else")


def control():
    # === 控制语句 ===
    # - break - # 结束(一层)循环, 作用范围: for / while (无作用:if)
    for i in range(5):
        if i == 2:
            print("numberB:break")
            break
        print("numberB:%d"%i)

    # - continue - # 跳过本次(一层)循环, 作用范围: for / while (无作用:if)
    for i in range(5):
        if i == 2:
            print("numberC:continue")
            continue
        print("numberC:%d"%i)


# === 封装 ===
# - def 函数(方法) -
def method():
    print("method")



# ======= 函数调用 ======
if __name__ == "__main__":
    helloworld()
    explanatorynote()
    variable()
    typeconversion()
    inputoutput()
    judge()
    loop()
    control()
    method()
# ======= 函数调用 ======
