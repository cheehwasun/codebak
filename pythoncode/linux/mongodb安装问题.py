#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-23 23:21:30
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$


# mongoDB在centos7上的安装
# 1，下载安装包

# 下载mongoDB的安装文件
# 地址：https://www.mongodb.org/downloads#production 
# 选择Linux 64-bit legacy 版本,下载到目标服务器上。
# 解压文件
# tar -zxvf mongodb-linux-x86_64-3.0.2.tgz
# 进入解压后的目录，把bin文件夹内的文件都置为可执行权限
# chmod -R 755 bin

# 2，创建数据文件路径

# 这里，我希望把数据文件和日志文件都放在data目录下，在任意位置创建data目录
# mkdir data
# 进入data，创建数据文件目录
# mkdir db

# 给data目录赋可写权限
# 我这里粗暴一些，直接777了
# chmod -R 777 data

# 3，编写配置文件

# 为了便于我们启动mongoDB，先编写一个配置文件
# 我这里把配置文件直接放入了bin目录下
# [plain] view plain copy
# vi mongodb.conf  
# 内容如下：
# [plain] view plain copy
# port=27017  
# dbpath=/usr/appdata/mongodb/data/db  
  
# logappend=true  
# fork=true  
# logpath=/usr/appdata/mongodb/data/logs  

# 注意，开启守护进程模式 fork 的时候，一定要设置log日志；
# 设置log日志要注意，logpath的路径一定要是文件路径，而不是文件夹路径。

# 4，测试启动

# 进入bin目录，输入命令
# [plain] view plain copy
# ./mongod -f ./mongodb.conf  

# 这时候会显示数据库启动成功
# 在服务器本地测试一下，使用命令
# [plain] view plain copy
# ./mongo 127.0.0.1  
# MongoDB shell version: 2.6.4  
# connecting to: 127.0.0.1/test  
# 这标识数据库启动成功

# 在局域网内的其它机器使用工具连接测试一下。
# 有的小伙伴可能会发现无法连接，通常这都是防火墙的端口没有打开造成的
# 使用命令打开端口
# [plain] view plain copy
# 开启端口  
# firewall-cmd --zone=public --add-port=27017/tcp --permanent  
# 查看端口  
# firewall-cmd --permanent --query-port=27017/tcp  
  
  
# 重启防火墙  
# firewall-cmd --reload  

# 注意事项：
# a，要加上  --permanent 才能保证重启后也能打开
# b，这里最好重启一下防火墙，有时候开启端口并不能立即生效，什么原因我也不清楚

# 好了，现在局域网内其它机器也可以连接到数据库了。

# 5，注册到系统开机启动

# centos 7的开机启动跟之前版本的centos有很大不同。现在用 systemctl命令代替了之前的chkconfig 和 service 命令
# 注册到开机启动的方法如下：
# 在系统服务目录下新建mongodb的启动服务，并给与754的权限
# [plain] view plain copy
# cd /lib/systemd/system  
# vi mongodb.service  
# [plain] view plain copy
# chmod 754 mongodb.service  

# 内容如下
# [plain] view plain copy
# [Unit]  
  
# Description=mongodb  
# After=network.target remote-fs.target nss-lookup.target  
  
# [Service]  
# Type=forking  
# ExecStart=/usr/appdata/mongodb/bin/mongod -f /usr/appdata/mongodb/bin/mongodb.conf  
# ExecReload=/bin/kill -s HUP $MAINPID  
# ExecStop=/usr/appdata/mongodb/bin/mongod --shutdown -f /usr/appdata/mongodb/bin/mongodb.conf  
# PrivateTmp=true  
  
# [Install]  
# WantedBy=multi-user.target  

# 路径必须要写绝对路径

# [plain] view plain copy
# 启动  
# systemctl start mongodb.service  
# 关闭  
# systemctl stop mongodb.service  
# 注册到开机启动  
# systemctl enable mongodb.service  

# 6，重启机器验证

# reboot 





# Mongodb集群搭建过程及常见错误
# Replica Sets
# MongoDB 支持在多个机器中通过异步复制达到故障转移和实现冗余。多机器中同一时刻只 有一台是用于写操作。正是由于这个情况，为 MongoDB 提供了数据一致性的保障。担当 Primary 角色的机器能把读操作分发给 slave。
# Replica Sets的结构非常类似一个集群。因 为它确实跟集群实现的作用是一样的， 其中一个节点如果出现故障， 其它节点马上会将业务接过来而无须停机操作。
# 下面以本机为例介绍一下集群的部署过程，以及部署过程中常见的注意点及错误
# 本例环境是Linux操作系统，mongodb版本:mongodb-linux-x86_64-2.6.1.tgz，Vmwre虚拟机，虚拟机IP:192.168.169.129,集群以本机不同端口模拟三台服务器。
# 1.集群主要分为三个节点master主节点，slaver备用节点，arbiter仲裁节点
# 建立数据文件夹

