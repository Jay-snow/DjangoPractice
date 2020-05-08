from django.urls import path

from . import views

urlpatterns = [
    # index
    path('', views.home, name="home"),

]