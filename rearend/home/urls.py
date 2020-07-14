from django.conf.urls import url
from .views import account

urlpatterns = [
    # url(r'^login1/',account.login),
    url(r'^$', account.login),
    # url(r'^showlogin/', account.showlogin),
    # url(r'^quitzh/', account.quitzh),
    url(r'^home/', account.home),
    url(r'^index2/',account.index2),
    url(r'^index3/', account.index3),
]
