from django.urls import path
from . import views

urlpatterns = [
    path('', views.views),
    path('about', views.about),
    path('location', views.location),
    path('exer1', views.exer1),
    path('exer2', views.exer2)
]