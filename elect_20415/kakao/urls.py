from django.urls import path
from . import views


app_name = 'kakao'

urlpatterns = [
    path('', views.index, name='index'),
    path('message/', views.message, name='message'),
    path('sgg/', views.sgg, name='send_url'),
    path('filter/<str:sgg>/', views.filter_candidates, name='filter'),
    path('name/', views.name, name="name"),
    path('searchname/<str:name>/', views.search_name, name="search_name"),
    path('juso/', views.juso, name='juso'),
    path('searchjuso/<str:juso>/', views.search_juso, name="search_juso"),

]
