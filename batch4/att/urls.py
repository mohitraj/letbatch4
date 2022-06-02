
from django.urls import path
#from base import views as viewbase 
#from att.views import about
from .views import *

urlpatterns = [


    path("reg/", StudentMaster, name="regform")


]
