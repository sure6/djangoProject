from django.test import TestCase
import datetime

# Create your tests here.
if __name__=="__main__":
    print(datetime.date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day))
    print(datetime.date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day).strftime("%A"))