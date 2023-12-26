"""
URL configuration for core project.

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
from django.urls import path,include,re_path    
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView
from rest_framework import routers
from Data_Analyst import views

router = routers.DefaultRouter()
router.register(r'villages', views.VillageBoundaryViewset,basename="village")
router.register(r'mapping',views.VillageMappingFileViewset,basename='mapping')

urlpatterns = [
    
     path("admin/",admin.site.urls),
    path('auth/',include("djoser.urls")),
    path('auth/',include("djoser.urls.jwt")),
    path('auth/',include('djoser.urls.authtoken')),
    path('',include(router.urls)),
    
    
]

urlpatterns +=  [re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]

