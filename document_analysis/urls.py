from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('result/<similarity>/', views.result, name='result'),
]