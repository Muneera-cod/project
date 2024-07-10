from django.shortcuts import render
from clinic_bill.models import ClinicBill
from django.core.files.storage import FileSystemStorage
from user_reg.models import User
import datetime
# Create your views here.

def add_clinic_bill(request):
    obb=User.objects.all()
    context={
        'y':obb
    }
    if request.method=='POST':
        obj=ClinicBill()
        myfile=request.FILES['bill']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.bill=myfile.name
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.user_id=request.POST.get('pr')
        obj.status='Pending'
        obj.save()
    return render(request,'clinic_bill/add_clinic_bill.html',context)


def manage_clinic_bill(request):
    obj = ClinicBill.objects.all()
    context = {
        'x': obj
    }
    return render(request,'clinic_bill/manage_clinic_bill.html',context)


def view_clinic_bill(request):
    ss=request.session['uid']
    obj = ClinicBill.objects.filter(user_id=ss)
    context = {
        'x': obj
    }
    return render(request,'clinic_bill/view_clinic_bill.html',context)

def view_report(request):
    obj = ClinicBill.objects.all()
    context = {
        'x': obj
    }
    return render(request,'clinic_bill/view_clinic_bill_report.html',context)
