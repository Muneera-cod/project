from django.conf.urls import url
from doctor import views

urlpatterns = [

    url('register/',views.register),
    url('manage_doctor/',views.manage),
    url('update_profile/(?P<idd>\w+)',views.update),
    url('view/',views.view_profile),
    url('delete/(?P<idd>\w+)',views.delete),
    url('abcd/(?P<idd>\w+)',views.cl_up)

]