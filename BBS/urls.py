"""BBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import django_comments
from django.contrib.auth.views import login
from junge import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^detail/(\d+)/$',views.detail),
    url(r'^sub_comment/$',views.sub_comment),

    url(r'^accounts/Login/$',login,{'template_name':'Login.html'}),
    url(r'^acc_reg/$',views.acc_reg),
    url(r'^login/$',views.Login),
    url(r'^acc_login/$',views.acc_login),
    url(r'^logout/$',views.logout_view),
    url(r'^bbs_pub/$',views.bbs_pub),
    url(r'^bbs_sub/$',views.bbs_sub),
    url(r'^reg/$',views.reg),
    url(r'^log/$',views.log),

]
