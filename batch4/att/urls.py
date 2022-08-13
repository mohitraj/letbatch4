
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
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
    path("class_api/", MasterListAPI.as_view(), name="masterall"),
    path("create_api/", MasterCreateAPI.as_view(), name="mastercreate"),
    path("class_api/<int:pk>", MasterRetrieveAPI.as_view(), name="masterretrive"),
    path("class_update/<int:pk>", MasterUpdateAPI.as_view(), name="masterupdate"),
    path("class_des/<int:pk>", MasterDestroyAPI.as_view(), name="masterdelete"),
    path("class_createlist", MasterListCreateAPI.as_view(), name="MasterListCreateAPI"),
    path("class_retup/<int:pk>", MasterRetUpdate.as_view(), name="masterdelete"),
    path("class_redes/<int:pk>", MasterRetDes.as_view(), name="masterretdes"),
    path("class_rud/<int:pk>", MasterRUD.as_view(), name="MasterRUD"),
    path('gettoken/', obtain_auth_token),
    


    
    
    #path('api-auth/', include('rest_framework.urls')),

    #path("login/",auth_views.LoginViews.as_view(template_name='user_app/disform.html'), name='')

]
