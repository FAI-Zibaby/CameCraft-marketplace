from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/artisan/', views.artisan_dashboard, name='artisan_dashboard'), # <--- New
    path('dashboard/buyer/', views.buyer_dashboard, name='buyer_dashboard'),
    path('register/', views.register, name='register'),
]