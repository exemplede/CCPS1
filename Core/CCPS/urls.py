from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    indexView, proposView, equipementsView, projetsView, loginView, registerView, 
    dashboardView, testView, articleDetailsView, articleDeleteView, articleEditView,
    imageDeleteView, missionView, equipeView,contView,propos1View,filView
)

urlpatterns = [
    #path('', testView, name="home"),
    path('', indexView, name="home"),
    path('propos/', proposView, name="about"),
    path('projets/', projetsView, name="projets"),
    path('equipement/', equipementsView, name="equipements"),
    path('login/', loginView, name='login'),
    path('register/', registerView, name='register'),
    path('dashboard/', dashboardView, name='dashboard'),
    path('articles/<str:pk>/', articleDetailsView, name='articleDetails'),
    path('articles/<str:pk>/edit/', articleEditView, name='articleEdit'),
    path('articles/<str:pk>/delete/', articleDeleteView, name='articleDelete'),
    path('images/<str:pk>/', imageDeleteView, name='imageDelete'),
    path("mission/", missionView, name="mission"),
    path("equipe/", equipeView, name="equipe"),
    path("cont/", contView, name="cont"),
    path("propos/propos1/", propos1View, name="propos1"),
    path("propos/fil/", filView, name="fil")
]

if settings.DEBUG:
    # en devoleppememt
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# en production il faudra utiliser nginx ou apache2 comme reverse proxy
# utilser des images docker se...
