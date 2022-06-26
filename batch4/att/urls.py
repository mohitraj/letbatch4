
from django.urls import path
#from base import views as viewbase 
#from att.views import about
from .views import *

urlpatterns = [


    path("reg/", StudentMaster, name="regform"),
    path("mark/", Mark_Att, name="mark"),
    path("allatt/", display_attendance, name="all_att"),
    path("oneatt/", display_attendanceone, name="one_att"),
    path("stuinfo/<int:pk>", studentdetails, name= "stu_api"),
    path("student_api/", student_api),

    #path("login/",auth_views.LoginViews.as_view(template_name='user_app/disform.html'), name='')

]
