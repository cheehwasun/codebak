#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:20:48
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# json_demo.py json格式的数据
# 解析和创建json数据
# 编码: 默认编码为"ascii", 中文(非ASCII字符)将被转义

import json


class Person:
    def __init__(self):
        self.name = "luzhuo"
        self.age = 23
        self.lists = [4, 5, 6, "中文"]

data = {"dicts": None, "class": None}
dicts = {"name": "luzhuo", "age": 21, "lists": [1, 2, 3, "中文"]}


def json_encode():
    '''
    编码
    '''

    # 编码字典
    data_dicts = json.dumps(dicts, indent=4)
    print(data_dicts)
    data["dicts"] = data_dicts

    # 编码类
    data_class = json.dumps(Person(), indent=4, default=lambda obj: obj.__dict__)
    print(data_class)
    data["class"] = data_class


def json_decode():
    '''
    解码
    '''

    # 解码字典
    dicts = json.loads(data["dicts"])
    print(dicts)

    # 解码类(实际上是被解析成了字典)
    clazz = json.loads(data["class"])
    print(clazz)



def json_func():
    # 将obj序列转为fp, skipkeys:是否跳过非Python基本类型的数据, ensure_ascii:是否将非ASCII字符转义, check_circular:是否进行容器循环引用检查, indent:格式化None/int, default:def default(obj):为不能为序列化的函数调用, sort_keys:是否按键排序
    # json.dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
    json.dump(dicts, open("file.txt", "w"))
    # 将obj序列转为json格式的str
    # json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
    data_str = json.dumps(dicts)

    # 从fp反序列化为python对象
    # json.load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    data_dict = json.load(open("file.txt"))
    # 从str反序列化为python对象
    # json.loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    data_dict = json.loads(data_str)

    # Json解码器
    # class json.JSONDecoder(object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)
    jsondecoder = json.JSONDecoder()

    data_dict = jsondecoder.decode("")  # 解码字符串json文档
    data_dict = jsondecoder.raw_decode("")  # 解码字符串json文档, 返回(Python形式, 原始json文档的字节数)

    # Json编码器
    # class json.JSONEncoder(skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)
    jsonencode = json.JSONEncoder()

    # jsonencode.default(o)  # 返回可序列化对象, 在子类中重写并实现
    jsonencode.encode(dicts)  # 编码, 字符串形式
    jsonencode.iterencode(dicts)  # 编码, 可迭代对象


if __name__ == "__main__":
    json_encode()
    json_decode()

    # json_func()

# xml_demo.py xml格式的数据
# 解析和创建xml数据
# 传统的接口传的数据还是xml
# 这里只讲ElementTree, 其他两种方式再说...-.-!

# 解析XML文件有三种方式:
    # 1. SAX: 适合读取大文件,数据流形式读取,速度快,内存占用少,通过回调函数返回数据
    # 2. DOM: 适合读取小文件,数据映射到内存中的树,速度慢,耗内存
    # 3. ElementTree: 默认适合小文件, 递增解析方式适合大中文件,数据生成元素树,速度快,内存占用少

data = '''<?xml version='1.0' encoding='utf-8'?>
        <data>
            <student name="liuyan">
                <age>21</age>
            </student>
            <student name="tanwei">
                <age>22</age>
            </student>
        </data>
        '''

import xml.etree.ElementTree as et

path = "xml.xml"  # xml里的数据与data相同
def et_encode():
    '''
    编码为xml数据
    '''

    # 创建
    root = et.Element("data")  # 根元素
    name = et.SubElement(root, "name", attrib={"show": "yes"})  # 子元素
    age = et.SubElement(name, "age")
    age.text = '21'

    et_ = et.ElementTree(root)  # 生成xml
    et_.write("new.xml", encoding="utf-8", xml_declaration=True)
    et.dump(root)  # 写入文件



def et_decode():
    '''
    xml数据解码
    '''

    tree = et.parse(path)
    root = tree.getroot()  # 获取根元素
    # 遍历xml文档
    for child in root:  # 第二层
        print(child.tag, child.attrib, child.text) # tag:元素名 attrib:属性{key:value} text:内容
        for i in child:  # 第三层
            print(i.tag, i.attrib, i.text)

    # 遍历所有age元素
    for node in root.iter("age"):
        print(node.tag, node.text)

    # 修改元素
    for node in root.iter("age"):
        new_year = int(node.text) + 1
        node.text = str(new_year)  # 修改值
        node.set("updated", "age")  # 添加属性
    tree.write(path, encoding="utf-8", xml_declaration=True)

    # 删除元素
    for student in root.findall("student"):  # findall()定位元素可使用XPath表达式
        age = int(student.find("age").text)
        if age > 22:
            root.remove(student)  # 删除元素
    tree.write(path, encoding="utf-8", xml_declaration=True)


