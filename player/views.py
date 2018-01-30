from django.shortcuts import render

# Create your views here.
from gameplay.models import Game


def home(request):
    games_first_player = Game.object.filter(
        first_player = request.user,
        status = 'F'
    )
    games_second_player = Game.object.filter(
        second_player = request.user,
        status = 'S'
    )
    all_games = list(games_first_player) + list(games_second_player)

    return render(request, "player/home.html",
                  {'games': all_games})
