#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:04:14
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# 定义类
class Person:
    # 类属性 (class) (注:类/类方法 能修改类属性; 对象不能修改类属性,更改的只是实例属性)
    name = "name" # 公共属性
    __adress = "adress" # 私有属性 (__属性 表示私有)

    # 构造方法(对象创建调用) (__init__ 表示构造)
    def __init__(self, name, address = "地球"):
        # 实例属性
        self.name = name # (注:类属性与实例属性名称相同时用实例属性,实例属性被删除后使用类属性)
        self.__adress = address
        Person.setData(self)

    # 析构方法(对象销毁调用) (__del__ 表示析构)
    def __del__(self):
        print("对象被销毁.")

    # toString()
    def __str__(self):
        return "Person.class"

    # 实例方法 (this)
    def setName(self, name): # self可为其他字符串 (this)
        self.name = name; # 修改 实例属性 (不存在自动添加)

    # 类方法 (static)
    @classmethod
    def setName_cls(cls, name):
        cls.name = name  # 修改 类属性

    # 静态方法 (tools)
    @staticmethod
    def setName_sta(name): # (注:参数部分)
        return name

    def getName(self):
        return self.name

    def setData(self):
        # 实例属性
        self.__age = 21 # 私有属性
        self.sex = "女" # 公共属性

    def show(self):
        print("Hello! %s"%self.name)
        print("Address:%s"%self.__adress) # 使用自身私有属性
        self.__eat() # 使用自身私有方法

    def __eat(self): # 私有方法
        print("eat")



# ======= 函数调用 ======
if __name__ == "__main__":
    # - 创建对象 -
    ps = Person("LY")

    # --- 调用方法 ---
    # 调用实例方法
    ps.setName("LY") # 实例调用 实例方法
    ps.show()

    # 调用类方法
    Person.setName_cls("Person") # 类调用 类方法
    ps.setName_cls("Person") # 实例调用 类方法

    # 调用静态方法 ()
    print(ps.setName_sta("Per")) # 实例调用 静态方法
    print(Person.setName_sta("Per")) # 类调用 静态方法

    # --- 访问属性 ---
    print(ps.getName())
    print(ps.name) # 访问 类属性 的公共属性值
    print(ps.sex) # 访问 实例属性 的公共属性值

    # --- 修改属性 ---

    # 修改实例属性
    ps.name = "123" # 修改 类属性 (注:并非真修改,只是向对象中创建了一个实例属性)
    del ps.name # 删除 实例属性 (注:实例不能(非类方法)删除 类属性, 只是删除了对象中创建的实例属性,类属性依然存在)
    del ps.sex # 删除 实例属性 (注:真删除,删除后不能访问)

    # 修改类属性
    Person.name = "Person" # 修改类属性
    Person.setName_cls("Person") # 类 调用 类方法 修改 类属性 (注:类不能调用实例方法)
    ps.setName_cls("Person") # 对象 通过 类方法 修改 类属性
    del Person.name # 删除类属性

    # - 删除对象 -
    del ps
    # > Less is more! "静态方法"和"类方法/属性"同级都可理解为"静态",静态方法适合做工具箱,类方法/属性可认为在静态区,随手拿来即用,而实例则需要实例化才能使用. (--本人的个人理解)
# ======= 函数调用 ======

# --- 单继承 ---
# 父类
class Animal(object):

    def __init__(self, name = "动物"):
        self.name = name

    def run(self):
        print("%s在跑."%self.name)

# 子类
class Cat(Animal): # 继承 (父类写()内)

    def __init__(self, name, ot = ""):
        super(Cat, self).__init__(name)

    def miao(self):
        print("喵")



# --- 多继承 ---
class Donkey: # 驴
    def walk(self):
        print("walk")

    def eat(self):
        print("Donkey.eat")

class Horse: # 马
    def run(self):
        print("run")

    def eat(self):
        print("Horse.eat")

class Mule(Donkey, Horse): # 骡(驴+马)
    pass



