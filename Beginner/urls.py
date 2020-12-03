from django.urls import path
from .views import (
                    BeginnerTutorialListView,
               )
from .import views                    

urlpatterns = [
  
   path('Beginner/' ,   BeginnerTutorialListView.as_view() , name = 'Beginner-tutorial'),
   path('Beginner_join/', views.Beginnerjoin, name='Beginner-join'),
]