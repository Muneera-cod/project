from django.shortcuts import render
from user_reg.models import User
from login.models import Login
# Create your views here.

def register(request):
    # obk=""
    if request.method=='POST':
        obj=User()
        obj.name=request.POST.get('dname')
        obj.age=request.POST.get('age')
        obj.gender=request.POST.get('gen')
        obj.place=request.POST.get('place')
        obj.email=request.POST.get('email')
        obj.phn_no=request.POST.get('phone')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('pass')
        obj.save()
        ob = Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.type = 'user'
        ob.uid = obj.user_id
        ob.save()
    #     obk="k"
    #
    # context={
    #     'x':obk
    # }
    return render(request,'user_reg/register.html')

def update_profile(request,idd):
    obj = User.objects.get(user_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=User.objects.get(user_id=idd)
        obj.name=request.POST.get('dname')
        obj.age=request.POST.get('age')
        obj.place=request.POST.get('place')
        obj.email=request.POST.get('email')
        obj.phn_no=request.POST.get('phone')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('pass')
        obj.save()
        return view_profile(request)
    return render(request,'user_reg/update_profile.html',context)

def view_profile(request):
    ss = request.session['uid']
    obj = User.objects.filter(user_id=ss)
    context = {
        'x': obj
    }
    return render(request,'user_reg/view_profile.html',context)