# === 多态 ====
def animalRun(animal): # 参数接收自己及其自己的子类
    animal.run()




# ======= 函数调用 ======
if __name__ == "__main__":
    # - 单继承调用 -
    ani = Animal()
    ani.run()

    cat = Cat("猫")
    cat.run()
    cat.miao()


    # - 多继承调用 -
    mule = Mule()
    mule.walk()
    mule.run()
    mule.eat() # 多个父类中有相同的方法时,调用()内最前面的父类(Donkey)的方法


    # - 多态调用 -
    ani = Animal()
    animalRun(ani)

    cat = Cat("猫")
    animalRun(cat)
# ======= 函数调用 ======




#coding=utf-8
# class_rewrite.py 重写(新式类)

class Animal(object):

    def run(self):
        print("Animal.run")

    def eat(self, food = "食物"):
        print("eat:%s"%food)


class Cat(Animal):

    # 子类重写了父类的方法
    def run(self):
        print("Cat.run")

    def eat(self):
        # 调用父类的方法
        super(Cat, self).eat("猫粮")



# ======= 函数调用 ======
if __name__ == "__main__":
    ani = Animal()
    ani.run()
    ani.eat()
    cat = Cat()
    cat.run()
    cat.eat()
# ======= 函数调用 ======


# class_propertiemethod.py 属性方法
# 属性方法: 把方法变成静态属性


# 写法1
class PM_1(object):
    def __init__(self):
        self.__name_str = "PropertieMethod_1"

    # 获取
    @property
    def name(self):  # 注意,方法名相同
        return self.__name_str

    # 设置
    @name.setter
    def name(self, name):
        self.__name_str = name

    # 删除
    @name.deleter
    def name(self):
        del self.__name_str


if __name__ == "__main__":
    pm = PM_1()
    print(pm.name)
    pm.name = "PM"
    print(pm.name)
    del pm.name
    # print(pm.name)

# ==========================================================


# 写法2
class PM_2(object):
    def __init__(self):
        self.__name_str = "PropertieMethod_2"

    # 获取
    def getname(self):
        return self.__name_str

    # 设置
    def setname(self, name):
        self.__name_str = name

    # 删除
    def delname(self):
        del self.__name_str

    # property(fget=None, fset=None, fdel=None, doc=None) # 返回一个property 属性, 实现原理见 内置函数 文章 property_my 块代码(http://blog.csdn.net/rozol/article/details/70603230)
    name = property(getname, setname, delname)


if __name__ == "__main__":
    p = PM_2()
    print(p.name)
    p.name = "PM2"
    print(p.name)
    del p.name
    # print(p.name)


    # class_reflection.py 反射
# 通过反射机制,可动态修改程序运行时的状态/属性/方法
# Python的反射机制性能如何? 在Android中Java的反射产生垃圾而执行gc,从而导致UI不流畅,而且性能低
# Python的反射性能(1亿次测试): 直接获取属性值:反射获取属性值 = 1:1.164 ;直接设置属性值:反射设置属性值 = 1:1.754

def setname(self, name):
    self.name = name

class Clazz(object):
    def __init__(self):
        self.name = "Clazz"

    def getname(self):
        return self.name



if __name__ == "__main__":
    c = Clazz()

    # --- 方法 ---
    if hasattr(c, "getname"):
        # 获取
        method = getattr(c, "getname", None)
        if method:
            print("setname_ref: {}".format(method()))  # 获取方法对象并执行

    if not hasattr(c, "setname"):
        # 添加
        setattr(c, "setname", setname)  # 添加方法
        method = getattr(c, "setname", None)
        if method:
            method(c, "Reflection")
        print("setname_raw: {}".format(c.getname()))

    if hasattr(c, "setname"):
        # 删除
        delattr(c, "setname")
        # c.setname(c, "Demo")


    # --- 属性 ---
    if not hasattr(c, "age"):
        # 添加
        setattr(c, "age", 21)  # 添加方法
        var = getattr(c, "age", None)
        print("age_ref: {}".format(var))
        print("age_raw: {}".format(c.age))

    if hasattr(c, "age"):
        # 获取
        var = getattr(c, "age", None)
        print("age_ref: {}".format(var))

    if hasattr(c, "age"):
        # 删除
        delattr(c, "age")
        # print("age_raw: {}".format(c.age))


