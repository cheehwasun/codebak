"""iis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.test),
    url(r'^it/', include('web.urls',namespace='web')), #通过app请求
    url(r'^user_list/(\d+)/(\d+)$', views.index), #分页请求
    url(r'^user_list/(?P<v1>\d+)/(?P<v2>\d+)$', views.index), #通过参数请求 比如K_V
]
