from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('home', views.home),
    path('process_money/<str:place>', views.process_money),
    path('reset', views.reset),
]


