
from django.urls import path
#from base import views as viewbase 
#from att.views import about
from .views import about, hello, ok

urlpatterns = [

    path('', about),
    path("hello/", hello),
    path("ok/", ok)


]
