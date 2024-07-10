from django.db import models

# Create your models here.

class Pharmacy(models.Model):
    pharmacy_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'pharmacy'
