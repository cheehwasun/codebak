#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:00:19
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# 列表[有序可变序列]
def lists():
    # --- 列表 ---
    # 列表可通过 append() / pop() 方法,作为栈使用
    # 列表可通过 deque() 封装,作为双向队列使用
    # 创建
    lists = ["a", "b", "c"] # 列表
    lists = list() # 空列表
    lists = list((1, 2, 3)) # (将 元组 转为列表 (注:将字典转为列表会损失数据)
    lists = [i for i in range(10)] # 其他:[(10,i) for i in range(10)]

    # 统计
    length = len(lists) # 列表长度
    count = lists.count("c") # 统计该元素数量

    # 获取
    str0 = lists[0] # 取出列表中的数据
    lists = lists[0:3]
    lists = lists[0:3:2]
    ary2 = lists.copy() # 浅拷贝列表

    # 查找
    index = lists.index("b") # 查询该元素的位置, 不存在抛异常(注意)
    index = lists.index("b", 1)  # 从 1-末尾
    index = lists.index("b", 0, 2) # 从 0-2 (起始索引不能越界)
    elem = min(lists)
    elem = max(lists)

    # 遍历
    for i in lists:
        print("for:%s"%i)

    # 修改
    lists[0] = "0" # 修改第一个数据
    lists.reverse() # 倒序
    lists.sort() # (自然顺序)排序

    # 添加
    lists.append("d") # 添加数据(加到末尾)
    lists.insert(1, "a1") # 插入数据
    lists.extend(["d", "e", "f"]) # 添加数据(元素追加到末尾)
    lists = [1, 2] + [3, 4] # 合并列表
    lists = [1, 2] * 3 # 添加元素到自身3次


    # 删除
    del lists[1] # 根据索引删除(注意)
    lists.pop() # 删除最后元素
    lists.remove("aa") # 根据元素删除, 找不到则抛一行
    lists.clear() # 清空列表

    # 判断
    boolean = "a" in lists # 该元素是否存在于列表中
    boolean = "a" not in lists # 该元素是否不存在于列表中

    # 排序
    lists = sorted(lists)



# 字典(无序可变的映射类型,键值对集合,且键唯一)
def dics():
    # --- 字典 ----
    # 创建(由 键值对(key:value) 组成)
    dics = {1:"a", 2:"b", 3:"c"}
    dics = dict() # 创建空字典
    dics = dict([(1, "a"), (2, "b")]) # (序列)转为字典 (列表序列: dict([[1, "a"], [2, "b"]]); 元组列表: dict(((1, "a"), (2, "b"))))
    dics = dict(a = 1, b = 2) # (注: 格式固定, 字母 = 数字, 字母不能加"号) # => {'a': 1, 'b': 2}
    dics = {i for i in range(10)} # 其他:{(10,i) for i in range(10)} 
    dics = {chr(x) : x for x in range(65, 80)}

    # 获取
    strs = dics[1] # 按key取value, 没有对应key时抛异常(注意)
    strs = dics.get(1) # 按key获取value
    strs = dics.get(5, -1) # -1 为没有该key的返回
    strs = dics.setdefault(1) # 按key取value, key不存在则添加,value为None
    strs = dics.setdefault(12, -1) # -1为不存在key时,添加的value为-1
    keys = dics.keys() # 所有key
    values = dics.values() # 所有value
    kevaList = dics.items() # 获取(key,value)列表,格式为[(key1, value1), (key2, value2)]
    dics2 = dics.copy() # 浅拷贝
    dics3 = dics.fromkeys(dics) # 根据字典所有key创建新字典,value为None
    dics4 = dics.fromkeys(dics, -1) # -1为创建的新字典,value为-1

    # 查找
    key = min(dics) # 最小键
    key = max(dics) # 最大键

    # 遍历
    for key,value in dics.items():
        print("key:%d value:%s"%(key, value))

    # 添加
    dics.update({4:"d", 5:"f"}) # 添加字典

    # 修改
    dics[1] = "c"

    # 删除
    del dics[1] # 删除 键1 (注意)
    dics.clear() # 清空
    strs = dics.pop(1) # 删除,返回被删的元素(注意:同key同时删)
    strs = dics.pop(5, -1) # -1 为没有该key时的返回
    pul = dics.popitem() # 删除键值对,返回被删的元组(末尾起删)

    # 统计
    length = len(dics) # 字典长度

    # 判断
    boolean = 1 in dics # 该key是否在字典中存在
    boolean = 1 not in dics # 该key是否不在字典中存在

    # 排序
    lists = sorted(dics) # 注:返回排序后的键列表



