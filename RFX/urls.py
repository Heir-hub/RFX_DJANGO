from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home-section'),
    path('admin/', views.admin, name='admin'),
    path('join/', views.join, name='join'),
    path('aboutfx/', views.aboutfx, name='aboutfx'),
  
    
     
]
