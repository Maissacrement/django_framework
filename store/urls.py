from django.conf.urls import url
from store import views

urlpatterns = [
    #url(r'^$', views.index),
    url(r'^$', views.listing),
]
