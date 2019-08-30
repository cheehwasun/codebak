#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-23 23:25:50
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$


# git操作
# git config --global core.autocrlf false
# $ git config --global user.name "Your Name"
# $ git config --global user.email "email@example.com"

# 第二步，通过git init命令把这个目录变成Git可以管理的仓库：

# $ git init


# 第一步，用命令git add告诉Git，把文件添加到仓库：

# $ git add readme.txt

# 第二步，用命令git commit告诉Git，把文件提交到仓库：

# $ git commit -m "wrote a readme file"


# 初始化一个Git仓库，使用git init命令。

# 添加文件到Git仓库，分两步：

# 第一步，使用命令git add <file>，注意，可反复多次使用，添加多个文件；

# 第二步，使用命令git commit，完成。


# git remote add origin https://github.com/cheehwasun/616.git
# git push -u origin master


#回到上次修改
# git reset --hard HEAD^

# 查看记录
# git log  

# 可以顺着往上找啊找啊，找到那个append GPL的commit id是3628164于是就可以指定回到未来的某个版本
# $ git reset --hard 3628164
# HEAD is now at 3628164 append GPL

# git reflog用来记录你的每一次命令：


# 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令
# git checkout -- file。

# 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令
# git reset HEAD file，就回到了场景1，第二步按场景1操作。

# 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。


# git rm     用于删除一个文件
# $ git checkout -- test.txt 可以从库中恢复

# 远程库初始化一个新的空项目 一个是ssh 一个https
# git clone git@github.com:michaelliao/gitskills.git
# git clone https://github.com/michaelliao/gitskills.git


# 首先，我们创建dev分支，然后切换到dev分支：

# $ git checkout -b dev
# Switched to a new branch 'dev'
# git checkout命令加上-b参数表示创建并切换，相当于以下两条命令：

# $ git branch dev
# $ git checkout dev
# Switched to branch 'dev'

# Git鼓励大量使用分支：

# 查看分支：git branch

# 创建分支：git branch <name>

# 切换分支：git checkout <name>

# 创建+切换分支：git checkout -b <name>

# 合并某分支到当前分支：git merge <name>

# 删除分支：git branch -d <name>

# 当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。

# 用git log --graph命令可以看到分支合并图。


# 分支策略

# 在实际开发中，我们应该按照几个基本原则进行分支管理：

# 首先，master分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；

# 那在哪干活呢？干活都在dev分支上，也就是说，dev分支是不稳定的，到某个时候，比如1.0版本发布时，再把dev分支合并到master上，在master分支发布1.0版本；

# 你和你的小伙伴们每个人都在dev分支上干活，每个人都有自己的分支，时不时地往dev分支上合并就可以了。

# 合并分支时，加上--no-ff参数就可以用普通模式合并
# git merge --no-ff



# 工作区是干净的，刚才的工作现场存到哪去了？用git stash list命令看看

# 修复bug时，我们会通过创建新的bug分支进行修复，然后合并，最后删除；

# 当手头工作没有完成时，先把工作现场git stash一下，然后去修复bug，修复后，再git stash pop，回到工作现场

# 开发一个新feature，最好新建一个分支；

# 如果要丢弃一个没有被合并过的分支，可以通过git branch -D <name>强行删除

# 查看远程库信息，使用git remote -v；

# 本地新建的分支如果不推送到远程，对其他人就是不可见的；

# 从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；

# 在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；

# 建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；

# 从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。

# 命令git tag <name>用于新建一个标签，默认为HEAD，也可以指定一个commit id；

# git tag -a <tagname> -m "blablabla..."可以指定标签信息；

# git tag -s <tagname> -m "blablabla..."可以用PGP签名标签；

# 命令git tag可以查看所有标签。

# 命令git push origin <tagname>可以推送一个本地标签；

# 命令git push origin --tags可以推送全部未推送过的本地标签；

# 命令git tag -d <tagname>可以删除一个本地标签；

# 命令git push origin :refs/tags/<tagname>可以删除一个远程标签。



#ssh设置

	# 1、设置Git的user name和email：(如果是第一次的话)
	#     $ git config --global user.name "cheehwasun"
	#     $ git config --global user.email "cheehwasun@163.com"
	# 2、生成密钥
	#     $ ssh-keygen -t rsa -C "cheehwasun@163.com"
	# 连续3个回车。如果不需要密码的话。
	# 最后得到了两个文件：id_rsa和id_rsa.pub。

	# 如果不是第一次，就选择overwrite.


	# 3、添加密钥到ssh-agent
	# 确保 ssh-agent 是可用的。ssh-agent是一种控制用来保存公钥身份验证所使用的私钥的程序，其实ssh-agent就是一个密钥管理器，运行ssh-agent以后，使用ssh-add将私钥交给ssh-agent保管，其他程序需要身份验证的时候可以将验证申请交给ssh-agent来完成整个认证过程。

	#     # start the ssh-agent in the background
	#     eval "$(ssh-agent -s)"
	#     Agent pid 59566
	# 添加生成的 SSH key 到 ssh-agent。

	#     $ ssh-add ~/.ssh/id_rsa


	# 4、登陆Github, 添加 ssh 。
	# 把id_rsa.pub文件里的内容复制到这里

	# 5、测试：
	#     $ ssh -T git@github.com
	# 你将会看到：

	#     The authenticity of host 'github.com (207.97.227.239)' can't be established.
	#     RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
	#     Are you sure you want to continue connecting (yes/no)?
	# 选择 yes

	#     Hi humingx! You've successfully authenticated, but GitHub does not provide shell access.
	# 如果看到Hi后面是你的用户名，就说明成功了。


	# 6、修改.git文件夹下config中的url。
	# 修改前

	#     [remote "origin"]
	#     url = https://github.com/humingx/humingx.github.io.git
	#     fetch = +refs/heads/*:refs/remotes/origin/*
	# 修改后

	#     [remote "origin"]
	#     url = git@github.com:humingx/humingx.github.io.git
	#     fetch = +refs/heads/*:refs/remotes/origin/*



# 	以ubuntu服务器为例，如果要创建小范围的私有git服务器，是非常简单的，只需要如下几个简单步骤：

# Step 1: 安装git

# 直接通过sudo apt-get install git即可完成。

# Step 2: 创建git用户

# git用户用来通过SSH连接git服务，输入命令：

# $ sudo adduser git

# Step 3: 创建证书登录

# 首先收集所有需要登录的用户公钥，然后导入到/home/git/.ssh/authorized_keys文件即可。

# Step 4: 初始化git仓库

# 假设仓库位于/srv/sample.git，在/srv目录下输入命令：

# $ sudo git init --bare sample.git

# 这样就创建了一个裸仓库，裸仓库没有working dir，因为服务器上的git仓库纯粹是为了共享，仓库目录一般以.git结尾。然后把owner改为git：

# $ sudo chown -R git:git sample.git

# Step 5: 防止登录shell

# 出于安全考虑，git用户不应该登录shell，可以编辑/etc/passwd，找到类似一行：

# git:x:1001:1001:,,,:/home/git:/bin/bash

# 改为：

# git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell
