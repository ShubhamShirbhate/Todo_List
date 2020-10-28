from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('current/',views.currenttodo, name="currenttodo"),
    path('complete/',views.completetodos, name="completetodos"),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),

]