def et_func():
    '''
    ElementTree
    '''
    # 创建
    # xml.etree.ElementTree.parse(source, parser=None)  // xml解析到元素树中, source:文件名 / file-obj
    tree = et.parse(path)

    # xml.etree.ElementTree.SubElement(parent, tag, attrib={}, **extra) // 穿件元素实例, parent:父元素, tag:子元素名称, attrib:{attr:value}, extra:其他关键字属性
    elem = et.SubElement(elem, "name", attrib={"show": "yes"})
    # xml.etree.ElementTree.fromstring(text) // 从字符换解析xml, 返回Element实例
    elem = et.fromstring(data)
    # xml.etree.ElementTree.fromstringlist(sequence, parser=None) // 同fromstring
    elem = et.fromstringlist(data)
    # xml.etree.ElementTree.XML(text, parser=None) // 同fromstring
    elem = et.XML(data)
    # xml.etree.ElementTree.XMLID(text, parser=None) // 从字符串中解析xml, 并返回(元素, 字典)
    elem, dicts = et.XMLID(data)
    # xml.etree.ElementTree.Comment(text=None) // 注释元素, text:注释内容(bytes / Unicode字符串), XMLParser跳过注释,ElementTree只包含注释结点
    elem = et.Comment(r"注释")
    # xml.etree.ElementTree.ProcessingInstruction(target, text=None) // PI元素, target:PI目标字符串, text:PI内容字符串, 返回元素实例, XMLParser跳过该元素, ElementTree只包含节点
    # xml.etree.ElementTree.register_namespace(prefix, uri) // 注册命名空间前缀, prefix:前缀, uri:命名空间
    et.register_namespace("web", "http://luzhuo.me")

    # xml递增的方式解析到元素树中(适合大文件), source:文件名/file-obj, events:要报告的事件("start", "end"(默认), "start-ns", "end-ns), parser:可选的解析器(XMLParser的子类)
    # xml.etree.ElementTree.iterparse(source, events=None)
    events, elem = et.iterparse(path)

    # xml.etree.ElementTree.dump(elem) // 将元素树写成普通的xml文件
    et.dump(elem)
    # xml字符串表示形式, method:"xml"(默认)."html"."text"
    # xml.etree.ElementTree.tostring(element, encoding="us-ascii", method="xml", *, short_empty_elements=True)
    strs = et.tostring(elem, encoding="utf-8")
    # xml.etree.ElementTree.tostringlist(element, encoding="us-ascii", method="xml", *, short_empty_elements=True) // 同tostring
    strs = et.tostringlist(elem)

    boolean = et.iselement(elem)  # 是否是元素对象


    # --- Element 对象 ---
    # class xml.etree.ElementTree.Element(tag, attrib={}, ** extra) // 元素类, tag:bytes/Unicode字符串, attrib:{attr:value}

    elem.tag  # 元素名
    elem.text  # 元素内容(标签的内容<a>text</a>)
    elem.tail  # 元素内容(标签之后的内容</a>text)
    dicts = elem.attrib  # 属性字典
    elem.clear()  # 删除所有元素,属性
    elem.get("age", default=None)  # 获取属性的值
    key, value = elem.items()  # 元素属性列表(key, value)返回
    elem.keys()  # 元素的属性列表
    elem.set(key, value)  # 设置元素的属性
    elem.append(elem)  # 添加元素到末尾(直接下级)
    # elem.extend(elem)  # 添加元素到末尾, 源码是调用_children列表.extentd()方式添加元素,不知为何.append()有用,而extentd()无效果
    # find(match, namespaces=None) // 匹配(直接下级)第一个子元素, match:元素名 / XPath, namespaces:命名空间
    elem = elem.find("root")
    # findall(match, namespaces=None) // 匹配(直接下级)所有子元素, match:元素名 / XPath
    elems = elem.findall("root")
    # findtext(match, default=None, namespaces=None) // 匹配(直接下级)第一个子元素的文本
    texts = elem.findtext("root")
    elem.insert(1, elem)  # 插入子元素, index:位置, subelement:子元素
    # iter(tag=None)  # 指定(所有下级)元素名的迭代器(深度优先)
    elem.iter("root")
    elem.iterfind("root")  # 匹配(直接下级)所有子元素, 返回迭代器
    elem.itertext()  # 文本迭代器(所有下级)
    elem.remove(elem)  # 删除子元素


    # --- ElementTree 对象 ---
    # ElementTree包装类, 表示整个元素的层次结构, element:根元素, file:如果给定,将生成初始化树
    # class xml.etree.ElementTree.ElementTree(element=None, file=None)
    et_ = et.ElementTree(elem)
    # parse(source, parser=None) // 解析xml到元素树, source:文件名 / file-obj
    et_ = et_.parse(path)

    et_.getroot()  # 获取根元素
    et_.__setroot(elem)  # 替换根元素
    et_._find("root", namespaces=None)  # 同Element.find()
    et_._findall("root", namespaces=None)  #同Element.findall()
    et_._findtext("root", default=None, namespaces=None)  # Element.findtext()

    et_.iter(tag=None)  # Element.iter()
    # iterfind(match, namespaces=None) // Element.iterfind()
    et_.iterfind("root")

    # 将元素树写入文件, file:文件名/file-obj, xml_declaration:是否显示声明信息, default_namespace:命名空间("xmlns"), method:"xml"(默认)/"html"/"text", short_empty_elements:是否自闭标签(默认True)
    # write(file, encoding="us-ascii", xml_declaration=None, default_namespace=None, method="xml", *, short_empty_elements=True)
    et_.write("new.xml", encoding="utf-8", xml_declaration=True)


    # 异常
    # class xml.etree.ElementTree.ParseError
        # code # 错误吗
        # position # 行列



