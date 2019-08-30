# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Date    : 2017-11-30 10:16:17
# # @Author  : kakarot (kakarotsun@163.com)
# # @Link    : http://example.org
# # @Version : $Id$

# 创建项目：django-admin startptoject mydjango
# 项目启动：python manage.py  runserver 0.0.0.0:8080

# 	③ settings.py(最重要)
# 	ALLOWED_HOSTS如果有值，只允许同意的主机进行访问 * 表示全可以访问
# 	ROOT_URLCONF = 'myblog.urls'  它指向 urls.py 文件
# 	setting的DEBUG生产中不能为true  因为会把日志信息暴露给前端页面用户 这个参数测试环境调试用

# 	在INSTALL_APPS写入创建的APP


# 创建应用：python manage.py starapp blog
# 添加应用：settings.py的 installed_apps中

# 	URL配置（第一种）：
# 	urlpatterns第一个参数，写URL，即路径。访问该路径看到对应的网页
# 	第二个参数，方法，即响应。访问路径后的响应。需把对应的模块导入
# 	from django.conf.urls import url,include
# 	from django.contrib import admin

# 	url(r'^myapp/', include('myapp.urls')),

# 	urlpatterns = [
# 	    url(r'^index/$', views.index),
# 	]

# 	关于url的几个知识点：
# 	1.在根目录下面有一个urls.py文件，同时在blog中新建一个urls.py文件，里面内容一致，只不过可以在根目录下使用include，指向blog中的所有url，在blog中配置的过程中需要注意：
# 	    1）如果根目录和blog目录下的urls.py文件书写都为r'^index/',那么访问的时候需要http://127.0.0.1:8000/index/index才可以访问到。

# 	     r'^index/$' 后面必须添加 / 的原因是该 app 的页面索引 index 处在 url 字符串的结尾，为了使 根据 url 找到页面正常（也就是不会出现 /index/index/1243ede 仍然能匹配到 blog app 的 index 页面最后显示hello world的情况）正则表达式的结尾添加了 $ ,这也表明app 的页面索引 index 处在 url 字符串的结尾。之所以 $ 前面必须添加 / ，是因为浏览器总是会在页面的最后添加一个 / 比如 index/index/ （即使你不手动添加 / 浏览器也会自动给你加上），因此 如果不加 / ,那么正则表达式就匹配不到


# 创建Tamplates：
# 1.在应用的根目录下创建Tamplates目录。
# 2.在Tamplates目录下创建HTML文件。
# 3.在views.py中返回render
# render有三个参数，第一个request，第二个模板。第三个支持一个dict类型参数，传递数据到前端。（键值对，键就是前端获取的参数名，就是模板中类似{{}}引用的，值是我们要传递给前端的数据）


# 	注意：Django按照INSTALLED_APPS中的添加顺序查找templates（如果模板名字一致的话，会造成冲突）
# 	解决方式：在APP的Templates目录下创建以APP名为名称的目录，再把HTML文件放入新创建的目录下。
# 	然后把render的第二个参数改为'blog/index.html'  假如blog是我们新建的目录

# django Models 流程
# 在应用根目录下创建models.py 并引入models模块 from django.db import models
# 创建一个类继承models.Model
# class Article(models.Model):
# 	title=models.CharField(max_length=32,default='Title')
# 	content=models.TextField(null=True)

# 然后生成数据表
# python manage.py makemigrations app名（可选）

# python manage.py migrate

# 查看 数据表
# python manage.py sqlmigrate 应用名 文件id

# python manage.py sqlmigrate myapp 0001

# 查看并编辑db.sqlite3
# 使用第三方软件
# sqlite expert personal

# 页面呈现
# views.py 中import models
# article=models.Article.objects.get(pk=1)
# render(request,page,{'article':article})

# 前端模板可以直接使用对象以及对象的.操作
# {{article.title}}

# 配置超级用户
# python manage.py createsuperuser
# /admin/ 入口
# 修改settings.py 设置中文

# admin配置：
# 1.在应用下的Model.py文件中，导入自身的models模块（或者里边的模型类）
# from . import models
# 2.编辑admin.py，加入代码admin.site.register(models.Article)
# 修改默认的admin中名字显示：
# 在类里边增加方法，def __str__(self):return self.title(python3)

# 模板的常用
#     {% for article in articles %}
# 	<a href="">{{article.title}}</a>
# 	</br>
# 	{% endfor %}



