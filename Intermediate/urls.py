from django.urls import path
from .views import (
                    IntermediateTutorialListView,
                  )
from .import views                  

urlpatterns = [

   path('Intermediate/' , IntermediateTutorialListView.as_view() , name = 'Intermediate-tutorial'),
   path('Intermediate_join/', views.Intermediatejoin, name='Intermediate-join'),
]