
from django.urls import path
#from base import views as viewbase 
#from att.views import about
from .views import *

urlpatterns = [

    path('', about),
    path("hello/", hello),
    path("ok/", ok),
    path("home/", home),
    path("hero/", ravinder),
    path("simpleform/", Student1, name="simpleform"),
    #path("live/", live, name="live"),
    #path('screenfeed/', screenfeed,"screenfeed"),


]
