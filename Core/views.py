import json

from django.http import JsonResponse, Http404
from django.shortcuts import render

from django.urls import reverse

from Core.models import Pokemon
from Core.pokemon_utils import pokemons_list, get_payload, get_pokemon, fight_start, get_random_pokemon, fight_hit


def index(request):
    return render(request, 'Core/index.html',
                  context=pokemons_list(get_payload(request), base_page=reverse(index)))


def properties(request):
    return JsonResponse(get_pokemon(request.GET["name"]).to_json())


def search(request):
    try:
        poke = get_pokemon(request.GET["name"])
        return render(request, 'Core/index.html', context={"pokemons": [poke]})
    except Http404:
        return render(request, 'Core/index.html', context={"errors": "not found"}, status=404)


def fight(request):
    player_pokemon = request.GET["name"]
    opponent_pokemon = get_random_pokemon().name
    return render(request, "Core/fight.html", context=fight_start(player_pokemon, opponent_pokemon))


def hit(request):
    player_pokemon = Pokemon(**json.loads(request.GET["player_pokemon"].replace("'", '"')))
    opponent_pokemon = Pokemon(**json.loads(request.GET["opponent_pokemon"].replace("'", '"')))
    number = int(request.GET["number"])
    current_round = int(request.GET["round_count"])
    return JsonResponse(fight_hit(request, current_round, player_pokemon, opponent_pokemon, number))


def revenge(request):
    player_pokemon = request.GET["player_pokemon"]
    opponent_pokemon = request.GET["opponent_pokemon"]
    return render(request, "Core/fight.html", context=fight_start(player_pokemon, opponent_pokemon))
