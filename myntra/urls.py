from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('profile/', views.profile, name='profile'),
    path('mysaved/', views.mysaved, name='mysaved'),
    path('reel/', views.reel, name='reel'),
    path('chat/', views.chat, name='chat'),
]