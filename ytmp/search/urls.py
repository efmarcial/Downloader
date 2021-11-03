from os import name
from .import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index' ),
    path('video/', views.youTube, name="video_url")
]