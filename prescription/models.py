from django.db import models
from user_reg.models import User
from doctor.models import Doctor
# Create your models here.

class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # doctor_id = models.IntegerField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    prescription = models.CharField(max_length=450)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'prescription'

