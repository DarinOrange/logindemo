from django.shortcuts import render, HttpResponse, redirect
from app01 import models


def login(request):
    # 获取提交的数据
    print(request.GET)
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alex' and pwd == 'alexdsb':
            # return redirect('http://jandan.net/')
            return render(request, 'login2.html')
            # return redirect('/index/')
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


# 测试ORM操作
def test(request):
    # all = models.User.objects.all()
    # print(all, type(all))
    # first = all[0]
    # print(first,type(first))
    # print(first.name,first.pwd)
    # one = models.User.objects.get(name='alex')
    # print(one,type(one))
    ret = models.User.objects.filter(name='alex', pwd='123')[0]
    print(ret, type(ret))
    print(ret.id, ret.pk)

    return HttpResponse('ok')
