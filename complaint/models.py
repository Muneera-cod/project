from django.db import models
from doctor.models import Doctor
from user_reg.models import User
# Create your models here.

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # doctor_id = models.IntegerField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    complaint = models.CharField(max_length=45)
    reply = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'complaint'

