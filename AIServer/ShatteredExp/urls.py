from django.urls import path
from . import views

urlpatterns = [
    path('deduceBlue/', views.deduceBlue, name='deduceBlue'),
    path('pureTest/',views.pureTest,name='pureTest'),
    path('updateAgent/',views.updateAgent,name='updateAgent'),
    path('gameOver/',views.gameOver,name='gameOver'),
    path('updateEnemyTarget/',views.updateEnemyTarget,name='gameOver'),
    path('updateObstacleTarget/',views.updateObstacleTarget,name='updateObstacleTarget'),
    path('updateBuildingTarget/',views.updateBuildingTarget,name='updateBuildingTarget'),
    path('updateDestination/',views.updateDestination,name='updateDestination'),
    path('initializeMap/',views.initializeMap,name='initializeMap'),
    path('gameOverTest/',views.gameOverTest,name='gameOverTest'),
    path('updateMapData/',views.updateMapData,name='updateMapData'),
    path('updateApartmentData/',views.updateApartmentData,name='updateApartmentData'),
    path('updateDestinationTest/',views.updateDestinationTest,name='updateDestinationTest'),
]