# 元组[有序不变序列](不可修改)
def tuples():
    # --- 元组 ---
    # 创建 (类似于列表的数据存储方式,但是不能修改)
    tuples = ("柳岩", 21, "女")
    tuples = tuple(["a", "b", "c"]) # 将 列表 转为 元组 (注:将字典转为元组会损失数据)
    tuples = tuple() # 空元组,不知何用

    # × 添加 × 修改 × 删除 (注意:不许修改)

    # 获取
    strs = tuples[0] # 获取指定索引数据
    strs = tuples[-1] # 倒数获取数据 (1开始)
    tup4 = tuples[1:] # 截取
    tup5 = tuples[0:2]
    tup2 = tuples + (1, 2, 3) # 合并元组(原元组不变)
    tup3 = tuples * 3 # 复制(3份)合并元组
    strs = max((1, 3, 6, 2.5)) # 最大值
    strs = min((1, 3, 6, 2.5))

    # 统计
    length = len(tuples) # 元组长度
    count = tuples.count(21) # 该元素的数量

    # 查找
    index = tuples.index(21) # 该元素出现的索引,找不到抛异常
    index = tuples.index(21, 1) # 从 1-末尾
    index = tuples.index(211, 0, 2) # 从 0-2

    # 遍历
    for i in tuples:
        print("tuple:%s"%i)

    # 判断
    boolean = 21 in tuples
    boolean = 21 not in tuples



# Ranges[有序不变数字序列]
def ranges():
    # 创建
    ranges = range(10)
    ranges = range(1, 10)
    ranges = range(1, -10, -2) # (开始, 停止, 步骤)

    # 获取
    num = ranges.index(5)
    num = ranges[5]
    ranges = ranges[:5]
    ranges = ranges[1:5]
    ranges = ranges[1:5:2]

    # 判断
    boolean = 5 in ranges
    boolean = 5 not in ranges



