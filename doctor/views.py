from django.shortcuts import render
from doctor.models import Doctor
from login.models import Login

# Create your views here.

def register(request):
    if request.method=='POST':
        obj=Doctor()
        obj.dname=request.POST.get('dname')
        obj.age=request.POST.get('age')
        obj.gender=request.POST.get('gen')
        obj.experience=request.POST.get('exp')
        obj.place=request.POST.get('place')
        obj.specialization=request.POST.get('spec')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('pass')
        obj.save()
        ob=Login()
        ob.username=obj.username
        ob.password=obj.password
        ob.type='doctor'
        ob.uid=obj.doctor_id
        ob.save()
    return render(request,'doctor/register_doctor.html')


def manage(request):
    obj=Doctor.objects.all()
    context={
        'x':obj
    }
    return render(request,'doctor/manage_doctor.html',context)

def delete(request,idd):
    obj=Doctor.objects.get(doctor_id=idd)
    obj.delete()
    return manage(request)


def view_profile(request):
    ss = request.session['uid']
    obj = Doctor.objects.filter(doctor_id=ss)
    context = {
        'x': obj
    }
    return render(request,'doctor/view_profil.html',context)


def update(request,idd):
    obj = Doctor.objects.get(doctor_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=Doctor.objects.get(doctor_id=idd)
        obj.dname=request.POST.get('dname')
        obj.age=request.POST.get('age')
        obj.experience=request.POST.get('exp')
        obj.place=request.POST.get('place')
        obj.specialization=request.POST.get('spec')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('pass')
        obj.save()
        return view_profile(request)
    return render(request,'doctor/update_profile.html',context)

def cl_up(request,idd):
    obj = Doctor.objects.get(doctor_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=Doctor.objects.get(doctor_id=idd)
        obj.dname=request.POST.get('dname')
        obj.age=request.POST.get('age')
        obj.experience=request.POST.get('exp')
        obj.place=request.POST.get('place')
        obj.specialization=request.POST.get('spec')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('pass')
        obj.save()
        return manage(request)
    return render(request,'doctor/update_doctor.html',context)

