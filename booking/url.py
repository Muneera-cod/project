from django.conf.urls import url
from booking import views

urlpatterns=[
    url('booking/(?P<idd>\w+)',views.book_appointment),
    url('manage_book/',views.manage_app_staff),
    url('view_app_sts/',views.view_app_status),
    url('dentist_vw/',views.view_appp_dentist),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject)

]