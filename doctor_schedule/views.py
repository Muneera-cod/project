from django.shortcuts import render
from doctor_schedule.models import DoctorSchedule
from doctor.models import Doctor
import datetime
# Create your views here.

def add_doc_schedule(request):
    ob=Doctor.objects.all()
    context={
        'x':ob
    }
    if request.method=='POST':
        obj=DoctorSchedule()
        obj.doctor_id=request.POST.get('dname')
        obj.start_time=request.POST.get('stime')
        obj.end_time=request.POST.get('etime')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.save()
        return render(request, 'temp/clinc.html')
    return render(request,'doctor_schedule/add_doctor_schedule.html',context)


def manage_doc_schedule(request):
    obj = DoctorSchedule.objects.all()
    context = {
        'x': obj
    }
    return render(request,'doctor_schedule/manage_doctor_schedule.html',context)

def delete(request,idd):
    obj=DoctorSchedule.objects.get(schedule_id=idd)
    obj.delete()
    return manage_doc_schedule(request)


def view_doc_schedule_doctor(request):
    ss = request.session['uid']
    obj = DoctorSchedule.objects.filter(doctor_id=ss)
    context = {
        'x': obj
    }
    return render(request,'doctor_schedule/view_doctor_schedule_doc.html',context)


def view_doc_schedule_user(request):
    obj = DoctorSchedule.objects.all()
    context = {
        'x': obj
    }
    return render(request,'doctor_schedule/view_doctor_schedule_and_book.html',context)
