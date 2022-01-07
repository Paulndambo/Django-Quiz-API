from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("send-mail/", views.send_email, name="send-mail"),
]
