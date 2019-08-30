#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-15 15:30:19
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

import json
import pickle  # 导入模块。
data = {
    'name': "lixin",
    'sex': "female",
    'height': 1.58,
    'weight': 82,
    'utterance': '奏是这么瘦,来打我啊'
}
jsondata = json.dumps(data, indent=2)  # 转json数据
pythondata1 = json.loads(jsondata)  # json数据转python
print(pythondata1)
pickledate = pickle.dumps(data)  # 转持久化数据
pythondata2 = pickle.loads(pickledate)  # 转回python
print(pythondata2)


with open("jsondata.json", "w+") as file:  # 打开一个名为jsondata.json文本，只能写入状态 如果没有就创建
#注意这里是'w' 如果是wb中文会出错
    json.dump(data, file, ensure_ascii=False,indent=2,default=None)  # data转换为json数据格式并写入文件 ensure False 中文显示 indent缩进 default自己设置转换函数
    file.close()  # 关闭文件
with open("jsondata.json", "r") as file:  # 打开文本读取状态
    l = json.load(file)  # 解析读到的文本内容 转为python数据 以一个变量接收
    print(l)  # 打印变量
    file.close()  # 关闭文件

with open('5.pk', 'wb') as f:  # 'wb'注意要用二进制写入
    pickle.dump(data, f)
with open('5.pk', 'rb') as f:
    d3 = pickle.load(f)
    print(d3)
