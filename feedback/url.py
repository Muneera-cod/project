from django.conf.urls import url
from feedback import views

urlpatterns = [
    url('post_feedback/',views.add_feedback),
    url('view_feed_clinic/',views.view_feedback_clinic),
    url('doctor_view/',views.view_feed_docttor)

]