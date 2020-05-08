from django.urls import path

from . import views

urlpatterns = [
    # /login/
    path('', views.login, name="login"),

    # /login/success/
    path('success/', views.success, name="success"),


]