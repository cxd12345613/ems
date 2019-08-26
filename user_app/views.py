import os
import uuid

from django.db import transaction
from django.shortcuts import render, HttpResponse, redirect
from user_app.models import User
from datetime import datetime
import time
# Create your views here.





def login(request):
    n = request.COOKIES.get('name')
    p = request.COOKIES.get('pwd')
    result = User.objects.filter(user=n, password=p)

    if result:
        request.session['a'] = 'ok'
        return redirect('emplist_app:emp')
    return render(request,'user_app/login.html',{
        'time':datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    })


def loginlogic(request):

    res=redirect('emplist_app:emp')
    rem=request.POST.get('rember')
    user=request.POST.get('name')
    pwd=request.POST.get('pwd')
    if rem:
        res.set_cookie('name',user,max_age=5*3600)
        res.set_cookie('pwd',pwd,max_age=50*3600)
    result=User.objects.filter(user=user,password=pwd)
    code = request.session.get('code')
    input_code = request.POST.get('captcha')
    print(code.lower(), input_code.lower(),result)
    if input_code.lower()==code.lower() and result:
        request.session['a']='ok'

        return res
    else:
        return redirect('user_app:login')


def regist(request):
    return render(request,'user_app/regist.html',{
        'time': datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    })

def registlogic(request):
    try:
        with transaction.atomic():
            user = request.POST.get('username')
            name = request.POST.get('name')
            ##获取上传文件
            headpic=request.FILES.get('source')
            # 获取文件的extension（扩展名-后缀名）
            ext = os.path.splitext(headpic.name)
            #uuid随机产生32位数字，保证图片的名字不重复，拼接图片后缀
            headpic.name = str(uuid.uuid4()) + ext[1]
            pwd=request.POST.get('pwd')
            sex=request.POST.get('sex')
            print(headpic,user,name,pwd,sex)
            result=User.objects.create(user=user,name=name,password=pwd,sex=sex,pic=headpic)
            print(result)
            if result:
                return redirect('user_app:login')
    except Exception as e:
        print(e)
        return HttpResponse('注册失败！')

def checkName(request):
    # time.sleep(3)
    user = request.POST.get('username')

    checkname = User.objects.filter(user=user)
    if checkname:
        return HttpResponse('用户名以存在')
    else:
        return HttpResponse('用户名可以使用')

def checkCaptcha(request):
    code = request.session.get('code')
    input_code = request.POST.get('number')

    if code.lower()==input_code.lower():
        return HttpResponse('验证成功')
    else:
        return HttpResponse('验证失败')