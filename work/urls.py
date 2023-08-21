from django.urls import path

from . import views

app_name='work'
urlpatterns=[
    path("",views.index, name="work"),
    path("poster/",views.poster, name="poster"),
]