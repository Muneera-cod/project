from django.conf.urls import url
from pharmacy_bill import views

urlpatterns = [
    url('add_bill/(?P<idd>\w+)',views.add_ph_bill),
    url('manage/',views.manage_bill),
    url('view_bill_user/',views.view_bill_user),
    url('report_vw/',views.view_bill_report),
    url('update/(?P<idd>\w+)',views.update),
    url('delete/(?P<idd>\w+)',views.delete)

]