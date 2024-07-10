from django.db import models
from user_reg.models import User
# Create your models here.

class ClinicBill(models.Model):
    clinicbill_id = models.AutoField(primary_key=True)
    bill = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    # user_id = models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=45)



    class Meta:
        managed = False
        db_table = 'clinic_bill'
