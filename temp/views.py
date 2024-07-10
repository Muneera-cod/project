from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'temp/home.html')

def clinic(request):
    return render(request,'temp/clinc.html')

def doctor(request):
    return render(request,'temp/doctor.html')

def pharmacy(request):
    return render(request,'temp/pharmacy.html')

def staff(request):
    return render(request,'temp/staff.html')

def user(request):
    return render(request,'temp/user.html')