# @·url函数的名称参数
# ①跟urls，卸载include()的第二个参数未知，namespace = 'blog'
# ②应用下则卸载url()的第三个参数位置，name = 'a1'
# url(r'^article/(?P<article_id>[0-9]+)$', views.article,name='a1'),
# 主要取决于是否使用include应用了另一个url配置文件

# 超链接目标地址
# href 后面是目标地址
# template 中可以用 "{% url 'blog:a1' param % }"

# 创建 admin 配置类
# class ArticleAdmin(admin.ModelAdmin)
# 注册：admin.site.register(Article,ArticleAdmin)
# 2.在 admin 管理界面添加其他字段
# 在配置类中添加  list_display = ('title','content')  ,list_display 同时支持 tuple 和 list
# 3.Admin 过滤器  list_filter = ('pub_time',)




# Django-Model操作数据库(增删改查、连表结构）

# 一、数据库操作

# 1、创建model表
       
# 基本结构


# from django.db import models
   
# class userinfo(models.Model):
#     #如果没有models.AutoField，默认会创建一个id的自增列
#     name = models.CharField(max_length=30)
#     email = models.EmailField()
#     memo = models.TextField()
# 更多字段：

# 1、models.AutoField　　自增列= int(11)
# 　　如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True。
# 2、models.CharField　　字符串字段
# 　　必须 max_length 参数
# 3、models.BooleanField　　布尔类型=tinyint(1)
# 　　不能为空，Blank=True
# 4、models.ComaSeparatedIntegerField　　用逗号分割的数字=varchar
# 　　继承CharField，所以必须 max_lenght 参数
# 5、models.DateField　　日期类型 date
# 　　对于参数，auto_now =True则每次更新都会更新这个时间；auto_now_add 则只是第一次创建添加，之后的更新不再改变。
# 6、models.DateTimeField　　日期类型 datetime
# 　　同DateField的参数
# 7、models.Decimal　　十进制小数类型= decimal
# 　　必须指定整数位max_digits和小数位decimal_places
# 8、models.EmailField　　字符串类型（正则表达式邮箱）=varchar
# 　　对字符串进行正则表达式
# 9、models.FloatField　　浮点类型= double
# 10、models.IntegerField　　整形
# 11、models.BigIntegerField　　长整形
# 　　integer_field_ranges ={
# 　　　　'SmallIntegerField':(-32768,32767),
# 　　　　'IntegerField':(-2147483648,2147483647),
# 　　　　'BigIntegerField':(-9223372036854775808,9223372036854775807),
# 　　　　'PositiveSmallIntegerField':(0,32767),
# 　　　　'PositiveIntegerField':(0,2147483647),
# 　　}
# 12、models.IPAddressField　　字符串类型（ip4正则表达式）
# 13、models.GenericIPAddressField　　字符串类型（ip4和ip6是可选的）
# 　　参数protocol可以是：both、ipv4、ipv6
# 　　验证时，会根据设置报错
# 14、models.NullBooleanField　　允许为空的布尔类型
# 15、models.PositiveIntegerFiel　　正Integer
# 16、models.PositiveSmallIntegerField　　正smallInteger
# 17、models.SlugField　　减号、下划线、字母、数字
# 18、models.SmallIntegerField　　数字
# 　　数据库中的字段有：tinyint、smallint、int、bigint
# 19、models.TextField　　字符串=longtext
# 20、models.TimeField　　时间 HH:MM[:ss[.uuuuuu]]
# 21、models.URLField　　字符串，地址正则表达式
# 22、models.BinaryField　　二进制
# 23、models.ImageField图片
# 24、models.FilePathField文件
# 　　

# 更多参数

# 1、null=True
# 　　数据库中字段是否可以为空
# 2、blank=True
# 　　django的Admin中添加数据时是否可允许空值
# 3、primary_key =False
# 　　主键，对AutoField设置主键后，就会代替原来的自增 id 列
# 4、auto_now 和 auto_now_add
# 　　auto_now 自动创建---无论添加或修改，都是当前操作的时间
# 　　auto_now_add 自动创建---永远是创建时的时间
# 5、choices
# GENDER_CHOICE =(
# (u'M', u'Male'),
# (u'F', u'Female'),
# )
# gender = models.CharField(max_length=2,choices = GENDER_CHOICE)
# 6、max_length
# 7、default　　默认值
# 8、verbose_name　　Admin中字段的显示名称
# 9、name|db_column　　数据库中的字段名称
# 10、unique=True　　不允许重复
# 11、db_index =True　　数据库索引
# 12、editable=True　　在Admin里是否可编辑
# 13、error_messages=None　　错误提示
# 14、auto_created=False　　自动创建
# 15、help_text　　在Admin中提示帮助信息
# 16、validators=[]
# 17、upload-to
 
 
# 2、注册APP，settings添加app
# 3、生成相应的表
#     python manage.py makemigrations
#     python manage.py migrate   
 
