from django.conf.urls import url
from doctor_schedule import views

urlpatterns = [
    url('add_doc_schedule/',views.add_doc_schedule),
    url('manage/',views.manage_doc_schedule),
    url('view_and_book/',views.view_doc_schedule_user),
    url('doctor_vw/',views.view_doc_schedule_doctor),
    url('delete/(?P<idd>\w+)',views.delete)

]