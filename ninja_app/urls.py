from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('register', views.register),
    path('logout', views.logout),
    path('game', views.index),
    path('get_rations', views.get_rations),
    path('train', views.train),
    #path('process_money', views.process),
    path('process', views.game),
    path('reset', views.reset),
    #path('countdown', views.countdown),
    path('textgame', views.game)
]