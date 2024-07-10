from django.conf.urls import url
from prescription import views

urlpatterns = [
    url('add_prescription/',views.add_prescription),
    url('vw_pres_user/',views.view_prescription_user),
    url('pharmacy_view/',views.view_prescription_pharmacy),
    url('manage/',views.manage),
    url('update/(?P<idd>\w+)',views.update),
    url('delete/(?P<idd>\w+)',views.delete)

]