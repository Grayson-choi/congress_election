from django.urls import path
from . import views


app_name = 'kakao'

urlpatterns = [
    path('', views.index, name='index'),
    path('checksever/', views.checkserver, name='chkserver'),
    path('message/', views.message, name='message'),
    path('context/', views.context),
    path('context2/', views.context2),
    path('context3/', views.context3),
    path('message/', views.message, name='message') ,
    path('filter/<str:sgg>/', views.filter_candidates, name='filter'),
    path('send_url/', views.send_url, name='send_url')
]
