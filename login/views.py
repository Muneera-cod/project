from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login
# Create your views here.


def login(request):
    if request.method == "POST":
        name = request.POST.get('unmae')
        pasw = request.POST.get('psw')
        obj = Login.objects.filter(username=name, password=pasw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.uid
            if tp == "clinic":
                request.session['uid'] = uid
                return HttpResponseRedirect('/temp/clinic/')
            elif tp == "staff":
                request.session['uid'] = uid
                return HttpResponseRedirect('/temp/staff/')
            elif tp == "doctor":
                request.session['uid'] = uid
                return HttpResponseRedirect('/temp/doctor/')
            elif tp == "user":
                request.session['uid'] = uid
                return HttpResponseRedirect('/temp/user/')
            elif tp == "pharmacy":
                request.session['uid'] = uid
                return HttpResponseRedirect('/temp/pharmacy/')
        else:
            objlist = "incorected username or password... please try again..."
            context = {
                'msg': objlist,
            }
            return render(request, 'login/login.html', context)
    return render(request,'login/login.html')