# 4、admin后台注册表

# python manage.py createsuperuser 创建用户
# 后台可以管理，添加数据


 
 
# 对数据进行增删改查
# 查
# models.UserInfo.objects.all()
# models.UserInfo.objects.all().values('user')    #只取user列
# models.UserInfo.objects.all().values_list('id','user')    #取出id和user列，并生成一个列表
# models.UserInfo.objects.get(id=1)
# models.UserInfo.objects.get(user='yangmv')



# 成功获取数据

 
 
# 增
# models.UserInfo.objects.create(user='yangmv',pwd='123456')
# 或者
# obj = models.UserInfo(user='yangmv',pwd='123456')
# obj.save()
# 或者
# dic = {'user':'yangmv','pwd':'123456'}
# models.UserInfo.objects.create(**dic)

# 删
# models.UserInfo.objects.filter(user='yangmv').delete()

# 改
 
# models.UserInfo.objects.filter(user='yangmv').update(pwd='520')
# 或者
# obj = models.UserInfo.objects.get(user='yangmv')
# obj.pwd = '520'
# obj.save()

 
 
#  常用方法
# + View Code

# 二、常用字段
# models.DateTimeField　　日期类型 datetime
# 参数，
# auto_now = True ：则每次更新都会更新这个时间
# auto_now_add 则只是第一次创建添加，之后的更新不再改变。
 

# class UserInfo(models.Model):
#     name = models.CharField(max_length=32)
#     ctime = models.DateTimeField(auto_now=True)
#     uptime = models.DateTimeField(auto_now_add=True)

# from web import models
# def home(request):
#     models.UserInfo.objects.create(name='yangmv')
#     after = models.UserInfo.objects.all()
#     print after[0].ctime
#     return render(request, 'home/home.html')

 
# 表结构的修改
# 表结构修改后，原来表中已存在的数据，就会出现结构混乱，makemigrations更新表的时候就会出错
# 解决方法：
# 1、新增加的字段，设置允许为空。生成表的时候，之前数据新增加的字段就会为空。(null=True允许数据库中为空，blank=True允许admin后台中为空)
# 2、新增加的字段，设置一个默认值。生成表的时候，之前的数据新增加字段就会应用这个默认值

# 执行makemigrations， migrate 后。老数据会自动应用新增加的规则

# models.ImageField                        图片
# models.GenericIPAddressField      IP
# ip = models.GenericIPAddressField(protocol="ipv4",null=True,blank=True)
# img = models.ImageField(null=True,blank=True,upload_to="upload")


# 数据库中保存的只是图片的路径

# 常用参数
# 选择下拉框 choices
# class UserInfo(models.Model):
#     USER_TYPE_LIST = (
#         (1,'user'),
# (2,'admin'),
# )
#     user_type = models.IntegerField(choices=USER_TYPE_LIST,default=1)


# 2、连表结构

# 一对多：models.ForeignKey(其他表)
# 多对多：models.ManyToManyField(其他表)
# 一对一：models.OneToOneField(其他表)
# 应用场景：

# 一对多：当一张表中创建一行数据时，有一个单选的下拉框（可以被重复选择）
# 例如：创建用户信息时候，需要选择一个用户类型【普通用户】【金牌用户】【铂金用户】等。
# 多对多：在某表中创建一行数据是，有一个可以多选的下拉框
# 例如：创建用户信息，需要为用户指定多个爱好
# 一对一：在某表中创建一行数据时，有一个单选的下拉框（下拉框中的内容被用过一次就消失了
# 例如：原有含10列数据的一张表保存相关信息，经过一段时间之后，10列无法满足需求，需要为原来的表再添加5列数据
 
 
# 一对多：

# 6
# class Game(models.Model):
#     gname = models.CharField(max_length=32)
 
# class Host(models.Model):
#     hostname = models.CharField(max_length=32)
#     game = models.ForeignKey('Game')
# 　　

# 这是Game表，里面有3个业务

# 这是主机表，可以通过外键，对应到Game表的业务的ID

 
 
# 多对多：

# class UserGroup(models.Model):
#     group_name = models.CharField(max_length=16)
 
# class User(models.Model):
#     name = models.CharField(max_length=16)
#     sex = models.CharField(max_length=16)
#     email = models.EmailField(max_length=32)
#     usergroup_user = models.ManyToManyField('UserGroup')

