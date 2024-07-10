from django.shortcuts import render
from medicine.models import Medicine
# Create your views here.

def add_med(request):
    if request.method=='POST':
        obj=Medicine()
        obj.med_name=request.POST.get('medname')
        obj.price=request.POST.get('price')
        obj.quantity=request.POST.get('qu')
        obj.save()
    return render(request,'medicine/add_medcine.html')

def view_med(request):
    if request.method=='POST':
        vv=request.POST.get('lop')
        obj = Medicine.objects.filter(med_name__contains=vv)
        context = {
            'x': obj
        }
        return render(request, 'medicine/view_medicine.html', context)
    else:
        obj=Medicine.objects.all()
        context={
            'x':obj
        }
    return render(request,'medicine/view_medicine.html',context)

def manage(request):
    obj = Medicine.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'medicine/manage_medicine.html', context)


def dlt(request,idd):
    obj=Medicine.objects.get(medicine_id=idd)
    obj.delete()
    return manage(request)

def update(request,idd):
    obj = Medicine.objects.get(medicine_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=Medicine.objects.get(medicine_id=idd)
        obj.med_name=request.POST.get('medname')
        obj.price=request.POST.get('price')
        obj.save()
        return manage(request)
    return render(request, 'medicine/update.html', context)


