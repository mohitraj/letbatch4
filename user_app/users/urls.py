from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import path

from . import views 


urlpatterns = [
    

    path('', views.register, name="ChangePassword"),

    #path('', views.function2, name="main_route")
]