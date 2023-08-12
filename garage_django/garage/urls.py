from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('home/', views.home, name='home'),
    path('repair/<str:pk>/', views.repair, name='repair'),
    path('create-repair/', views.createRepair, name='createrepair'),
    path('update-repair/<str:pk>/', views.updateRepair, name='updaterepair'),
    path('profile/<str:pk>/', views.userProfile, name='userprofile'),
    path('add-car/', views.addCar, name='addcar'),
    path('car/<str:pk>/', views.car, name='car'),
    path('repair-status/<str:pk>/', views.repairstatus, name='repairstatus'),
    path('client-login/', views.clientLogin, name='clientlogin'),
    path('', views.index, name='index'),

]