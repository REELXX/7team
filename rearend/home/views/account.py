"""
注册，登录，注销
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .. import models
from django.contrib.auth import logout


# session
def login(request):
    if request.method == 'GET':
        return render(request, 'home/login1.html')
    else:
        name = request.POST.get('username')
        pwd  = request.POST.get('password')
        # if request.POST.get('username') == CISCO123 and request.POST['password'] == CISCO123:
        if name == 'CISCO123' and pwd == '':
            return render(request, 'home/index.html')
        else:
            return render(request, 'home/login1.html')

#
# def showlogin(request):
#     # 储存session
#     username = request.POST.get('username')
#     request.session['name'] = username
#     return HttpResponseRedirect('/home')
#
# #
# # def main(request):
#     username = request.session.get('name', '游客')
#     return render(request, 'home/main.html', {'username': username})


# def quitzh(request):
#     # 清除session
#     logout(request)
#     return HttpResponseRedirect('/main')

def home(request):
    return render(request, 'home/index.html')
def index2(request):
    return render(request,'home/index2.html')
def index3(request):
    return render(request,'home/index3.html')
