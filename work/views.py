from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"work/index.html",{"content":"welcome to work app"})

def poster(request):
    return render(request,"work/poster.html")