from django.urls import path
from .views import index, game_page, inscription


urlpatterns = [
    path('', index, name='index'),
    path('game/',game_page, name='game_page'),
    path('inscription.html', inscription, name='inscription')
]