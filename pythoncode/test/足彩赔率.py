#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-18 17:10:08
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version :

from tkinter import *
import random

class myTk():
	def __init__(self,parent,sp,row=11,column=8):
		self.root=parent
		self.root.title("赔率变化")
		self.root.resizable(width=False, height=False)
		self.row=row
		self.sp=sp
		self.th=th
		self.column=column
		self._setTh()
		self._setTr()


	def _w(self,index):
		if index==0:
			return 10
		elif index<3:
			return 28
		else:
			return 16		

	def  _setTr(self):		
		for i in range(1,int(self.row)):
			self._setTh(i)

	def _setTh(self,index=0):
		self.var1=tuple([[]]*int(self.row))
		for j in range(self.column):
			w=self._w(j)
			a=StringVar()
			self.var1[index].append(a)

			Label(self.root,textvariable=self.var1[index][j], bg=self.sp[index%2],font=("微软雅黑", 12, "bold"),width = w,height = 2).grid(row=index+1,column=j+1,padx=2, sticky=W+E+N+S)

			if not index:
				self.var1[index][j].set(self.th[j])
			else:
				self.var1[index][j].set('')
	def setvar(self):
		self.var2=tuple([[]]*random.randint(1,5))
		for i in len(self.var2):
			for j in range(8):
				var2[i].append(str(j))

	def timer(self):
		for i in range(1,len(self.var2)+1):
			for j in range(self.column):
				self.var1[i][j].set(self.var2[i][j])
		self.root.update()
		self.root.after(500,self.timer)

if __name__ == '__main__':
	sp=['Bisque','Gray']
	th = ('场次','主队','客队','变化前','变化后','水位','比分','比赛时间')
	root = Tk()
	app = myTk(root,sp,th)
	# app.setvar()
	# app.timer()
	root.mainloop()





