#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-31 01:18:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from xml.dom.minidom import Document

class VlcList:
	"""docstring for VlcList"""
	def __init__(self, *args):
		self.arg = args
		#在内存中创建一个空的文档
		self.doc=Document()		
		self.file='1.xspf'
		self.initDoc()


	#初始化xml容器doc
	def initDoc(self):

		#创建一个根节点companys对象
		root=self.doc.createElement('playlist')
		#给根节点添加属性
		root.setAttribute('xmlns','http://xspf.org/ns/0/')
		root.setAttribute('xmlns:vlc','http://www.videolan.org/vlc/playlist/ns/0/')
		root.setAttribute('version','1')
		#将根节点添加到文档对象中
		self.doc.appendChild(root)

		#给根节点添加一个叶子节点
		title=self.doc.createElement('title')
		root.appendChild(title)
		title.appendChild(self.doc.createTextNode('播放列表'))

		#给根节点添加一个叶子节点
		tracklist=self.doc.createElement('trackList')
		root.appendChild(tracklist)

		extension2=self.doc.createElement('extension')

		#批量添加
		for i in range(15):	
			url=self.arg[0]+str(i+1)+self.arg[1]
			titlecontent='cctv'+str(i+1)		
			track=self.doc.createElement('track')
			tracklist.appendChild(track)

			location=self.doc.createElement('location')
			track.appendChild(location)
			location.appendChild(self.doc.createTextNode(url))

			title2=self.doc.createElement('title')
			track.appendChild(title2)
			title2.appendChild(self.doc.createTextNode(titlecontent))

			extension=self.doc.createElement('extension')
			track.appendChild(extension)
			extension.setAttribute('application','http://www.videolan.org/vlc/playlist/0')

			vlc_id=self.doc.createElement('vlc:id')
			vlc_option=self.doc.createElement('vlc:option')

			extension.appendChild(vlc_id)
			extension.appendChild(vlc_option)

			vlc_id.appendChild(self.doc.createTextNode(str(i)))
			vlc_option.appendChild(self.doc.createTextNode('network-caching=1000'))

	#写入文件
	def makeXml(self):
		with open(self.file,'a+',encoding='utf-8') as f:
			self.doc.writexml(f,indent='\t', newl='\n', addindent='\t', encoding='utf-8')

if __name__ == '__main__':
	vlc=VlcList('http://cctvcnch5c.v.wscdns.com/live/cctv','_2/index.m3u8')
	vlc.makeXml()


