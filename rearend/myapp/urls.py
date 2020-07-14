from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^myapp/index$', views.index),
    url(r'^myapp/router/$', views.router),
    url(r'^myapp/port/$', views.port),
    url(r'^myapp/router/(\d+)$', views.routerport)
]
