from django.urls import path

from . import views

urlpatterns = [
    path("", views.getFloors, name="floors"),   
    path('floors/', views.getFloors, name='floors'),
    path('zones/', views.getZones, name='zones'),
    path('walls/', views.getWalls, name='walls'),
    path('columns/', views.getColumns, name='columns'),
    path('newwall/', views.createNewWall, name='newwall'),
    path('newcolumn/', views.createNewColumn, name = 'newcolumn'),
    path('newfloor/', views.createNewFloor, name='newfloor'),
    path('newzone/', views.createNewZone, name='newzone'),
]