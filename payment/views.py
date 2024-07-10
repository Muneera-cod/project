from django.shortcuts import render
from payment.models import Payment
from payment.models import ClinicPay
from payment.models import PharmacyPayment
from pharmacy_bill.models import PharmacyBill
from clinic_bill.models import ClinicBill
from user_reg.models import User
from django.http import HttpResponseRedirect
import datetime
# Create your views here.

def payment(request,idd):
    if request.method=='POST':
        obj=Payment()
        obj.booking_id=idd
        obj.cardholdername=1
        obj.acc_no=1
        obj.cvv=1
        obj.date=datetime.datetime.today()
        obj.amount=request.POST.get('amount')
        obj.status='paid'
        obj.save()
    return render(request,'payment/payment.html')

def pharmacy_bill(request,idd):
    # ss = request.session['uid']
    if PharmacyPayment.objects.filter(phbill_id=idd).exists():
        message = "Already Paid"
        ss = request.session['uid']
        obj = PharmacyBill.objects.filter(pharmacy_id=ss)
        context = {
            'x': obj,
            'msg': message
        }
        return render(request, 'pharmacy_bill/manage_pharmacy_bill.html', context)

    ob=PharmacyBill.objects.get(phbill_id=idd)
    obb = User.objects.all()
    context={
        'x':ob,
        'y': obb
    }
    if request.method=='POST':
        obj=PharmacyPayment()
        obj.phbill_id=idd
        obj.user_id=request.POST.get('dname')
        obj.amount=request.POST.get('amnt')
        obj.status='paid'
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.save()
        ob.status='paid'
        ob.save()
        ss = request.session['uid']
        obj = PharmacyBill.objects.filter(pharmacy_id=ss)
        context = {
            'x': obj
        }
        return render(request, 'pharmacy_bill/manage_pharmacy_bill.html', context)
    return render(request,'payment/pharmacy_bill.html',context)

def clinic_bill(request,idd):
    ss = request.session['uid']
    ob=ClinicBill.objects.get(clinicbill_id=idd)

    context={
        'y':ob
    }
    if request.method=='POST':
        obj=ClinicPay()
        obj.user_id=request.POST.get('dname')
        obj.clinicbill_id=idd
        obj.amount=request.POST.get('amnt')
        obj.status='paid'
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.save()

        ob=ClinicBill.objects.get(clinicbill_id=idd)
        ob.status='paid'
        ob.save()
        return HttpResponseRedirect('/temp/staff/')
    return render(request,'payment/clinic_pay.html', context)

def view_pay_pharmasist(request):
    ss = request.session['uid']
    obj = PharmacyPayment.objects.filter(phbill__pharmacy_id=ss)
    context = {
        'x': obj
    }
    return render(request,'payment/view_payment_pharmaist.html',context)

def view_pay_staff(request):
    obj = ClinicPay.objects.all()
    context = {
        'x': obj
    }
    return render(request,'payment/view_payment_staff.html',context)

def view_payment_sts(request):
    ss = request.session['uid']
    obj = Payment.objects.filter(booking__user_id=ss)
    context = {
        'x': obj
    }
    return render(request,'payment/view_payment_status_user.html',context)


