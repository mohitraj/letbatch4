"""batch4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base import views as viewbase 
from user_app import views as user_view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

#from att.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', include('base.urls')),
    path('att/', include('att.urls')),
    path('user/', include('user_app.urls')),
    path('post/', include('blog.urls')),
    path('photos/', include('photos.urls')),
    path("", user_view.loginpage),
    path("login/", user_view.loginpage),
    path('api-auth/', include('rest_framework.urls')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user_app/password_reset.html'), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>', 
    	auth_views.PasswordResetConfirmView.as_view(template_name='user_app/password_reset_confirm.html'),name='password_reset_confirm'),

    path('password-reset-done/', 
    	auth_views.PasswordResetDoneView.as_view(template_name='user_app/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-complete/', 
    	auth_views.PasswordResetCompleteView.as_view(template_name='user_app/password_reset_complete.html'), name='password_reset_complete'),



    ]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


#path("login/", loginpage, name= 'login'),