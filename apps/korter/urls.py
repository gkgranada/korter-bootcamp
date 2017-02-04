from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.default_view, name='index'),
    url(r'^feed/$', views.feed_view, name='feed'),
    url(r'^feedManage/$', views.feedManage_view, name='feedManage'),
    url(r'^bills/$', views.bill_view, name='bills'),
    url(r'^neighbours/$', views.neighbours_view, name='neighbours'),
    url(r'^documents/$', views.documents_view, name='documents'),
    url(r'^account/$', views.account_view, name='account'),
]
