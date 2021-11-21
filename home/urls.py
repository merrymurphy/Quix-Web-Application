from django.contrib import admin
from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
]