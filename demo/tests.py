import time,datetime

from django.test import TestCase

# Create your tests here.
if __name__=="__main__":

    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # print(type(datetime.datetime.now()))
    print(type(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