# XPath表达式
# tag   标签名的所有子元素
# *     所有子元素
# .     选择当前节点(相对路径)
# //    该级别下的所有元素
# ..    父元素
# [@attrib='value'] 具有指定属性的所有元素
# [tag] 标签名的直接子元素
# [tag='text']  该级别下为标签名的所有元素
# [position]    指定位置的元素[1, last()-1]

# 案例:
# root.findall("./student")  # root元素下的所有student元素
# root.findall(".//student[@name='liuyan']")  # student下所有name属性为liuyan的元素
# root.findall(".//*[@name='liuyan']/age")  # root元素下的所有name属性为liuyan的元素下的 age元素
# root.findall(".//student[2]")  # 所有student元素的第二个元素


if __name__ == "__main__":
    et_encode()
    et_decode()

    # et_func()



# base64_demo.py 将二进制数据编码为可打印ASCII字符,并且可解码为二进制
# 支持: base16 base32 base64 base85
# 可作用文本 / URL / HTTP POST
# 现代接口: 支持 字节(bytes-like object) 的 编码 和 解码
# 传统接口: 支持 文件对象 的 编码 和 解码


import base64


def base64_demo():
    # 使用Base64编码/解码
    bytes = base64.b64encode(b'luzhuo.me')
    print(bytes)

    bytes = base64.b64decode(bytes)
    print(bytes)

    # 对文件的内容进行编码
    base64.encode(open("file.txt", "rb"), open("base.txt", "wb"))



def base54_func():
    # 现代接口
    # base64.b64encode(s, altchars=None) // Base64编码
    bytes = base64.b64encode(b'luzhuo.me')
    # base64.b64decode(s, altchars=None, validate=False)  // Base64解码, validate:True(非字母字符抛binascii.Error), False(非字母字符丢弃)
    bytes = base64.b64decode(bytes)
    # base64.standard_b64encode(s) // 标准的Base64字母表编码(同b64encode)
    bytes = base64.standard_b64encode(b'luzhuo.me')
    # base64.standard_b64decode(s) // 标准的Base64字母表解码(同b64decode)
    bytes = base64.standard_b64decode(bytes)
    # base64.urlsafe_b64encode(s) // 使用URL和文件系统安全的字母表编码
    bytes = base64.urlsafe_b64encode(b'luzhuo.me')
    # base64.urlsafe_b64decode(s) // 使用URL和文件系统安全的字母表解码
    bytes = base64.urlsafe_b64decode(bytes)
    # base64.b32encode(s) // Base32编码
    bytes = base64.b32encode(b'luzhuo.me')
    # base64.b32decode(s, casefold=False, map01=None) // Base32解码
    bytes = base64.b32decode(bytes)
    # base64.b16encode(s) // 使用Base16编码
    bytes = base64.b16encode(b'luzhuo.me')
    # base64.b16decode(s, casefold=False) // Base16解码
    bytes = base64.b16decode(bytes)
    # base64.a85encode(b, *, foldspaces=False, wrapcol=0, pad=False, adobe=False) // Ascii85编码
    bytes = base64.a85encode(b'luzhuo.me')
    # base64.a85decode(b, *, foldspaces=False, adobe=False, ignorechars=b' \t\n\r\v') // Ascii85解码
    bytes = base64.a85encode(bytes)
    # base64.b85encode(b, pad=False) // base85编码
    bytes = base64.b85encode(b'luzhuo.me')
    # base64.b85decode(b) // base85解码
    bytes = base64.b85decode(bytes)

    # 传统接口
    # base64.encode(input, output) // 编码, input从文件读取二进制数据, output写入文件 (每76个字节后 和 末尾 插入b'\n')
    base64.encode(open("file.txt", "rb"), open("base.txt", "wb"))
    # base64.decode(input, output) // 解码
    base64.decode(open("base.txt", "rb"), open("file.txt", "wb"))
    bytes = base64.encodebytes(b'luzhuo.me')  # 编码 (每76个字节后 和 末尾 插入b'\n')
    bytes = base64.decodebytes(bytes)  # 解码




if __name__ == "__main__":
    base64_demo()

    # base54_func()
        
