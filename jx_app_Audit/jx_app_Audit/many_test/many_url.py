"""jx_app_Audit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

#restframework is url
from rest_framework import routers
import view_set


router = routers.DefaultRouter()
router.register(r'author', view_set.AuthorViewSet)
router.register(r'book', view_set.BookViewSet)


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    
]

