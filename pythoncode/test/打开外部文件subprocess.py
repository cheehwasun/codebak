import sublime
import sublime_plugin
import os
from subprocess import Popen, PIPE

class Git(object):
	"""docstring for Git"""
	def __init__(self):
		settings = sublime.load_settings("Example.sublime-settings")
		self.path=settings.get('path')
		self.log=[]

	def cmd(self,args):
		p=Popen(args=args,shell=True,stdout=PIPE)	
		self.log.append(p.stdout.read().decode('utf-8'))
		p.communicate()	

	def phase(self,args):
		os.chdir(self.path)
		for arg in args:
			self.cmd(arg)


	def gitpush(self,origin='origin',branch='dev'):
		args=['git status','git add .','git commit -m "auto"','git push %s %s'%(origin,branch)]
		self.phase(args)	
	

	
	# def __getattr__(self,item):



