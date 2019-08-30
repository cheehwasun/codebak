#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-15 13:51:18
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

import requests
import os
import random
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


	#静态网页
def getHtml(url, params=None, headers=None, proxies=None, timeout=None):
	try:
		r=requests.get(url, params=params, headers=headers,proxies=proxies, timeout=timeout)
		r.encoding=r.apparent_encoding
		html=r.text
		return html
	except Exception as e:
		print(e)
		return '网络异常'


url='https://www.bilibili.com/video/av11134689/'
r=getHtml(url)
bs=BeautifulSoup(r,'lxml')
l_path=[]
for each in bs.select('.v-plist #plist option'):
	l_path.append(each.attrs['value'])

print(l_path)
	

