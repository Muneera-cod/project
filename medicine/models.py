from django.db import models

# Create your models here.

class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    med_name = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    quantity = models.CharField(max_length=45)



    class Meta:
        managed = False
        db_table = 'medicine'


