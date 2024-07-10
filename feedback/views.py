from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.

def add_feedback(request):
    ss = request.session['uid']
    if request.method=='POST':
        obj=Feedback()
        obj.user_id=ss
        obj.feedback=request.POST.get('feedback')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.save()
    return render(request,'feedback/add_feedback.html')


def view_feedback_clinic(request):
    obj = Feedback.objects.all()
    context = {
        'x': obj
    }
    return render(request,'feedback/view_feedback_clinic.html',context)


def view_feed_docttor(request):
    obj = Feedback.objects.all()
    context = {
        'x': obj
    }
    return render(request,'feedback/view_feedback_doctor.html',context)

