from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=45)
    age = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    experience = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    specialization = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'doctor'

