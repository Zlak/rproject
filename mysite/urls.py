"""mysite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from zhifutime import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page, name='home_page'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^thesaurus/$', views.thesaurus, name='thesaurus'),
    url(r'^info/$', views.projectinfo, name='projectinfo'),
    url(r'^services/$', views.services, name='services'),
    url(r'^prediction/$', views.prediction, name='prediction'),
]