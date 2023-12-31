"""
URL configuration for nexusbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.urls import path
from sharing_api import views as sharing_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sharing_api/', sharing_views.sharing_list),
    path('sharing_api/<int:id>/', sharing_views.sharing_detail),

    path('api/', include('meter_api.urls')),


]

from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

   
    path('api/', include('meter_api.urls')),





    path('meter_reading_api/', include('meter_reading_api.urls')),
    path('user/', include('user.urls')),
]

