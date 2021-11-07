"""gaitTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

#urls are defined here, path definitions are arbirtary, but the views are defined in views.py
#signin is the first page of the website beacause of empty path definition

urlpatterns = [
	path('admin/', admin.site.urls),
    path('',views.signin),
    path('postsignin/', views.postsignin),
    path('signup/', views.signup, name='signup'),#name = 'signup is used in login.html
    path('logout/', views.logout, name='log'),#name = 'log' is used in Home.html
    path('postsignup/',views.postsignup),
    path('home/', views.home),
]
