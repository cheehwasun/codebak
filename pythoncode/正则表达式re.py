#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:10:09
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

#coding=utf-8
# regular.py 正则表达式
import re # 正则模块

def regular():
    data = "She is more than pretty. 520"

    # --- 正则 ---
    reg = r"mo" # 指定字符 => span=(7, 9), match='mo'
    reg = r"." # (.)单个字符 => span=(0, 1), match='S'
    reg = r"\." # (\)转义符 => span=(23, 24), match='.'
    reg = r"[.]" # ([])字符集合(注意:部分特殊字符失去特殊意义) => span=(23, 24), match='.'
    reg = r"[love]" # []内任意字符 => span=(2, 3), match='e'
    reg = r"[i-u]" # (-)范围 => span=(4, 5), match='i'
    reg = r"t{2}" # {}内为长度(3个6) => span=(20, 22), match='tt'
    reg = r"t{1,3}" # {M,} / {.N} / {N} => span=(12, 13), match='t'
    reg = r"(i|o|u){1}" # (())组 => span=(4, 5), match='i'
    reg = r"^S" # (^)开头 => span=(0, 1), match='S'
    reg = r"[^S]" # ([^])取反(不含H) => span=(1, 2), match='h'
    reg = r"520$" # ($)结尾 => span=(25, 28), match='520'
    reg = r"et*" # (*)匹配{0,}个表达式 => ['e', 'e', 'ett']
    reg = r"et+" # (+)匹配{1,}个表达式 => ['ett']
    reg = r"et?" # (?)匹配{0,1}个表达式 => ['e', 'e', 'et']
    reg = r".+?e" # (?)非贪婪模式(span=(0, 20), match='She is more than pre' => span=(0, 3), match='She')

    reg = r"\145" # ascii标的8进制数(145=101=e) => span=(2, 3), match='e'
    reg = r"\d" # (\d)单个数字 => span=(25, 26), match='5' (推荐:[0-9])
    reg = r"\D" # (\D)非数字 => span=(0, 1), match='S' (推荐:[^0-9])
    reg = r"\s" # (\s)空白字符 => span=(3, 4), match=' ' (推荐:[\t\n\r\f\v])
    reg = r"\S" # (\S)非空白字符 => span=(0, 1), match='S' (推荐:[^\t\n\r\f\v])
    reg = r"\w" # (\w)单词 => span=(0, 1), match='S' (推荐:[a-zA-Z0-9_])
    reg = r"\W" # (\W)非单词 => span=(3, 4), match=' ' (推荐:[^a-zA-Z0-9_])
    reg = r"\AS" # (\A)开头 => span=(0, 1), match='S'
    reg = r"520\Z" # (\Z)结尾 => span=(25, 28), match='520'
    reg = r"y\b" # (\b)单词边界(Hello) => span=(22, 23), match='y'
    reg = r"o\B" # (\B)非单词边界(world) => span=(8, 9), match='o'
    reg = r"[01]\d\d|2[0-4]\d|25[0-5]" # 或(|) 多位数(匹配0 - 255 直接的数字)


    index = re.search(reg, data) # 查找单个匹配项
    index = re.match(r"She", data) # 匹配开头 => span=(0, 3), match='She'
    index = re.fullmatch(r".+", data) # 匹配全部 => span=(0, 28), match='She is more than pretty. 520'

    lists = re.findall(reg, data) # 查找所有匹配项(列表)
    lists = re.split(r"o", data, maxsplit=1) # 根据正则分割字符串(maxsplit分割次数) => ['She is m', 're than pretty. 520']

    strs = re.sub(r"\.", r"!", data, count=1) # 替换(count:替换次数)(匹配替换,未匹配原样) => She is more than pretty! 520

    re.purge() # 清除正则表达式缓存



    # --- 正则表达式对象 ---
    pat = re.compile(r"e") # 编译成正则对象

    index = pat.search(data) # 查找单个匹配项 => span=(2, 3), match='e'
    index = pat.search(data, 5) # => span=(10, 11), match='e'
    index = pat.search(data, 1, 10)
    index = pat.match(data) # 匹配开头 => None
    index = pat.match(data, 2) # => span=(2, 3), match='e'
    index = pat.match(data, 1, 10)
    index = pat.fullmatch(data) # 匹配全部 => None
    index = pat.fullmatch(data, 2) # => None
    index = pat.fullmatch(data, 2, 3) # span=(2, 3), match='e'

    lists = pat.split(data, maxsplit=0) # 分割 => ['Sh', ' is mor', ' than pr', 'tty. 520']
    lists = pat.findall(data) # 查找全部 => ['e', 'e', 'e']
    lists = pat.findall(data, 5) # => ['e', 'e']
    lists = pat.findall(data, 1, 10) # => ['e']

    strs = pat.sub(r"o", data, count=0) # 替换 => Sho is moro than protty. 520


    # --- Match ---
    match = index;
    # span=(2, 3), match='e'
    strs = match.string # 被匹配的数据 => She is more than pretty. 520
    strs = match.group() # 获取 match 数据 => e
    pos = match.pos # => 2
    pos = match.endpos # => 3



if __name__ == "__main__":
    regular()
