from django.conf.urls import url
from django.contrib import admin

from .views import UpdateModelDetailAPI, UpdateModelListAPI

urlpatterns = [
    url(r'^$', UpdateModelListAPI.as_view()),
    url(r'^(?P<id>\d+)/$', UpdateModelDetailAPI.as_view()),
]
