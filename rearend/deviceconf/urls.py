from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^form_wizards/', views.form_wizards),
    url(r'^form_upload/', views.form_upload),
    url(r'^form_buttons/', views.form_buttons),
]