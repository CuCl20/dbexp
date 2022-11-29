from django.urls import path, include
from . import views

# appname = main

urlpatterns = [
    path('', views.display_order, name='main'),
    path('add/', views.addview, name='add'),
    path('add/addorder/', views.display_add, name='order')
]
