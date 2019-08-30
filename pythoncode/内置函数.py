#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:10:53
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# coding=utf-8
# builtin_function.py 内置函数
import os


def fun():
    all([True, False])  # 迭代器(为空or)所有元素为true,返回true => False
    any([True, False])  # 迭代器任意一个元素为true,返回true => True

    num = abs(-1.23)  # 绝对值
    num = pow(5, 3)  # 幂次方 x**y =>125
    num = pow(5, 3, 3)  # 幂次方再取余 (x**y) % z => 2
    num = round(1.23)  # 返回浮点数近似值,默认保留0位,且四舍五入
    num = round(1.23, 5)  # 5为保留小数点后位数
    num = sum([1, 2, 3, 4, 5])  # 对列表数字求和
    strs = ascii(os)  # 返回对象的ascii字符串形式
    strs = bin(123)  # 整数转为二进制字符串(若被转对象非int类型可在__index__里定义)
    # 获取真假(假:None / False / 任何类型的0 / 空""()[]{} / __bool__返回False / __len__返回0)
    boolean = bool(0)
    # 字符串(字符串,编码):按编码转为字节序列 / 数字(数字):生成相应大小的空数组 / 无参():0数组
    bytes = bytearray("You were, are and will be in my heart!", "utf-8")
    bytes = bytes("You were, are and will be in my heart!",
                  "utf-8")  # 同bytearray(),但是不可变
    strs = chr(123)  # 整数(Unicode)转为char类型(范围[0, 1 114 111])
    num = ord("{")  # char类型转为整数(Unicode)
    num = complex("1+2j")  # 将字符串或数字转为复数(不能含有空格)
    num = float('1.1')  # 构建浮点数
    strs = format(123, 'f')  # 格式化(类型:x,b,f... / 位移:>(>10),<,^ / 长度:5 / E)
    strs = hex(123)  # 将整数转为16进制字符串
    strs = oct(123)  # 十进制转成8进制字符串
    num = int(123.1)  # 转为整数
    strs = str(123)  # 将对象转为字符串
    strs = str(b"123", "utf-8")
    elem = max([1, 2, 3, 4], [2, 4, 6])  # 可接收1个iterable,或多个元素 => [2, 4, 6]
    elem = max(1, 2, 3, 4)  # => 4
    elem = max([1, 2, 3, 4, 6], key=lambda x: x == 2)  # => 2
    elem = min(1, 2, 3, 4)  # 与max相反

    # 编译为代码, mode(编译模式:可执行语句'exec',单个语句'eval',交互式语句'single')
    exe = compile("print('O_O')", filename='strs', mode='exec')
    exec(exe)  # 执行已编译代码
    exec("print('O_O')")  # 执行String未编译代码
    eval(compile("print('O_O')", filename='strs', mode='eval'))  # 不接受字符串类型

    # 删除某对象属性 = del clazz.name 详情见 类 文章的 反射 代码块(http://blog.csdn.net/rozol/article/details/69317339)
    delattr(Clazz("Hello!"), "name")
    setattr(Clazz("Hello!"), "name", "World!")  # 给对象某属性赋值
    strs = getattr(Clazz("Hello!"), "name")  # 获取某个对象的属性值
    strs = getattr(Clazz("Hello!"), "name", -1)  # -1为未找到属性的返回
    boolean = hasattr(Clazz("Hello!"), "name")  # 该对象是否有该属性
    lists = dir(Clazz("Hello!"))  # 查看函数
    clazz = type(os)  # 获取类型
    dicts = globals()  # 获取当前全局函数与对象
    dicts = locals()  # 获取当前局部函数与对象
    dicts = vars()  # 同locals() (__dict__)
    dicts = vars(Clazz("Hello!"))
    num = hash(Clazz("Hello!"))  # 获取某对象的hash值
    help(os)  # 获取某对象的帮助文档
    num = id(os)  # 获取某对象的id
    boolean = isinstance(Clazz("Hello!"), Clazz)  # 对象是否是该类的实例
    boolean = issubclass(Clazz, Clazz)  # 该类(前)是否是该类(后)的子类(包括自己)
    strs = repr(os)  # 将对象转为字符串表达形式
    # - super() # 代理父类对象,详情见 类 文章(http://blog.csdn.net/rozol/article/details/69317339)
    # - memoryview(obj) # 内存视图,详解 数据结构 文章(http://blog.csdn.net/rozol/article/details/68938984)

    dics = dict()  # 创建字典
    tups = divmod(10, 5)  # 返回元组,(商(10/5),余数(10%5))
    lists = enumerate(['a', 'b', 'c'])  # 返回枚举对象
    lists = filter(lambda x: True if (ord(x) > 66) else False,
                   ['a', 'b', 'c'])  # function为Frue保留,False移除
    sets = frozenset([1, 2, 3])  # 返回新的frozenset对象(集合)
    num = len([1, 2, 3])  # 长度
    lists = list((1, 'a'))  # 转为list类型
    tups = tuple([1, 2, 3])  # 转为tuple元组类型
    ran = range(5)  # 不可变序列
    ran = range(0, 5)
    ran = range(0, 5, 2)  # (起始,结束,增加量)
    sets = set([1, 2, 3])  # 返回set集合
    # 返回一个迭代器,元素通过自定义函数筛选,可接收多个iterable参数 => [65, 132, 201]
    maps = map(lambda x, y: x * y, [1, 2, 3], [65, 66, 67, 68])
    # 创建新的迭代器, 聚合每个迭代器元素 => [('A', 1), ('B', 2), ('C', 3)]
    iters = zip(["A", "B", "C", "D", "E", "F"], [1, 2, 3])
    iters = iter([1, 2, 3, 4, 5])  # 返回一个迭代器对象
    # 从迭代器中获取下个元素; 实现原理见 内置函数 文章 lis 块代码(http://blog.csdn.net/rozol/article/details/70769628)
    elem = next(iters)
    iters = reversed([1, 2, 3])  # 返回反向的遍历器 => [3, 2, 1]
    lists = [1, 2, 3, 4, 5][slice(3)]  # 切片 => [1, 2, 3]
    # [slice(3) == slice(None, 3, None) / slice(1,3) == slice(1, 3, None) / slice(1,3,1) == slice(1, 3, 1)
    lists = [1, 2, 3, 4, 5][slice(1, 3)]
    lists = sorted([2, 5, 3, 1, 4])  # 排序 => [1, 2, 3, 4, 5]
    lists = sorted(['a', 'B', ';', 't', 'D', '1'], key=lambda x: ord(
        x), reverse=True)  # key:比较键的函数, reverse是否反向遍历

    strs = input("请输入数据:")  # 输入数据
    f = open("temp.txt", "r+")  # 打开文件,详情见os文章
    print("字符串%d" % 123)  # 打印字符 => 字符串123
    print("字", "符", "串", sep="-")  # sep为分隔 => 字-符-串
    print("字", "符", "串", sep="-", end="\r\n")  # end为尾部 => 字-符-串/r/n
    print("字", "符", "串", sep="-", end="\r\n",
          file=open("temp.txt", "w+"))  # 打印到文件


class Clazz:
    def __init__(self, name):
        self.name = name

    @classmethod  # 将函数包装成类方法
    def setName_cls(cls, name):
        pass

    @staticmethod  # 将函数包装成静态方法
    def setName_sta(name):
        pass

    def getname(self):
        return self.name

    def setname(self, value):
        self.name = value

    def delname(self):
        del self.name

    # property(fget=None, fset=None, fdel=None, doc=None) # 返回一个property 属性, 实现原理见 内置函数 文章 property_my 块代码(http://blog.csdn.net/rozol/article/details/70603230)
    # property 为属性方法, 有两种实现方式,详情见 类 文章的 属性方法代码块(http://blog.csdn.net/rozol/article/details/69317339)
    x = property(getname, setname, delname)


if __name__ == "__main__":
    fun()

    # property 的使用
    c = Clazz("柳岩")
    print(c.x)  # => 柳岩
    c.x = '汤唯'
    print(c.getname())  # => 汤唯
    del c.x
