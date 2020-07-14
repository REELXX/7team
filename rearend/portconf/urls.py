from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tables/', views.tables),
    url(r'^tables_dynamic/', views.tables_dynamic),
]