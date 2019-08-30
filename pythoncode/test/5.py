#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-15 13:51:18
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

import requests
import os 
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def getHtml(url, params=None, headers=None, proxies=None, timeout=None):
	try:
		r=request.get(url, params=params, headers=headers,proxies=proxies, timeout=timeout)
		# r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except Exception as e:
		return '网络异常'

url='https://www.baidu.com'
t=getHtml(url)
print(t)
# bs=BeautifulSoup(t)

