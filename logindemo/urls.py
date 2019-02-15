"""logindemo URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render,HttpResponse,redirect
from app01 import views
def login(request):
    # print(request.method, type(request.method))
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alex' and pwd == '123':
            # return HttpResponse('login sucessful')
            # return redirect('http://jiandan.net/')
            return redirect('/index/')
        # print(request.POST, type(request.POST))
        # print(request.POST['user'],type(request.POST['user']))
    return render(request, 'login.html')

def index(request):
    return render(request,'index.html')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/', views.login),
    url(r'index/', views.index),
    url(r'test/', views.test),
]