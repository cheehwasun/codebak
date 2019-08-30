from django.db import models

# Create your models here.
class UserInfo(models.Model):
	user=models.CharField(max_length=16)
	pwd=models.CharField(max_length=32)

class UserList(models.Model):
	username=models.CharField(max_length=16)
	age= models.IntegerField(default=0)

class Article(models.Model):  
    ''''' 
    文章表 
    '''  
    title = models.CharField(u"文章标题",max_length=255,unique=True)  
    # categroy = models.ForeignKey("Category",verbose_name=u"板块")  
    #blank=True,null=True,后台提交form允许keywords为空  
    keywords = models.CharField(u'文章关键字',max_length=255,blank=True,null=True)  
    description = models.TextField(u'描述',max_length=200,blank=True,null=True)  
    # head_img = models.ImageField(u"缩略图",upload_to="static/uploads")  
    #content = models.TextField(u"文章内容",)  
    content = models.TextField(blank=True,null=True,verbose_name="文章内容")  
    # author = models.ForeignKey("UserProfile",verbose_name=u"作者")  
    publish_date = models.DateTimeField(u'发布时间',auto_now=True)  
    hideden = models.BooleanField(u"是否隐藏",default=False)  
    weight = models.IntegerField(u"优先级",default=1000)  
  
    def __str__(self):  
        return "<%s,author:%s>" %(self.title,self.author)  


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
 
class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __str__(self):
        return self.name
 
class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name    = models.CharField(max_length=50)
    def __str__(self):
        return self.name