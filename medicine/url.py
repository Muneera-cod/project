from django.conf.urls import url
from medicine import views

urlpatterns=[
    url('add_med/',views.add_med),
    url('vw_medicine/',views.view_med),
    url('manage/',views.manage),
    url('update/(?P<idd>\w+)',views.update),
    url('dlll/(?P<idd>\w+)', views.dlt)
]