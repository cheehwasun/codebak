#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-20 23:40:30
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$
######sf###

# 一些mongodb 安装出现的问题

# 查看mongo 是否在进程中
# pgrep mongo -l


# 安装
# 一、导入包管理系统使用的公钥

# sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

# 二、为MongoDB创建一个列表文件

# Ubuntu 16.04
# echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

# 三、重新加载本地包数据库

# sudo apt-get update

# 四、安装最新的稳定版本的MongoDB

# sudo apt-get install -y mongodb-org

# 六、启动MongoDB

# sudo service mongod start

# 七、关闭MongoDB

# sudo service mongod stop

# 八、重启MongoDB

# sudo service mongod restart

# 九、卸载MongoDB

# sudo service mongod stop

# sudo apt-get purge mongodb-org*

# sudo rm -r /var/log/mongodb
# sudo rm -r /var/lib/mongodb

# 十、配置文件

# dbpath
# /var/lib/mongodb

# logpath
# /var/log/mongodb

# config path
#  /etc/mongod.conf

# 警告处理

# 在 /etc/rc.local 文件中添加

#sudo /usr/bin/mongod --config /etc/mongodb.conf  #自启动

# if test -f /sys/kernel/mm/transparent_hugepage/enabled; then
#    echo never > /sys/kernel/mm/transparent_hugepage/enabled
# fi
# if test -f /sys/kernel/mm/transparent_hugepage/defrag; then
#    echo never > /sys/kernel/mm/transparent_hugepage/defrag
# fi

# 创建用户权限
# db.createUser(
#   {
#     user: "asd", //用户名
#     pwd: "123", //密码
#     customData:{"desc":"This user is for administrators"},
#     roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] //权限
#   }
# )

#更换配置目录
# vi /etc/mongodb.conf 
# dbpath=/john/mongodb
# vi /etc/init.d/mongodb 
# DATA=/john/mongodb
# mkdir /john/mongodb/ 
# chown -R mongodb:mongodb /john/mongodb/
# vi /etc/passwd
# mongodb 目录改为/john/mongodb