from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signupuser/',views.signupuser, name="signupuser"),
    path('loginuser/',views.loginuser, name="loginuser"),
    path('logout/',views.logoutuser, name="logoutuser"),
    path('create/',views.create, name="create"),
]
