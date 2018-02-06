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
from index import index_views,test_view
from many_test import many_views,many_url
from index.test_view import vue_test

 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index_views.index,name="index_page"),
    
    url(r'^login/', index_views.login,name="login_page"),
      url(r'^logout/', index_views.login,name="logout_page"),
    url(r'^register/', index_views.register),
    url(r'^change_pwd/', index_views.change_pwd),
    
    url(r'^client_account/', index_views.client_account, name="client_account"),
    url(r'^online_server/', index_views.online_server, name="online_server"),
    url(r'^test_server/', index_views.test_server, name="test_server"),
    url(r'^windows_server/', index_views.windows_server ,name="windows_server"),
    url(r'^test_fresh/', index_views.test_fresh ,name="test_fresh"),
    
# test djagno model--------------------------------------------------------------------------    
    url(r'^test_test/', test_view.test_test ),
#     url(r'^many_many/', test_view.many_many ),
    url(r'^many_2_many/', many_views.many_2_many ),
    url(r'^vue_test/', test_view.vue_test ),
                                                                
# rest framework
    
    url(r'^many_api/', include(many_url)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]
