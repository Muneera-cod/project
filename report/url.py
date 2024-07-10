from django.conf.urls import url
from report import views

urlpatterns=[
    url('report2/',views.cust_pdt_order_report),
    url('report1/', views.pharmacy_report),
    url('report3/', views.clinic_report),
]