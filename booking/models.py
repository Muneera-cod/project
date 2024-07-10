from django.db import models
from doctor_schedule.models import DoctorSchedule
from user_reg.models import User
# Create your models here.

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    # schedule_id = models.IntegerField()
    schedule=models.ForeignKey(DoctorSchedule,on_delete=models.CASCADE)
    booking_time = models.TimeField()
    status = models.CharField(max_length=45)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'booking'