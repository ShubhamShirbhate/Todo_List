from django.urls import path, include
from . import views 

urlpatterns = [
   path('post/',views.Apilist.as_view()),
   path('post/<int:pk>',views.RetriveDestApilist.as_view()),
]
