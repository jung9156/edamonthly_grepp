from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('rec/', views.rec, name='rec'),
]
