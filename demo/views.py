import time

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from demo.models import DemoModel


# Create your views here.
def index(request):
    demos = DemoModel.objects.all().values()
    return render(request, "demo/demo.html", {"demos": demos})

def addInfo(request):
    return render(request, "demo/addInfo.html")

def saveInfo(request):
    info = {}
    for para in request.POST:
        info.setdefault(para, request.POST[para])
    if info['id'] is "":
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
    demo.delete()
    return HttpResponseRedirect(reverse("demo:demo"))

def updateInfo(request,id):
    demo=DemoModel.objects.get(id=id)
    context={"demo": demo}
    return  render(request, "demo/addInfo.html", context)
