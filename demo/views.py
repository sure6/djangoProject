import time

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from demo.models import DemoModel


# Create your views here.
def index(request):
    demos = DemoModel.objects.filter(is_deleted=0).values()
    return render(request, "demo/demo.html", {"demos": demos,"titleName":"demo", "context":"index"})

def addInfo(request):
    return render(request, "demo/demo.html",{"titleName":"add info", "context":"addinfo"})

def saveInfo(request):
    info = {}
    for para in request.POST:
        info.setdefault(para, request.POST[para])
    if info['id'] == "":
        demo = DemoModel(first_name=info["first_name"], last_name=info["last_name"], age=info["age"], gender=info["gender"],
                         create_user="zhangsan", update_user="zhangsan")
        demo.save()
    else:
        demo = DemoModel.objects.get(id=info['id'])
        demo.first_name=info["first_name"]
        demo.last_name=info["last_name"]
        demo.age=info["age"]
        demo.gender=info["gender"]
        demo.update_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        demo.update_user=demo.first_name+demo.last_name
        demo.save()
    return HttpResponseRedirect(reverse("demo:demo"))

def deteteinfo(request, id):
    demo=DemoModel.objects.get(id=id)
    demo.is_deleted=1
    demo.save()
    return HttpResponseRedirect(reverse("demo:demo"))

def updateInfo(request,id):
    demo=DemoModel.objects.get(id=id)
    context={"demo": demo,"titleName":"update info", "context":"updateinfo"}
    return  render(request, "demo/demo.html", context)
