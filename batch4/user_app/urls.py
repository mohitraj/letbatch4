#from base import views as viewbase 
#from att.views import about
from .views import *
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [


    path("register/", Register, name="Register"),
    #path("login/",auth_views.LoginView.as_view(template_name='user_app/disform.html'), name='login'),
    path("logout/",auth_views.LogoutView.as_view(template_name='user_app/logout.html'), name='logout'),
    path("login/", loginpage, name= 'login'),
    path("profile/", Profile, name="profile"),
    path("profile/<int:id1>", Profile_user, name="profile_user"),
    path("update/", Updateprofile, name="Updateprofile"),
    path("updatepass/", user_change_pass, name="Updatepass"),



]
