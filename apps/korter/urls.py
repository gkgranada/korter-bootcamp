from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.default_view, name='index'),
    url(r'^feed/$', views.feed_view, name='feed'),
    url(r'^rules/$', views.rules_view, name='rules'),
    url(r'^neighbours/$', views.neighbour_view, name='neighbours'),
    url(r'^contract/$', views.contract_view, name='contract'),
    url(r'^bills/$', views.bill_view, name='bills'),

]
