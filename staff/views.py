from django.shortcuts import render
from staff.models import Staff
from login.models import Login
# Create your views here.

def register(request):
    if request.method=='POST':
        obj=Staff()
        obj.name=request.POST.get('dname')
        obj.age=request.POST.get('age')
        obj.gender=request.POST.get('gen')
        obj.place=request.POST.get('place')
        obj.email=request.POST.get('email')
        obj.phone_no=request.POST.get('phone')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('pass')
        obj.save()
        ob = Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.type = 'staff'
        ob.uid = obj.staff_id
        ob.save()
        return render(request, 'temp/clinc.html')
    return render(request,'staff/register_staff.html')

def manage_staff(request):
    obj = Staff.objects.all()
    context = {
        'x': obj
    }
    return render(request,'staff/manage_staff.html',context)

def delete(request,idd):
    obj=Staff.objects.get(staff_id=idd)
    obj.delete()
    message = "successfully deleted"
    obj = Staff.objects.all()
    context = {
        'x': obj,
        'msg': message
    }
    return render(request, 'staff/manage_staff.html', context)



def view_profile(request):
    ss = request.session['uid']
    obj = Staff.objects.filter(staff_id=ss)
    context = {
        'x': obj
    }
    return render(request,'staff/view_profile.html',context)


def update(request,idd):
    obj = Staff.objects.get(staff_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=Staff.objects.get(staff_id=idd)
        obj.name=request.POST.get('dname')
        obj.age=request.POST.get('age')
        obj.place=request.POST.get('place')
        obj.email=request.POST.get('email')
        obj.phone_no=request.POST.get('phone')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('pass')
        obj.save()
        return view_profile(request)
    return render(request,'staff/update_profile.html',context)
