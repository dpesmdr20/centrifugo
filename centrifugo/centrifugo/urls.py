"""centrifugo URL Configuration
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("token/", views.generate_token,name="generate_token"),
    path("broadcast/", views.broadcast, name="broadcast"),
    path("publish/", views.publish, name="publish"),
    path("admin/", admin.site.urls),
]
