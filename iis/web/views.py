from django.shortcuts import render,HttpResponse,redirect

from . import models
import pymongo

# Create your views here.#

#session验证
def handle_validate(request):
	if request.method=='POST':
		username=request.POST.get('username')			
		pwd=request.POST.get('pwd')
		try:
			p=models.UserInfo.objects.get(user=username)
		except Exception as e:
			return False
		if pwd==p.pwd:
			request.session['IS_LOGIN']=True
			request.session['USERNAME']=username
			return True
	return False

def index(request):
	return redirect('/it/home')

def login(request):
	is_ok=handle_validate(request)
	if is_ok:
		return redirect('/it/home/')
	else:
		return render(request, 'error.html')

def logout(request):
	del request.session['IS_LOGIN']
	return redirect('/it/login/')

def home(request):		
	is_login=request.session.get('IS_LOGIN',False)
	if is_login:
		username=request.session.get('USERNAME',False)
		return render(request, 'web/home.html',{'username':username})
	return render(request, 'web/login.html')

def ok(request):
	return render(request, 'ok.html')


#ajax异步调用测试
import json
def ajaxtest(request):
	ret={'status':True,'error':''}
	try:
		print(request.POST)
	except Exception as e:
		ret['status']=False
		ret['error']=str(e)
	return HttpResponse(json.dumps(ret,indent=2))

#上传组件测试
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def uploadtest(request):
	#session 验证
	is_login=request.session.get('IS_LOGIN',False)
	if is_login:
		if request.method=='POST':
			in_file=request.FILES
			file=in_file.get('f1')
			handle_upload(file)
			return redirect('/it/ok.html')
		return render(request, 'upload.html')
	else:
		return redirect('/it/home/')

def handle_upload(file):
	try:
		path=os.path.join('data',file.name)
		with open(path,'wb') as f:
			for each in file.chunks():
				f.write(each)
	except Exception as e:
		return False
	return True

def son(request):
	return render(request, '5.html')

# 分页测试
def ajaxpagetest(request,param):
	lo=(int(param)-1)*10
	userlist=models.UserList.objects.all().values_list('username','age')[lo:lo+10]
	if not len(userlist):
		return HttpResponse('status=403')

	l=[]
	for each in userlist:
		l.append(each)
	return JsonResponse(l,safe=False)
	


from django.http import JsonResponse
import json
#序列化Json两种方法
def ajax_list(request):
    a = list(range(100))
    return JsonResponse(a,safe=False) 
def ajax_dict(request):
    name_dict = {'a': 1, 'b': 2, 'c':3, 'd':4}
    return HttpResponse(json.dumps(name_dict,indent=2,sort_keys=True), content_type='application/json')



# from django.views.decorators.cache import cache_page

# @cache_page(60*15) #15分钟
# def cache(request):
# 	return HttpResponse('cache 15 fenzhong')
def deltest(request):
	a=models.UserList.objects.filter(id__gt=3).delete()
	return HttpResponse('ok')

def test(request):

	l_counts=models.UserList.objects.all().count()
	nums,div=divmod(l_counts,10)

	if div==0:
		totalpages=nums
	else:
		totalpages=nums+1

	if totalpages<7:
		i=totalpages+1
	else:
		i=7+1
	pagenum=list(range(2,i))

	return render(request, '1.html',{'totalpages':totalpages,'pagenum':pagenum})
