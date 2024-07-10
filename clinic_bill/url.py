from django.conf.urls import url
from clinic_bill import views

urlpatterns = [
    url('add_bill/',views.add_clinic_bill),
    url('manage_bill/',views.manage_clinic_bill),
    url('view_bill/',views.view_clinic_bill),
    url('report/',views.view_report)

]