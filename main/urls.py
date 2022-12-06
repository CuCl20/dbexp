from django.urls import path, include
from . import views

# appname = main

urlpatterns = [
    path('', views.display_order, name='main'),
    path('add/', views.addview, name='add'),
    path('submit/', views.display_add, name='submit'),
    path('update_order/', views.update_order, name='upd_order'),
    path('submit2/', views.update_o, name="upd_o"),
    path('submit3/', views.update_r, name="upd_r"),
    path('submit4/', views.delete_o, name='del_o')
]
