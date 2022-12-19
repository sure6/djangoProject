import time

from django.db import models
from django.db.models import AutoField, CharField, IntegerField, DateTimeField


# Create your models here.
class DemoModel(models.Model):
    id=AutoField(primary_key=True)
    first_name=CharField(max_length=100)
    last_name=CharField(max_length=100)
    age=IntegerField(default=0)
    gender=CharField(default="male",null=False, max_length=20)
    create_time = DateTimeField(default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    create_user = CharField(max_length=100)
    update_time = DateTimeField(default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    update_user = CharField(max_length=100)
    is_deleted = IntegerField(default=0)







