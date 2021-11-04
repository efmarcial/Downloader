from os import name
from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index' ),
    path('video/', views.youTube, name="video_url")
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)