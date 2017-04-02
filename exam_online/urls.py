from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^accounts/(?P<name>[\S]+)/login$', views.candidateLogin, name="candidateLogin"),
    url(r'^accounts/(?P<name>[\S]+)/register$', views.candidateRegister, name="candidateRegister"),
]