# class_doc.py 文档注释
# 文档注释的编写

class Foo(object):
    '''
    这是一个类
    '''

    def method(self, data):
        '''
        这是一个方法
        :param data: 需要的数据
        :return: 返回的数据
        '''
        return "method"


def func(data):
    '''
    这是一个函数
    :param data: 需要的数据
    :return: 返回的数据
    '''
    return "func"



if __name__ == "__main__":
    # 打印文档
    print(Foo.__doc__)
    print(Foo().method.__doc__)

    print(func.__doc__)




# class_origin.py 类的由来
# 类由type类实例化产生, 而type由解释器产生

age = 21

def __init__(self):
    self.name = "origin"

def getname(self):
    return self.name

def setname(self, name):
    self.name = name

def delname(self):
    del self.name


if __name__ == "__main__":
    # 用type创建类(类名, 基类元组, 类成员字典)
    Foo = type('Foo', (object,), {'__init__' : __init__, "getname" : getname, "setname" : setname,
                                  "delname": delname, "age" : age})
    # 实例化类
    f = Foo()
    # 使用
    print(f.age)
    print(f.getname())
    f.setname("ClassOrigin")
    print(f.getname())
    f.delname()
    # print(f.getname())

# ==================================================================================





# 元类 (type创建类原理)
# 元类是用于创建所有类的类, Python中是type类 (注意,类也是对象,也是被创建出来的,即万物皆对象), 下面将演示type类的功能

# __call__ 的调用 (__new__在__init__之前调用, __call__在什么时候调用呢)
class Foobar(object):
    def __call__(self, *args, **kwargs):
        print("Foobar __call__")

if __name__ == "__main__":
    fb = Foobar()
    fb()  # 只有在这个时候才会调用__call__属性

    Foobar()()  # 等同于该方式

# ------


# metaclass指定类有谁来创建
# Python创建类时会寻找__metaclass__属性,(包括父类)没有找到将使用内建元类type
class MyType(type):
    def __init__(self, *args, **kwargs):
        print("MyType __init__")

    def __call__(self, *args, **kwargs):
        print("MyType __call__")
        obj = self.__new__(self)
        self.__init__(obj, *args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("MyType __new__")
        return type.__new__(cls, *args, **kwargs)


class Foo(object, metaclass=MyType):  # (Python3.x写法) metaclass 用于创建类, Python创建类时会寻找__metaclass__属性,(包括父类)没有找到将使用内建元类type

    # __metaclass__ = MyType # Python2.x写法

    def __init__(self):
        print("Foo __init__")

    def __new__(cls, *args, **kwargs):  # 用于实例化对象
        print("Foo __new__")
        return object.__new__(cls)  # 必须是返回

    def show(self):
        print("Foo show")


if __name__ == "__main__":
    print("start")
    f = Foo()
    f.show()
    # MyType __new__ => MyType __init__ => 'start' => MyType __call__ => Foo __new__ => Foo __init__ => 'Foo show'


# class_other.py 关于类的一些补充


class Demo(object):
    def show(self):
        print("Demo show")

if __name__ == "__main__":
    # __module__ 该对象的模块名
    # __class__ 该对象的类对象
    print(Demo.__module__)  # 该对象的模块名 => __main__
    print(Demo.__class__)  # 该对象的类对象 => <class 'type'>

    obj = Demo()
    print(obj.__module__)  # 该对象的模块名 => __main__
    print(obj.__class__)  # 该对象的类对象 => <class '__main__.Demo'>
    obj.__class__.show(obj)  # 类对象可被使用

    # ============================

    # __dict__ 类或对象中的所有成员
    print(Demo.__dict__)  # 类属性
    print(obj.__dict__)  # 实例属性    