"""dental_clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from temp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('booking/',include('booking.url')),
    url('chat/',include('chat.url')),
    url('clinic_bill/',include('clinic_bill.url')),
    url('complaint/',include('complaint.url')),
    url('doctor/',include('doctor.url')),
    url('doctor_schedule/',include('doctor_schedule.url')),
    url('feedback/',include('feedback.url')),
    url('login/',include('login.url')),
    url('payment/',include('payment.url')),
    url('pharmacy/',include('pharmacy.url')),
    url('pharmacy_bill/',include('pharmacy_bill.url')),
    url('prescription/',include('prescription.url')),
    url('staff_reg/',include('staff.url')),
    url('user_reg/',include('user_reg.url')),
    url('medicine/',include('medicine.url')),
    url('temp/',include('temp.url')),
    url('report/',include('report.url')),
    url('$',views.home)
]
