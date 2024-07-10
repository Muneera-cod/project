from django.conf.urls import url
from staff import views

urlpatterns = [
    url('register/',views.register),
    url('manage/',views.manage_staff),
    url('profile/',views.view_profile),
    url('delete/(?P<idd>\w+)',views.delete),
    url('update/(?P<idd>\w+)',views.update)

]