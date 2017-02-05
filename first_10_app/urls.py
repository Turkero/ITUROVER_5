from django.conf.urls import url
from django.contrib import admin
#from post.views import topics_home
#this let the urls.py know the dir of topics_home
#we can also use this one ->
#from post import views
#but if i use this one I change second url to views.topics_home

from . import views

urlpatterns = [
    url(r'^$', views.bemember),
]