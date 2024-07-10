from django.conf.urls import url
from payment import views

urlpatterns = [
    url('payment/(?P<idd>\w+)',views.payment),
    url('pharmasist_vw/',views.view_pay_pharmasist),
    url('staff_view/',views.view_pay_staff),
    url('status/',views.view_payment_sts),
    url('pharmacy_bill/(?P<idd>\w+)',views.pharmacy_bill),
    url('clinic_pay/(?P<idd>\w+)',views.clinic_bill)

]