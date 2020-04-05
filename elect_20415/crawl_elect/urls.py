from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('sgg/', views.add_sgg),
    path('update_candidate/', views.update_candidate),
    path('brae/', views.brae_add)
]
