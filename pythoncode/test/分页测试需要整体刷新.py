#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-04 12:20:14
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

#django分页测试 需要刷新 不推荐 一般在js中实现
from django.utils.safestring import mark_safe
class Page():
	def __init__(self,current_page):
		self.current_page=int(current_page)
	@property
	def start(self):
		return (self.current_page-1)*10
	@property
	def end(self):
		return self.current_page*10

	def page_str(self,counts,base_url,tagid='page_test'):
		all_page,div1=divmod(counts,10)
		if 0<div1:
			all_page +=1

		page_str=[]
		# 页数小于11不动
		if all_page<=11:
			lo=1
			hi=all_page
		else:
			# 当前页数小于6不动防止负数
			if self.current_page<=6:
				lo=1
				hi=11
			elif self.current_page<(all_page-6):				
				lo=self.current_page - 5
				hi=self.current_page + 6
			#不大于总数
			else:
				lo=all_page-11
				hi=all_page+1
		#动态生成10个分页按钮
		for i in range(lo,hi):
			if i==self.current_page:				
				tmp='<a style="color:red;font-size:26px;padding: 10px" href="%s%d/" id="%s">%d</a>'%(base_url,i,tagid,i)
			else:
				tmp='<a style="padding: 10px" href="%s%d/" id="%s">%d</a>'%(base_url,i,tagid,i)	
			page_str.append(tmp)

		# 上下页
		if self.current_page<=1:
			pre_page = '<a href="javascript:void(0);">上一页</a>'          
		else:			
			pre_page='<a href="%s%d">上一页</a>' % (base_url, self.current_page - 1)

		if all_page<=self.current_page:
			next_page='<a href="javascript:void(0);">下一页</a>'
		else:
			next_page = '<a href="%s%d">下一页</a>' % (base_url, self.current_page + 1)

		page_str.insert(0,pre_page)
		page_str.append(next_page)
		# 标记安全 xss
		return mark_safe("".join(page_str))

