from .import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index' ),
    path('ajax/foo/', views.SomeFunction, name='ajax_foobar'),
    path('ajax/foo/', views.Convert, name='Convert')
]