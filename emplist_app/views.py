import os
import uuid

from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, redirect,HttpResponse
from emplist_app.models import Employee
from datetime import datetime
# Create your views here.


##主页显示员工信息
def emplist(request):
    if request.session.get('a')=='ok':
        emp=Employee.objects.all()
        #构造分页器对象,每3条数据为一页
        pagtor=Paginator(emp,per_page=3)
        #获取页码
        n=request.GET.get('number')
        #判断所选页码，初始为第一页，错误为第一页
        num=request.session.get('num')
        print(num)
        if num!='no' and num!='add':
            n=num
            count=pagtor.num_pages
            if int(n)>count:
                n=int(n)-1
            request.session['num']='no'
        elif num=='add':
            n=pagtor.page_range[-1]
            request.session['num']='no'
        try:
            if int(n) not in pagtor.page_range:   #range(1,总页+1)
                n=1
        except:
            n=1
            #获取页数对象
        page=pagtor.page(n)
        return render(request,'emplist_app/emplist.html',{
            'page':page,
            'time':datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        })
    else:
        return redirect('user_app:login',)

##更新员工信息页面显示
def updateEmp(request):
    if request.session.get('a') == 'ok':
        #获取更改员工id
        id=request.GET.get('id')
        number = request.GET.get('number')
        print(number)
        request.session['num']=number
        emp=Employee.objects.filter(id=id)
        #保存员工id
        request.session['id']=id
        print(emp)
        return render(request,'emplist_app/updateEmp.html',{
            'emp':emp[0],
            'time': datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        })
    else:
        return redirect('user_app:login',)
##更新员工信息处理逻辑
def updateEmplogic(request):
    try:
        with transaction.atomic():
            #获取到保存的id值
            id=request.session.get('id')
            name=request.POST.get('name')
            salary=request.POST.get('salary')
            age=request.POST.get('age')
            result=Employee.objects.get(id=id)

            if not name:
                name=result.name
            if not salary:
                salary=result.salary
            if not age:
                age=result.age
                ##获取图片
            headpic = request.FILES.get('file', 'ok')
            if headpic== 'ok':
                headpic=result.headpic
            else:
                ext = os.path.splitext(headpic.name)
                headpic.name = str(uuid.uuid4()) + ext[1]
            ##获取图片后缀
            ##修改图片名字为随机32位数字
            print(id, name, headpic, salary, age)
            result.name=name
            result.headpic=headpic
            result.salary=salary
            result.age=age
            result.save()
            return redirect('emplist_app:emp')
    except Exception as e:
        print(e)
        return HttpResponse('修改失败！')

# 删除员工信息
def delEmp(request):
    id=request.GET.get('id')
    number = request.GET.get('number')
    print(number)
    request.session['num'] = number
    print(id)
    Employee.objects.get(id=id).delete()
    return redirect('emplist_app:emp')

#添加员工信息页面显示
def addEmployee(request):
    if request.session.get('a') == 'ok':

        return render(request,'emplist_app/addEmp.html',{
            'time': datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        })
    else:
        return redirect('user_app:login', )

# 添加员工信息处理逻辑
def addEmplogic(request):
    try:
        with transaction.atomic():
            name=request.POST.get('name')
            #获取上传文件
            headpic=request.FILES.get('file')
            #获取上传文件后缀
            ext=os.path.splitext(headpic.name)
            #修改文件名,uuid模块下的uuid（4），可以产生32位为随机数字，可以保证文件名不重复
            headpic.name=str(uuid.uuid4())+ext[1]
            salary=request.POST.get('salary')
            age=request.POST.get('age')
            print(name,headpic,salary,age)
            result=Employee.objects.create(name=name,age=age,salary=salary,headpic=headpic)
            if result:
                request.session['num'] = 'add'
                return redirect('emplist_app:emp')
            return HttpResponse('添加失败！')
    except Exception as e:
        print(e)
        return  HttpResponse('添加失败！')