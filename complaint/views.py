from django.shortcuts import render
from complaint.models import Complaint
from doctor.models import Doctor
import datetime
# Create your views here.

def complaint(request):
    ss = request.session['uid']
    ob=Doctor.objects.all()
    context={
        'x':ob
    }
    if request.method=='POST':
        obj=Complaint()
        obj.user_id=ss
        obj.doctor_id=request.POST.get('dname')
        obj.complaint=request.POST.get('com')
        obj.reply='pending'
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.save()
    return render(request,'complaint/add_complaint.html',context)


def view_complaint(request):
    obj = Complaint.objects.all()
    context = {
        'x': obj
    }
    return render(request,'complaint/view_complaint.html',context)

def post_reply(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('rpy')
        obj.save()
        return view_complaint(request)
    return render(request,'complaint/post_reply.html')


def view_reply(request):
    ss = request.session['uid']
    obj = Complaint.objects.filter(user_id=ss)
    context = {
        'x': obj
    }
    return render(request,'complaint/view_reply.html',context)