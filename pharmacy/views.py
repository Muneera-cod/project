from django.shortcuts import render
from pharmacy.models import Pharmacy
from login.models import Login
# Create your views here.

def register(request):
    if request.method=='POST':
        obj=Pharmacy()
        obj.name=request.POST.get('name')
        obj.place=request.POST.get('place')
        obj.phone=request.POST.get('phone')
        obj.pincode=request.POST.get('pin')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('pass')
        obj.save()
        ob = Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.type = 'pharmacy'
        ob.uid = obj.pharmacy_id
        ob.save()
    return render(request,'pharmacy/register_pharmasist.html')

def manage(request):
    obj = Pharmacy.objects.all()
    context = {
        'x': obj
    }
    return render(request,'pharmacy/manage_pharmacy.html',context)

def update(request,idd):
    obj=Pharmacy.objects.get(pharmacy_id=idd)
    context={
        'x':obj
    }
    if request.method=='POST':
        obj=Pharmacy.objects.get(pharmacy_id=idd)
        obj.name=request.POST.get('name')
        obj.place=request.POST.get('place')
        obj.phone=request.POST.get('phone')
        obj.pincode=request.POST.get('pin')
        obj.save()
        return manage(request)
    return render(request,'pharmacy/update.html',context)

def delete(request,idd):
    obj=Pharmacy.objects.get(pharmacy_id=idd)
    obj.delete()
    return manage(request)
