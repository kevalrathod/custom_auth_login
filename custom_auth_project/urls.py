"""custom_auth_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from website_login.views import (home,signup,account_activation_sent,activate)
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('login/',auth_views.login,{'template_name':'profiles/login.html'},name='login'),
    path('logout/',auth_views.logout,{'next_page':'login'},name='logout'),
    path('signup/',signup,name='signup'),
    path('account_activation_sent/',account_activation_sent,name='account_activation_sent'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
                activate, name='activate'),

]
