from django.db import models
from booking.models import Booking
from pharmacy_bill.models import PharmacyBill
from user_reg.models import User
from clinic_bill.models import ClinicBill
# Create your models here.


class Payment(models.Model):
    payment = models.AutoField(primary_key=True)
    # booking_id = models.IntegerField()
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    cardholdername = models.CharField(max_length=45)
    acc_no = models.CharField(max_length=45)
    cvv = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'payment'


class PharmacyPayment(models.Model):
    phpayment_id = models.AutoField(primary_key=True)
    # phbill_id = models.IntegerField()
    phbill=models.ForeignKey(PharmacyBill,on_delete=models.CASCADE)
    amount = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'pharmacy_payment'

class ClinicPay(models.Model):
    clinic_pay = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=45)
    # clinicbill_id = models.IntegerField()
    clinicbill=models.ForeignKey(ClinicBill,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'clinic_pay'


