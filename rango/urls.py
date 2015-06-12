from django.conf.urls import patterns, url
from rango import views

#create urls
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
]
