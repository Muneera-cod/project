from django.conf.urls import url
from pharmacy import views

urlpatterns = [
    url('register/',views.register),
    url('manage/',views.manage),
    url('update/(?P<idd>\w+)',views.update),
    url('delete/(?P<idd>\w+)',views.delete)

]