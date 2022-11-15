from django.urls import path, include
from . import views

#appname = main

urlpatterns = [
    path('', views.display_order, name = 'main'),
    path('add/', views.addview, name = 'add')
]
