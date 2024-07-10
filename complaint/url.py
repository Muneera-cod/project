from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('complaint/',views.complaint),
    url('view/',views.view_complaint),
    url('post_reply/(?P<idd>\w+)',views.post_reply),
    url('view_reply/',views.view_reply)

]