# 字符串[有序不可变Unicode序列]
def strs():
    # === 创建字符串 ===
    strs = "Hello World!" # 字符串用 '/ " / ''' / """ 包裹
    strs = """可多行的字符串"""
    strs = str(123)
    strs = str({1, 2, 3}) # 将对象转为字符串
    strs = str(b'\xe4\xbd\xa0\xe5\xa5\xbd', "utf8") # bytes 转为字符串
    strs = r"原始字符串" # 原始字符串
    strs = u"Unicode字符串" # Unicode字符串

    # 截取字符串
    strs = strs[4] # 截取一个
    strs = strs[6:11]  # 截取 6-11 (0开始)
    strs = strs[6:] # 截取 6-末尾
    strs = strs[-6:] # 截取 倒数6-末尾 (倒数1开始)
    strs = strs.split("l") # 根据 关键词 分割字符串(返回列表)
    strs = strs.split("l", 2) # 2为限制分割次数
    strs = strs.partition("l") # 分割成三部分(前/l/后)
    strs = strs.rpartition("l")
    strs = "Hello\r\nWorld!".splitlines() # 按行分割

    # 查找
    index = strs.find("lo") # 查找 lo 字符串(首次)的索引, 未找到 -1
    index = strs.find("lo", 0, 10)
    index = strs.rfind("l") # 从右开始查找
    index = strs.rfind("l", 0, 10)
    index = strs.index("lo") # 查找 lo 字符串(首次)的索引, 未找到 抛异常
    index = strs.index("lo", 0, 10)
    index = strs.rindex("l") # 从右开始查找
    index = strs.rindex("l", 0, 10)
    index = strs.startswith("Hello") # 是否以该字符串开头
    index = strs.endswith("!")
    strs = min(strs)
    strs = max(strs)

    # 替换
    strs = strs.replace("l", "o")
    strs = strs.replace("l", "o", 2) # 2为限制替换次数

    # 遍历
    for i in strs:
        print("for:%s"%i)

    # 统计
    length = len(strs) # 字符串长度
    count = strs.count("l") # 统计 l 字符串出现的次数
    count = strs.count("l", 0, 10)

    # 转换
    strs = strs.capitalize() # 将首字符大写,其余全小写
    strs = strs.lower() # 所有字符转为小写
    strs = strs.casefold() # 同(lower)
    strs = strs.upper()
    strs = strs.swapcase() # 大小写字母取反
    bytes = strs.encode(encoding='utf-8', errors='strict') # 编码成("utf-8")bytes(同通过bytes.decode()解码)

    # 格式化
    strs = strs.ljust(20) # 左对齐, 20为补充长度(字符数不足20则自动补充空格至20)
    strs = strs.rjust(20)
    strs = strs.center(20)
    strs = strs.zfill(20) # 左边填充0到指定宽度
    strs = strs.lstrip() # 删除左边空格
    strs = strs.rstrip()
    strs = strs.title() # 标题 (每个单词首字母大写)
    strs = "-".join(strs) # 每个相邻字符中间插入关键词(注意:关键词调用该函数)
    strs.expandtabs() # 将"\t"用8位空格代替(注意:类似tab键的空格补充,而非直接将\t转为8位空格补充)
    strs = '{name},{age}'.format(age=21,name='柳岩') # 自动格式化 支持 '{age}'.format(age=21) / '{0[0]}'.format([21]) / '{person.age}'.format(person) / '{:b}'.format(21) / '{:,}'.format(123456789)
    strs = "6a6b6c6".translate(str.maketrans("abc", "123")) # 根据映射表格式化

    # 判断
    boolean = strs.isdigit() # 是否是(正整)数字(注意:是的关系,非包含的关系)
    boolean = strs.isnumeric() # 同(isdigit)
    boolean = strs.isalpha() # 是否是字母
    boolean = strs.isalnum() # 是否是字母和数字(可混合)
    boolean = strs.isspace() # 是否是空格
    boolean = strs.isupper() # 是否是大写字母(可含数字)
    boolean = strs.islower()
    boolean = strs.isdecimal() # 是否是十进制数
    boolean = strs.isidentifier() # 是否是合法标识符
    boolean = strs.isprintable() # 是否可打印(含转义符=false)
    boolean = strs.istitle() # 是否是标题 (单词首字母大写,空格分隔的视为标题)


