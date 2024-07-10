from django.shortcuts import render
from pharmacy_bill.models import PharmacyBill
import datetime
from prescription.models import Prescription
from django.core.files.storage import FileSystemStorage
# Create your views here.

def add_ph_bill(request,idd):
    ss = request.session['uid']
    obb=Prescription.objects.all()
    context={
        'y':obb
    }
    if request.method=='POST':
        obj=PharmacyBill()
        obj.pharmacy_id=ss
        obj.prescription_id=request.POST.get('pr')
        obj.medicine_id=idd
        obj.qty=request.POST.get('qty')
        obj.amount=request.POST.get('amnt')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.save()
    return render(request,'pharmacy_bill/add_pharmacy_bill.html', context)


def manage_bill(request):
    ss = request.session['uid']
    obj = PharmacyBill.objects.filter(pharmacy_id=ss)
    context = {
        'x': obj
    }
    return render(request,'pharmacy_bill/manage_pharmacy_bill.html',context)

def update(request,idd):
    obj = PharmacyBill.objects.get(phbill_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=PharmacyBill.objects.get(phbill_id=idd)
        obj.pharmacy_id = 1
        obj.prescription_id = 1
        obj.medicine_id = 1
        obj.qty = request.POST.get('qty')
        obj.amount = request.POST.get('amnt')
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.today()
        obj.save()
        return manage_bill(request)
    return render(request,'pharmacy_bill/update.html',context)

def delete(request,idd):
    obj=PharmacyBill.objects.get(phbill_id=idd)
    obj.delete()
    return manage_bill(request)


def view_bill_report(request):
    obj = PharmacyBill.objects.all()
    context = {
        'x': obj
    }
    return render(request,'pharmacy_bill/view_bill_report_clinic.html',context)


def view_bill_user(request):
    ss = request.session['uid']
    obj = PharmacyBill.objects.filter(prescription__user_id=ss)
    context = {
        'x': obj
    }
    return render(request,'pharmacy_bill/view_bill_user.html',context)
