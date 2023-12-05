from django.urls import path
from .views import index, game_page, inscription, classement, memorygame, mortsubite


urlpatterns = [
    path('', index, name='index'),
    path('gamemode.html',game_page, name='game_page'),
    path('inscription.html', inscription, name='inscription'),
    path('classement.html', classement, name='classement'),
    path('index.html', index, name='index'),
    path('memory_game.html', memorygame, name='memory_game'),
    path('mortsubite.html', mortsubite, name='mortsubite'),
    path('form.html', inscription, name='inscription'),
]