# 二进制序列
def bytes():
    # === bytes 字节[有序不可变序列] ===
    # 创建
    bs = b'She, in my opinion, is pretty.' # ' / " / '''均可, 只允许ASCII字符

    # 转换
    bs = bytes.fromhex("4c 6f 76 65") # 16进制字符串(每个字节两个16进制数)转为bytes (无视空格,类方法)
    strs - bs.hex() # bytes转为16进制字符串


    # === bytearray[有序可变序列] ===
    # 创建
    barray = bytearray()
    barray = bytearray(10)
    barray = bytearray(range(10))
    barray = bytearray(bytes)

    # 转换
    barray = bytearray.fromhex("4c 6f 76 65") # 解析16进制字符串 (类方法)
    strs = barray.hex() # bytearray转为16进制字符串


    # --- bytes bytearray 共有的方法(可混合使用) ---
    # 混合使用例子
    b = b'abc'.replace(b'b', b'e')
    barray = bytearray(b'abc').replace(b'b', b'e')
    b = b'abc'.replace(bytearray(b'b'), bytearray(b'e'))

    # 转换
    strs = bs.decode(encoding='utf-8', errors='strict') # 解码 (error: strict(UnicodeError异常,默认) / ignore(忽略错误) / replace) (编码:strs.encode())

    # 其他方法与 str 方法相同,这里不再重复测试


    # === memoryview[内存视图](用于直接访问对象内部数据) ===
    # 创建
    mv = memoryview(bs) # 参数必须支持缓冲区的协议。(系统自带支持缓冲区协议: bytes / bytearray / array.array)

    # 获取
    byte = mv[1] # => 104
    byte = mv[-1]
    mv = mv[1]
    mv = mv[1:3]
    data = mv.obj # 被内存视图缓存的基础对象 (bs)
    length = mv.nbytes # 数组的大小 (已被使用的空间大小)
    length = mv.itemsize # 每个元素的大小
    length = mv.ndim # 数组维度
    tups = mv.shape # 数组大小生成元组 => (30,)
    tups = mv.strides # 每个元素大小生成元组 => (1,)

    # 判断
    boolean = mv.readonly # 内存是否只读
    boolean = mv.c_contiguous # 是否C连续
    boolean = mv.f_contiguous # 是否Fortran连续
    boolean = mv.contiguous # 是否连续 (C or Fortran 连续)
    boolean = 83 in mv
    boolean = 83 not in mv

    # 转换
    bytes(mv)
    bytes = mv.tobytes()
    strs = mv.hex() # 16进制
    lists = mv.tolist() # 转为list # => [83, 104, ... , 121, 46]

    # 遍历
    for i in mv:
        print(i)

    # 关闭
    mv.release() # 释放资源 (with自动释放)



from collections import deque
# 双向队列[有序序列] (封装list)
def deques():
    # 双向队列,线程安全,队列两端添加和弹出复杂度为O(1),效率很高
    # 创建
    lists = ["A", "B", "C", "D", "E"]
    queue = deque(lists)
    queue = deque(lists, 3) # 3为限制容器大小,队列满之后,先添加的元素将挤出另一端的旧元素; 未指定容器大小将是任意长度
    queue = deque(range(10))

    # 添加
    queue.append("F") # 添加到右边
    queue.appendleft("G") # 添加到左边
    queue.extend(range(3)) # 右边添加iterable元素
    queue.extendleft(range(3))
    queue.insert(1, "L")
    queue = queue + deque(range(3))
    queue = queue * 3

    # 获取
    queue = queue.copy() # 浅拷贝
    index = queue.index("A") # 获取索引,未找到抛ValueError异常
    index = queue.index("A", 1)
    index = queue.index("A", 7, 10)
    elem = max(queue)
    elem = min(queue)

    # 统计
    count = queue.count("A")

    # 删除
    elem = queue.pop() # 弹出右边元素
    elem = queue.popleft() # 弹出左边元素
    queue.clear() # 清空
    queue.remove("L")

    # 指针
    queue.rotate(-1) # 旋转指针 +元素后移 -元素前移

    # 其他
    queue.reverse() # 反转元素
    num = queue.maxlen # 指定的限制容量,未做限制返回None

    # 遍历
    for i in queue:
        print(i)

    # 判断
    boolean = "A" in queue
    boolean = "A" not in queue



