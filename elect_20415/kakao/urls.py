from django.urls import path
from . import views


app_name = 'kakao'

urlpatterns = [
    path('', views.index, name='index'),
    path('checksever/', views.checkserver, name='chkserver'),
]
