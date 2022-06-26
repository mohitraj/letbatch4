from django.urls import path
#from base import views as viewbase 
#from att.views import about
from .views import *

urlpatterns = [

    path('pic/', multiple_upload_pdf, name="pic_multiple_upload"),
   	path('download/ok/<str:file>', download_file, name="download_file"),


]