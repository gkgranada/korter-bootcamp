from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.default_view, name='index'),
    url(r'^feed/$', views.feed_view, name='feed'),
]
