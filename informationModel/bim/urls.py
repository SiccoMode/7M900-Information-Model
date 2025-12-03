from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),   
    path('floors/', views.getFloors, name='floors'),
    path('zones/', views.getZones, name='zones'),
    path('buildingelements/', views.getBuildingElements, name='buildingelements'),
    path('newelement/', views.createNewBuildingElement, name='newelement'),
    path('newfloor/', views.createNewFloor, name='newfloor'),
    path('newzone', views.createNewZone, name='newzone'),
]