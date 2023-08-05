from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('repair/<str:pk>/', views.repair, name='repair'),
]