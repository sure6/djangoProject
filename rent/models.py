
from django.db import models
from django.db.models import AutoField, CharField, IntegerField, DateTimeField,DateField


# Create your models here.
class RentModel(models.Model):
    id=AutoField(primary_key=True)
    first_name=CharField(max_length=100)
    last_name=CharField(max_length=100)
    age=IntegerField(default=0)
    gender=CharField(default="male",null=False, max_length=20)
    create_time = DateTimeField(auto_now_add=True)
    create_user = CharField(max_length=100)
    update_time = DateTimeField(auto_now=True)
    update_user = CharField(max_length=100)
    is_deleted = IntegerField(default=0)

class Bill(models.Model):
    id=models.AutoField(primary_key=True)
    start_date=models.DateField(verbose_name="start_date")
    due_date=models.DateField(verbose_name="end_date")
    fee_aud=models.DecimalField(verbose_name="fee_aud",max_digits=7, decimal_places=2)
    fee_rmb=models.DecimalField(verbose_name="fee_rmb",max_digits=7, decimal_places=2)
    payment_date=models.DateField(verbose_name="payment_date")
    comments=models.CharField(null=True, max_length=1000, blank=True)
    create_time = DateTimeField(auto_now_add=True)
    create_user = CharField(max_length=100)
    update_time = DateTimeField(auto_now=True)
    update_user = CharField(max_length=100)
    is_deleted = IntegerField(default=0)






