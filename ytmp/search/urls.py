from .import views
from django.urls import path

urlpatterns = [
    path('', views.DoSomething, name='Do_Something'),
    path('',views.index, name='index' )
]