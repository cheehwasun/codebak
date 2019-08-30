#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-23 23:21:08
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

# ssh 操作

# 1、先在主机A上创建密钥对
# ssh-keygen -t rsa
# 这时可以在主机A上看到生成的秘钥~/.ssh/id_rsa 和公钥 ~/.ssh/ id_rsa.pub


# 2.把主机A的公钥放在主机B上
# scp -r /root/.ssh/id_rsa.pub 192.168.31.147:/root/.ssh/authorized_keys
	
# 	或者将公钥考到对方机器的用户目录下，并将其复制到~/.ssh/authorized_keys中（操作命令：
# 	#cat id_rsa.pub >> ~/.ssh/authorized_keys）。




# sha登陆
# cat id_rsa.pub >> ~/.ssh/authorized_keys
# 设置authorized_keys权限
# $ sudo chmod 600 authorized_keys 
# 设置.ssh目录权限
# $ sudo chmod 700 -R .ssh

# 修改ssh端口的详细步骤（centos7）：

# step1 修改/etc/ssh/sshd_config
# vi /etc/ssh/sshd_config
# #Port 22         //这行去掉#号，防止配置不好以后不能远程登录，还得去机房修改，等修改以后的端口能使用以后在注释掉
# Port 20000      //下面添加这一行

# step2 修改firewall配置
# firewall添加想要修改的ssh端口：
# firewall-cmd --zone=public --add-port=20000/tcp --permanent (permanent是保存配置，不然下次重启以后这次修改无效)
# reload firewall:
# firewall-cmd --reload
# 查看添加端口是否成功，如果添加成功则会显示yes，否则no
# firewall-cmd --zone=public --query-port=20000/tcp

# step3 修改SELinux

# #安装semanage
# # yum provides /usr/sbin/semanage
# # yum -y install policycoreutils-python
# 使用以下命令查看当前SElinux 允许的ssh端口：
# semanage port -l | grep ssh

# 添加20000端口到 SELinux
# semanage port -a -t ssh_port_t -p tcp 20000

# 然后确认一下是否添加进去
# semanage port -l | grep ssh
# 如果成功会输出
# ssh_port_t                    tcp    20000, 22

# step4 重启ssh
# systemctl restart sshd.service

# step5 测试新端口的ssh连接
# 测试修改端口以后的ssh连接，如果成功则将step1里面的port 22 重新注释掉


# 重复执行定时任务
# 我们将会使用 cron 和anacron，现在使用以下指令安装 cron 和anacron：
# yum -y install cronie

# yum -y install yum-cron


# /etc/yum/yum-cron.conf  这是每天执行 yum-cron 的配置档案，默认只会下载更新的软件，并不安装，用意是让管理员检视 yum-cron 的输出，选取需要更新的软件进行手动安装。

# --配置SELinux 添加端口 比如mongodb
# semanage port -a -t mongod_port_t -p tcp 27017
# #ssh端口
# semanage port -a -t ssh_port_t -p tcp 20000
