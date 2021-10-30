from os import name
from .import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index' ),
    path('r', views.SomeFunction, name='ajax_foobar')
]