from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('sgg/', views.add_sgg),
    path('delete_sgg/', views.delete_sgg)
]
