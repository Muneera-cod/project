from django.db import models
from doctor.models import Doctor

# Create your models here.

class DoctorSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    # doctor_id = models.IntegerField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    start_time = models.TimeField()
    date = models.DateField()
    time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'doctor_schedule'
