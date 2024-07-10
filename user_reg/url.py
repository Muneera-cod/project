from django.conf.urls import url
from user_reg import views

urlpatterns = [
    url('register/',views.register),
    url('update/(?P<idd>\w+)',views.update_profile),
    url('view_profile/',views.view_profile)
]