# mkdir -p /mongodb/data/master
# mkdir -p /mongodb/data/slaver
# mkdir -p /mongodb/data/arbiter
 

# ps:三个目录分别对应主，备，仲裁节点
# 2.建立配置文件夹
# 1)master.conf
#     打开编辑器:
# 1
# vi /etc/master.conf
# 按i 输入下列配置


# dbpath=/home/mongodb/data/master 
# logpath=/home/mongodb/log/master.log
# logappend=true
# replSet=rep1
# port=10000
# fork=true
# journal=true
# 完成之后按esc  》》 :  >>wq>>回车

# 2）slaver.conf
# 编辑器打开和保存按上边的步骤，下边只写详细内容

# dbpath=/home/mongodb/data/slaver
# logpath=/home/mongodb/log/slaver.log
# logappend=true
# replSet=rep1
# port=10001
# fork=true
# journal=true
# 3）arbiter.conf


# dbpath=/home/mongodb/data/arbiter
# logpath=/home/mongodb/log/arbiter.log
# logappend=true
# replSet=rep1
# port=10002
# fork=true
# journal=true
# smallfiles=true
# 参数解释：

# dbpath：数据存放目录

# logpath：日志存放路径

# logappend：以追加的方式记录日志

# replSet：replica set的名字

# port：mongodb进程所使用的端口号，默认为27017

# fork：以后台方式运行进程

# journal:写日志

# smallfiles:当提示空间不够时添加此参数

# 其他参数

# pidfilepath：进程文件，方便停止mongodb

# directoryperdb：为每一个数据库按照数据库名建立文件夹存放

# bind_ip：mongodb所绑定的ip地址

# oplogSize：mongodb操作日志文件的最大大小。单位为Mb，默认为硬盘剩余空间的5%

# noprealloc：不预先分配存储

# 3.启动Mongodb   


# cd /home/mongodb/bin
 

# 启动服务


# ./mongod -f /etc/master.conf
 
# ./mongod -f /etc/slaver.conf
 
# ./mongod -f /etc/arbiter.conf
#  有这样的提示说明启动成功



# 如果是下列的提示说明启动失败



# 启动失败的原因有很多，检查完配置文件，如果没有错误，可打开相应的配置文件查看详细的错误信息

# cat /etc/master.conf

# 最常见的一个错误就是磁盘空间不足，会提示这样的错误



# 因为Mongodb的日志文件是成2g的增长，所以所需空间比较大，这时你可以在配置文件里添加这样的一个配置
# smallfiles=true。
# 全部三个服务全部启动成功之后
# 4.配置主(master)，备(slaver)，仲裁(arbiter)节点

# 可以通过客户端连接mongodb，也可以直接在三个节点中选择一个连接mongodb。

# ./mongo 192.168.169.129:10000   #ip和port是某个节点的地址

# >use admin

# >cfg={ _id:"rep1", members:[ {_id:0,host:'192.168.169.129:10000',priority:2}, {_id:1,host:'192.168.169.129:10001',priority:1},
# {_id:2,host:'192.168.169.129:10002',arbiterOnly:true}] };
# >rs.initiate(cfg) #使配置生效

# {
#         "set" : "rep1",
#         "date" : ISODate("2014-09-05T02:44:43Z"),
#         "myState" : 1,
#         "members" : [
#                 {
#                         "_id" : 0,
#                         "name" : "192.168.169.129:10000",
#                         "health" : 1,
#                         "state" : 1,
#                         "stateStr" : "PRIMARY",
#                         "uptime" : 200,
#                         "optime" : Timestamp(1357285565000, 1),
#                         "optimeDate" : ISODate("2013-01-04T07:46:05Z"),
#                         "self" : true
#                 },
#                 {
#                         "_id" : 1,
#                         "name" : "192.168.169.129:10001",
#                         "health" : 1,
#                         "state" : 2,
#                         "stateStr" : "SECONDARY",
#                         "uptime" : 200,
#                         "optime" : Timestamp(1357285565000, 1),
#                         "optimeDate" : ISODate("2013-01-04T07:46:05Z"),
#                         "lastHeartbeat" : ISODate("2013-01-05T02:44:42Z"),
#                         "pingMs" : 0
#                 },
#                 {
#                         "_id" : 2,
#                         "name" : "192.168.169.129:10002",
#                         "health" : 1,
#                         "state" : 7,
#                         "stateStr" : "ARBITER",
#                         "uptime" : 200,
#                         "lastHeartbeat" : ISODate("2013-01-05T02:44:42Z"),
#                         "pingMs" : 0
#                 }
#         ],
#         "ok" : 1
# }
 
# 配置过程中可能还会出现其他的一些错误，不过都可以去查看相应的日志文件，去解决。
