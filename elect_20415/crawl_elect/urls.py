from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('sgg/', views.add_sgg),
    # path('emd/', views.add_location),
]
