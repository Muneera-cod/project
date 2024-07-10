from django.db import models
from pharmacy.models import Pharmacy
from user_reg.models import User
from prescription.models import Prescription
from medicine.models import Medicine
# Create your models here.

class PharmacyBill(models.Model):
    phbill_id = models.AutoField(primary_key=True)
    # pharmacy_id = models.IntegerField()
    pharmacy=models.ForeignKey(Pharmacy,on_delete=models.CASCADE)
    # medicine_id = models.IntegerField()
    medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    qty = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    # prescription_id = models.IntegerField()
    prescription=models.ForeignKey(Prescription,on_delete=models.CASCADE)
    status = models.CharField(max_length=45,null=True)

    class Meta:
        managed = False
        db_table = 'pharmacy_bill'


