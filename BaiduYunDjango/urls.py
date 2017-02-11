"""BaiduYunDjango URL Configuration

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
from CMS import views
from django.conf import settings
import django
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^file-(\d+)-(\d+).html', views.file_info, name = 'fileinfo'),
    url(r'^redirect-(\d+)-(\d+).html', views.redirect, name = 'redirect'),
    url(r'^search/(\d+)/$', views.search, name = 'search'),
    url(r'^v1/search/(\d+)/$', views.apisearch, name = 'apisearch'),
    url(r'^user-(\d+)-(\d+).html', views.user, name = 'user'),
    url(r'^admin/', admin.site.urls),
    url(r'^baidu/', views.index, name = 'home'),
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^download/', views.download, name = 'download'),
    #url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': '/root/www/BaiduYunDjango/CMS/static'}),
]
