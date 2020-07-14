from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('soulgoodman')


from .models import Router, Port


def router(request):
    # 去模型取数据
    routerlist = Router.objects.all()
    # 将数据传递给模板，模板再渲染页面，将页面返回web
    return render(request,'myapp/router.html',{'Router':routerlist})


def port(request):
    portlist = Port.objects.all()
    return render(request,'myapp/port.html',{'Port':portlist})


def routerport(request,num):
    # 获得对应的路由器对象
    routerlist = Router.objects.get(pk=num)
    # 获得路由器下所有端口对象
    portlist = routerlist.port_set.all()
    return render(request,'myapp/port.html',{'Port':portlist})


