from django.db import models
from django.db.models import AutoField, CharField, IntegerField, DateTimeField,DateField
import datetime

# Create your models here.
class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=100,default="leesure")
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=100,default="leesure")
    is_deleted = models.IntegerField(default=0)

    class Meta:
        abstract=True


class WorkModel(BaseModel):
    work_id = models.AutoField(primary_key=True)
    work_date = models.DateField()
    work_weekday = models.CharField(choices=[("Mon","Mondy"),("Tue","Tuesday"),("Wed","Wednesday"),("Thu","Thuresday"),("Fri","Friday"),("Sat","Saturday"),("Sun","Sunday")],max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    work_hour = models.FloatField()
    comments = models.CharField(null=True, max_length=1000, blank=True)

    # @property
    # def work_weekday(self):
    #     return self.work_weekday
    
    # @work_weekday.setter
    # def work_weekday(self,work_date):
    #     self.work_weekday = datetime.date(self.work_date.year,self.work_date.month,self.work_date.day).strftime("%A")