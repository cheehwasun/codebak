#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-15 13:51:18
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

import requests
import time
from bs4 import BeautifulSoup
from subprocess import Popen

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


def mkPath(url,cmd):
	# home='https://www.bilibili.com'
	r=getHtml(url)
	bs=BeautifulSoup(r,'lxml')	
	args=[]
	tags=bs.select('.v-plist #plist option')
	
	if not tags:
		args.append(cmd+url)
	else:
		cmd2=cmd+'https://www.bilibili.com'	
		for each in tags:
			a=cmd2+each.attrs['value']
			args.append(a)
	return args

def run(args):
	for arg in args:
		p=Popen(arg,shell=True)
		p.communicate()
		time.sleep(1)
	print(args)


if __name__ == '__main__':

	cmd='you-get -o d:\\bilibili -t 1 '	

	urls=['https://www.bilibili.com/video/av11134689/','https://www.bilibili.com/video/av8994940/','https://www.bilibili.com/video/av9005901/','https://www.bilibili.com/video/av9017598/','https://www.bilibili.com/video/av9034001/','https://www.bilibili.com/video/av10755879/','https://www.bilibili.com/video/av9076606/','https://www.bilibili.com/video/av9058217/']
	for url in urls:		
		args=mkPath(url,cmd)
		run(args)



