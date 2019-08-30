#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-07 08:44:21
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

import sqlite3

class mydb(object):
	"""docstring for mydb"""
	def __init__(self, db):
		self.conn=sqlite3.connect(db)
		self.cursor=self.conn.cursor()
		try:
			self.cursor.execute('DROP TABLE files')
		except Exception as e:
			pass
		self.cursor.execute('create table files (path text primary key,size real,mtime real)')
		# self.conn.autocommit(False)
	def __del__(self):
		self.cursor.close()
		self.conn.close()
		print('del')

	def dbin(self,t):
		try:
			self.cursor.execute('insert into files values(?,?,?)',t)
			# self.conn.commit()
		except Exception as e:
			print(e)
			# self.conn.rollback()
	def dbdel(self,t):
		self.cursor.execute('delete from files where path=?',t)

	def dbup(self,t1,t2):
		self.cursor.execute('update files set size=? where path=?',(t1,t2)

			
