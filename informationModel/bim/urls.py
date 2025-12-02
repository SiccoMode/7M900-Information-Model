from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),   
    path('floors/', views.getFloors, name='floors'),
    path('zones/', views.getZones, name='zones'),
    path('buildingelements/', views.getBuildingElements, name='buildingelements'), 
]