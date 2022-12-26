import time

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from rent.models import RentModel,Bill


# Create your views here.
def index(request):
    rents = RentModel.objects.filter(is_deleted=0).values()
    return render(request, "rent/index.html", {"rents": rents,"titleName":"rent", "context":"home"})

def bill(request):
    bills = Bill.objects.filter(is_deleted=0).values()
    return render(request, "rent/bill.html", {"bills": bills,"titleName":"bill"})

def addInfo(request):
    return render(request, "rent/index.html",{"titleName":"add info", "context":"addinfo"})

def saveInfo(request):
    info = {}
    for para in request.POST:
        info.setdefault(para, request.POST[para])
    if info['id'] == "":
        rent = RentModel(first_name=info["first_name"], last_name=info["last_name"], age=info["age"], gender=info["gender"],
                         create_user="zhangsan", update_user="zhangsan")
        rent.save()
    else:
        rent = RentModel.objects.get(id=info['id'])
        rent.first_name=info["first_name"]
        rent.last_name=info["last_name"]
        rent.age=info["age"]
        rent.gender=info["gender"]
        rent.update_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        rent.update_user=rent.first_name+rent.last_name
        rent.save()
    return HttpResponseRedirect(reverse("rent:rent"))

def deteteinfo(request, id):
    rent=RentModel.objects.get(id=id)
    rent.is_deleted=1
    rent.save()
    return HttpResponseRedirect(reverse("rent:rent"))

def updateInfo(request,id):
    rent=RentModel.objects.get(id=id)
    context={"rent": rent,"titleName":"update info", "context":"updateinfo"}
    return  render(request, "rent/index.html", context)
