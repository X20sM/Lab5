from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_User, name='add_User'),
    path('', views.People, name='People'),
]