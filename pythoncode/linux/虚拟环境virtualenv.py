#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-29 02:03:16
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$


pip install virtualenv  # py2安装
pip3 install virtualenv  # py3安装，这样用virtualenv创建的virtualenv默认python版本是py3

virtualenv ENV  # ENV 为环境的名字，可以任意设置，其实就是一个文件夹，在home下的用户名文件夹下可以找到。
# source ENV/bin/activate  # 这样进进入了virtualenv的虚拟开发环境。

# 输入命令行#

pip install virtualenvwrapper

# vi ~/.bashrc

# export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 # 这句是为了防止环境变量$PATH中已有其它环境的python
# export WORKON_HOME=$HOME/.virtualenvs    # 放所有虚拟环境的地方
# source /usr/local/bin/virtualenvwrapper.sh
#source /usr/bin/virtualenvwrapper.sh  #centos

mkvirtualenv env1

mkvirtualenv env2

列出已有环境

workon

退出环境

deactivate

删除环境

rmvirtualenv

创建project

    项目将创建到PROJECT_HOME目录下，实际上相当于在某个目录下，建了一个环境。

    mkproject