# Django model会自动创建第3张关系表，用于对应user id 和usergroup id
# 这是UserGroup表

# 这是User表

# 这是Django自动生成的对应关系表

# user_id = 1 为 yangmv，同时属于1,2(技术部，运营部)

# 一对一：   （一对多增加了不能重复）

# class User2(models.Model):
#     name = models.CharField(max_length=16)
#     sex = models.CharField(max_length=16)
#     email = models.EmailField(max_length=32)
 
# class Admin(models.Model):
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     admin_user2 = models.OneToOneField('User2')

# 连接Mysql
# + View Code

#  一对多操作实例
# 首先生成2个表

# from django.db import models
 
# class Group2(models.Model):
#     caption = models.CharField(max_length=32)
 
# class User2(models.Model):
#     username = models.CharField(max_length=32)
#     group2 = models.ForeignKey('Group2')
# 　　

# input和select标签用forms生成

# 先执行create_group生成3个group

# 已经查询出Group数据

# 添加
# 方法1，方法2

# def create_user(request):
#     obj = Forign.UserForm(request.POST)
#     if request.method == 'POST':
#         if obj.is_valid():
#             all_data = obj.clean()
#             #print all_data
#             #获取提交页面提交来的数据{'username': u'yang1', 'usergroup': 1}
#             #方法1，先获取对象，添加
#             #group_obj = models.Group2.objects.get(id=all_data['usergroup'])
#             #models.User2.objects.create(username=all_data['username'],usergroup=group_obj)
#             #方法2(推荐)
#             models.User2.objects.create(username=all_data['username'],group2_id=all_data['usergroup'])
#             #django会自动把数据库group2变为group2_id
#         else:
#             error = obj.errors
#             print error['username'][0]
#             print error['usergroup'][0]
#     return render(request,'forign/create_user.html',{'obj':obj})
# 　　


# 方法3

# def create_user(request):
#     obj = Forign.UserForm(request.POST)
#     if request.method == 'POST':
#         if obj.is_valid():
#             all_data = obj.clean()
#             #print all_data
#             #获取提交页面提交来的数据{'username': u'yang1', 'usergroup': 1}
#             #方法1，先获取对象，添加
#             #group_obj = models.Group2.objects.get(id=all_data['usergroup'])
#             #models.User2.objects.create(username=all_data['username'],usergroup=group_obj)
#             #方法2(推荐)
#             #models.User2.objects.create(username=all_data['username'],group2_id=all_data['usergroup'])
#             #django会自动把数据库group2变为group2_id
#             #方法3(推荐)
#             models.User2.objects.create(**all_data)
#             print models.User2.objects.all().count()
#         else:
#             pass
#             # error = obj.errors
#             # print error['username'][0]
#             # print error['usergroup_id'][0]
#     return render(request,'forign/create_user.html',{'obj':obj})
# 　　

# 查询。展示出所有的数据


# def create_user(request):
#     obj = Forign.UserForm(request.POST)
#     if request.method == 'POST':
#         if obj.is_valid():
#             all_data = obj.clean()
#             #方法3(推荐)
#             models.User2.objects.create(**all_data)
#             print models.User2.objects.all().count()
#         else:
#             pass
#     user_list = models.User2.objects.all()
#     return render(request,'forign/create_user.html',{'obj':obj,'user_list':user_list})

# <table border="1">
#     {% for item in user_list %}
#         <tr>
#             <td>{{ item.username }}</td>
#             <td>{{ item.group2.caption }}</td>
#         </tr>
#     {% endfor %}
# </table>
# 　　


# GET方式查询

# def create_user(request):
#     obj = Forign.UserForm(request.POST)
#     if request.method == 'POST':
#         if obj.is_valid():
#             all_data = obj.clean()
#             #方法3(推荐)
#             models.User2.objects.create(**all_data)
#             print models.User2.objects.all().count()
#         else:
#             pass
#     #查用户
#     get_user = request.GET.get('username')
#     user_list = models.User2.objects.filter(username=get_user)
#     return render(request,'forign/create_user.html',{'obj':obj,'user_list':user_list})
 

# #查组
# get_val = request.GET.get('group')
# user_list = models.User2.objects.filter(group2__caption=get_val)
# 　　

# 一对多跨表操作，总结
# 1、group2对应的是一个对象
# 2、创建数据 group2_id ，直接查询数据库
# 3、获取数据，通过.     group2.caption
# 4、查询数据，通过__   group2__caption