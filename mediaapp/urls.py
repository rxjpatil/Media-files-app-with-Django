from django.urls import path
from mediaapp import views

urlpatterns = [
    path('media', views.media),
    path('audio', views.Audio),
    path('video', views.Video),
    path('image', views.Images),
    
]
