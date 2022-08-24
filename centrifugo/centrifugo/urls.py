"""centrifugo URL Configuration
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("centrifugo/token/", views.generate_token,name="generate_token"),
    path("centrifugo/broadcast/", views.broadcast, name="broadcast"),
    path("centrifugo/publish/", views.publish, name="publish"),
    path("admin/", admin.site.urls),
]
