from django.urls import path
from . import views


app_name = 'kakao'

urlpatterns = [
    path('all/', views.all, name='all'),
    path('searchall/', views.searchall, name='message'),
    path('sgg/', views.sgg, name='send_url'),
    path('filter/<str:sgg>/', views.filter_candidates, name='filter'),
    path('name/', views.name, name="name"),
    path('searchname/<str:name>/', views.search_name, name="search_name"),
    path('juso/', views.juso, name='juso'),
    path('searchjuso/<str:juso>/', views.search_juso, name="search_juso"),
    path('jungdang/', views.jungdang, name='jungdang'),
    path('searchjungdang/<str:jungdang>/', views.search_jungdang, name="search_jungdang"),

    # 비례대표

    path('brae_all/', views.brae_all, name='brae_index'),
    path('brae_searchall/', views.brae_searchall, name='brae_searchall'),
    # path('message/', views.message, name='message'),
    # path('sgg/', views.sgg, name='send_url'),
    # path('filter/<str:sgg>/', views.filter_candidates, name='filter'),
    path('brae_name/', views.brae_name, name="name"),
    path('brae_searchname/<str:name>/', views.brae_search_name, name="search_name"),
    # path('juso/', views.juso, name='juso'),
    # path('searchjuso/<str:juso>/', views.search_juso, name="search_juso"),
    path('brae_jungdang/', views.brae_jungdang, name='brae_jungdang'),
    path('brae_searchjungdang/<str:jungdang>/', views.brae_search_jungdang, name="brae_search_jungdang"),

    # 정당
    path('show_jd/', views.show_jd),
    path('jd/searchall/', views.jd_searchall)
]
