from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.grabber_two, name='grabber_two'),
    url(r'^(?P<pkt>\d+)$', views.grabber_two, name='grabber_two'),
    url(r'^[0-9]{2}/', views.grabber_two, name='dope'),


]