# 集合(无重复元素的无序容器)
def sets():
    # 集合存放不同可哈希的对象,常用于删除重复项, 做交集 / 并集 / 差集 等数学运算
    # set可变, frozenset不可变,frozenset可存入set中(所以修改方法是set特有的)

    # --- set ---
    # 创建
    sets = set(range(10))
    sets1 = set('abcdefg')
    sets2 = set('acemnorsuvwxz')
    sets3 = set('bdfghijklpqty')

    # 获取
    sets = sets.copy() # 浅拷贝

    # 统计
    length = len(sets)

    # 数学运算
    sets = sets.union(set([9, 10, 11, 12, 13])) # 并集, 产生新集合 (新集合,元素来自于所有集合)
    sets = sets | set([9, 10, 11, 12, 13]) # 同union
    sets = sets.intersection(set([5, 6, 7])) # 交集,产生新集合 (新集合,元素来自所有集合共有的)
    sets = sets & set([5, 6, 7]) # 同intersection
    sets = sets.difference(set([5, 6, 7])) # 新集合,不含arg元素
    sets = sets - set([5, 6, 7]) # 同difference
    sets = sets.symmetric_difference(set([5, 6, 7, 13])) # 产生新集合, 元素来自两集合都不重复的元素
    sets = sets ^ set([5, 6, 7, 13]) # 同symmetric_difference

    # 遍历
    for i in sets1:
        print(i)

    # 判断
    boolean = 3 in sets
    boolean = 3 not in sets
    boolean = sets2.isdisjoint(sets3) # (元素不相交True) 该集合是否与arg集合的任何元素不相交
    boolean = set([1, 2]).issubset(sets) # (子集True) 是否是arg的子集(任何元素在arg中)
    boolean = set([1, 2]) <= sets # 同issubset
    boolean = set([1, 2]) < sets # (真子集True) sets <= arg and sets != arg
    boolean = sets.issuperset(set([1, 2])) # (父集True) 是否是arg的父集(arg任何元素在该集合中)
    boolean = sets >= set([1, 2]) # 同issuperset
    boolean = sets > set([1, 2]) # (真超集True) sets >= arg and sets != arg


    # --- frozenset ---
    # 创建
    fsets = frozenset(range(10))

    # 方法参考set (除set特有方法外)

    # set 和 frozenset 混合运算
    boolean = sets == fsets # 判断两集合任何元素是否相同
    boolean = sets >= fsets
    sets = sets1 | fsets


    # --- set特有方法(修改方法) ---
    # 添加
    sets.add("A")
    sets.add(frozenset([5, 6, 7])) # 集合中添加不可变集合

    # 修改
    sets.update(sets1) # 添加arg里的所有元素到该集合
    sets |= sets1 # 同updata
    sets.intersection_update(sets1) # 只保留arg的交集 (相同元素)
    sets &= sets1 # 同intersection_update
    sets.difference_update(sets1) # 取出arg的元素
    sets -= sets1
    sets.symmetric_difference_update(sets1) # 所有集合中非共有的元素
    sets ^= sets1

    # 删除
    sets.remove("A") # 不存在抛KeyErrory异常
    sets.discard("A") # 移除元素,不存在不抛异常,推荐使用
    elem = sets.pop() # 从左边弹出元素
    sets.clear()



import heapq
# 堆[二叉树结构,队列实现]
def heapqs():
    # 堆, 通过队列实现,而非链式实现, 左右结点查找通过 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2] 实现, 具体实现原理见 数据结构_树 文章
    # 该堆队列拥有优先级队列算法(排序), 主要操作最左边(最小)的元素
    lists = [3, 6, 8, 4, 5, 7, 9, 2, 4, 6, 5]
    lists1 = [(3, "A"), (6, "B"), (8, "C"), (4, "D"), (5, "E")]

    # 创建
    heapq.heapify(lists) # 带有优先级队列算法, 最小值在第一个 (注,只有先调用该方法,pop取出的值才准确)

    # 添加
    heapq.heappush(lists, 5) # 添加元素

    # 获取
    elem = lists[1]
    elem = heapq.heappop(lists) # 弹出第一项
    elem = heapq.heappushpop(lists, 6) # heappush + heappop
    elem = heapq.heapreplace(lists, 7) # heappop + heappush
    elem = max(lists)
    elem = min(lists)

    # 其他
    iterator = heapq.merge(lists, lists, key=None, reverse=False) # 合并, 返回迭代器



# ===== 函数调用 =====
if __name__ == "__main__":
    lists()
    dics()
    tuples()

    ranges()
    strs()
    bytes()
    deques()
    sets()
# ===== 函数调用 =====
