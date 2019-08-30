#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20 15:59:23
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

# yum update 
# netstat -nplt
# ifconfig
# ps -A 查看进程
# users
# who 
# systemctl enable vsftpd.service 运行以下命令设置开机自启动。
# systemctl start vsftpd

# 一.建立ssh 
	# 1、先在主机A上创建密钥对
	# ssh-keygen -t rsa
	# 这时可以在主机A上看到生成的秘钥~/.ssh/id_rsa 和公钥 ~/.ssh/ id_rsa.pub


	# 2.把主机A的公钥放在主机B上
	# scp -r /root/.ssh/id_rsa.pub 192.168.31.147:/root/.ssh/authorized_keys
		
	# 	或者将公钥考到对方机器的用户目录下，并将其复制到~/.ssh/authorized_keys中（操作命令：
	# 	#cat id_rsa.pub >> ~/.ssh/authorized_keys）。

	# vi /etc/ssh/sshd_config
	# #Port 22         //这行去掉#号，防止配置不好以后不能远程登录，还得去机房修改，等修改以后的端口能使用以后在注释掉
	# Port 20000      //下面添加这一行

	#PermitRootLogin yes 允许root登陆

# 二。虚拟环境virtualenv

	# yum install python34
	# yum install python34-setuptools
	# easy_install-3.4 pip

	# pip3 install virtualenv
	# pip3 install virtualenvwrapper

	# vi ~/.bashrc

	# export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 # 这句是为了防止环境变量$PATH中已有其它环境的python
	# export WORKON_HOME=$HOME/.virtualenvs    # 放所有虚拟环境的地方

	#source /usr/bin/virtualenvwrapper.sh  #centos

	# mkvirtualenv env1

	# mkvirtualenv env2

	# 列出已有环境

	# workon

	# 退出环境

	# deactivate

	# 删除环境

	# rmvirtualenv



# 三。vsftpd
	# yum install -y vsftpd

	# firewall-cmd --permanent --zone=public --add-service=ftp
	# firewall-cmd --reload

	# 查看ftp的Selinux状态：
	# sestatus -b | grep ftp
	# 将状态改为on:		   
	# setsebool -P ftpd_full_access on

	# systemctl restart firewalld.service

	# 修改配置
	# cd /etc/vsftpd/
	# vi vsftpd.conf

	# listen=YES
	# #listen_ipv6=YES 注释掉

	# #去掉前面的注释
	# chroot_local_user=YES

	# ascii_upload_enable=YES
	# ascii_download_enable=YES

	# #文件末尾添加
	# allow_writeable_chroot=YES

	# 添加用户
	# useradd -d /home/ftp -s /bin/bash -s /sbin/nologin -m vsftp

	#自启动服务
	# systemctl enable vsftpd 

# 四。开发环境 django

# pip3 install Django==1.11