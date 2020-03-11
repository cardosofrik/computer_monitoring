from django.urls import path
from dispositivo import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('computador/', views.configComputador, name='computador'),
    path('monitoramento/', views.monitorados, name='monitoramento'),
    path('camera/<camera_id>', views.capturar_camera, name='camera'),
    path('audio/<audio_id>', views.capturar_audios, name='audio'),


]
