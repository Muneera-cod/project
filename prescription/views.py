from django.shortcuts import render
from prescription.models import Prescription
from django.core.files.storage import FileSystemStorage
import datetime
from user_reg.models import User
# Create your views here.

def add_prescription(request):
    ss=request.session['uid']
    ob=User.objects.all()
    context={
        'x':ob
    }
    if request.method=='POST':
        obj=Prescription()
        obj.user_id=request.POST.get('uname')
        obj.doctor_id=ss
        myfile=request.FILES['pres']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.prescription=myfile.name
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.save()
    return render(request,'prescription/add_prescription.html',context)


def manage(request):
    obj = Prescription.objects.all()
    context = {
        'x': obj
    }
    return render(request,'prescription/manage.html',context)

def update(request,idd):
    ss=request.session['uid']
    obj = Prescription.objects.get(prescription_id=idd)
    context = {
        'x': obj
    }
    if request.method == 'POST':
        obj = Prescription.objects.get(prescription_id=idd)
        obj.user_id = 1
        obj.doctor_id = ss
        myfile = request.FILES['pres']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.prescription = myfile.name
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.today()
        obj.save()
        return manage(request)
    return render(request,'prescription/update.html',context)

def delete(request,idd):
    obj=Prescription.objects.get(prescription_id=idd)
    obj.delete()
    return manage(request)




def view_prescription_user(request):
    ss = request.session['uid']
    obj = Prescription.objects.filter(user_id=ss)
    context = {
        'x': obj
    }
    return render(request,'prescription/view_user.html',context)



def view_prescription_pharmacy(request):
    obj = Prescription.objects.all()
    context = {
        'x': obj
    }
    return render(request,'prescription/view_prescription_pharmacy.html',context)
