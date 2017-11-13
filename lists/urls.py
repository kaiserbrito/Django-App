from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view()),
    url(r'^list/$', views.user_list, name='user_list'),
    url(r'^add/$', views.add_user, name='add_user'),
]