from django.conf.urls import url
from temp import views

urlpatterns=[
    url('home/',views.home),
    url('clinic/',views.clinic),
    url('staff/',views.staff),
    url('pharmacy/',views.pharmacy),
    url('user/',views.user),
    url('doctor/',views.doctor)
]