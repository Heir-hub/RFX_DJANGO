from django.urls import path
from .views import (
                    AdvanceTutorialListView,
                )
from .import views                    


urlpatterns = [
  
   path('Advance/' , AdvanceTutorialListView.as_view() , name = 'Advance-tutorial'),
   path('Advance_join/', views.Advancejoin, name='Advance-join'),

]