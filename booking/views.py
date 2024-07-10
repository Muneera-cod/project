from django.http import HttpResponseRedirect
from django.shortcuts import render
from booking.models import Booking

# Create your views here.


def book_appointment(request,idd):
    ss=request.session['uid']
    if request.method=='POST':
        l=0
        if Booking.objects.filter(status='Accepted', schedule_id=idd).exists():
            ob=Booking.objects.filter(status='Accepted', schedule_id=idd)
            l=len(ob)
            print(l)
        if l>30:
            message="Booking limit is exceeded"
            context={
                'msg':message
            }
            return render(request, 'booking/book_appointment.html',context)
        else:
            obj=Booking()
            obj.schedule_id=idd
            obj.user_id=ss
            obj.booking_time=request.POST.get('btime')
            obj.status='pending'
            obj.save()
            return HttpResponseRedirect('/payment/payment/'+str(obj.booking_id))
    return render(request,'booking/book_appointment.html')


def manage_app_staff(request):
    obj=Booking.objects.all()
    context={
        'x':obj
    }
    return render(request,'booking/manage_app_staff.html',context)

def approve(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    l = 0
    if Booking.objects.filter(status='Accepted', schedule_id=obj.schedule_id).exists():
        ob = Booking.objects.filter(status='Accepted', schedule_id=obj.schedule_id)
        l = len(ob)
        print(l)
    if l > 30:
        message = "Booking limit is exceeded"
        obj = Booking.objects.all()
        context = {
            'x': obj,
            'msg': message
        }
        return render(request, 'booking/manage_app_staff.html', context)
    else:
        obj.status='Accepted'
        obj.save()
        return manage_app_staff(request)

def reject(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.status='Rejected'
    obj.save()
    return manage_app_staff(request)


def view_appp_dentist(request):
    ss = request.session['uid']
    obj = Booking.objects.filter(schedule__doctor_id=ss)
    context = {
        'x': obj
    }
    return render(request,'booking/view_appointment_dentist.html',context)


def view_app_status(request):
    ss = request.session['uid']
    obj = Booking.objects.filter(user_id=ss)
    context = {
        'x': obj
    }
    return render(request,'booking/view_appointment_status.html',context)