from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view()),
    url(r'^list/$', views.list, name='list'),
    url(r'^add/$', views.list, name='add'),
]