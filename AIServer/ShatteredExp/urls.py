from django.urls import path

from . import views

urlpatterns = [
    path('deduceBlue/', views.deduceBlue, name='deduceBlue'),
    path('pureTest/',views.pureTest,name='pureTest'),
]