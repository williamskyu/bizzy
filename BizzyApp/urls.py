from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^code', views.code, name='code'),
                url(r'^$', views.entry, name='entry'),
                url(r'^entry', views.entry, name='entry'),
              ]
