from django.urls import path
from .views import index, game_page, classement, memorygame, mortsubite, Inscription, Connexion, logoutUser, profil


urlpatterns = [
    path('', index, name='index'),
    path('gamemode.html',game_page, name='game_page'),
    path('classement.html', classement, name='classement'),
    path('index.html', index, name='index'),
    path('memory_game.html', memorygame, name='memory_game'),
    path('mortsubite.html', mortsubite, name='mortsubite'),
    path('inscription.html', Inscription, name='inscription'),
    path('connexion.html', Connexion, name='connexion'),
    path('deconnexion.html', logoutUser, name='deconnexion'),
    path('profil.html', profil, name='profil'),
]