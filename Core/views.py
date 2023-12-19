import json

from django.conf import settings
from django.core.exceptions import SuspiciousOperation
from django.core.mail import get_connection, EmailMessage
from django.http import JsonResponse, Http404
from django.shortcuts import render

from django.urls import reverse

from Core.models import Pokemon
from Core.pokemon_utils import pokemons_list, get_payload, get_pokemon, fight_start, get_random_pokemon, fight_hit, \
    fight_fast


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


def fast(request):
    player_pokemon = Pokemon(**json.loads(request.GET["player_pokemon"].replace("'", '"')))
    opponent_pokemon = Pokemon(**json.loads(request.GET["opponent_pokemon"].replace("'", '"')))
    return JsonResponse(fight_fast(request, player_pokemon, opponent_pokemon))


def send_email(request):
    if not request.user.is_authenticated:
        raise SuspiciousOperation()
    with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS
    ) as connection:
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email, ]
        message = f"ваш покемон {request.POST['player_pokemon']} встретился с {request.POST['opponent_pokemon']} в результате боя он {'победил' if request.POST['result'] == 'WIN' else 'проиграл'}"
        EmailMessage("PokeFight", message, email_from, recipient_list, connection=connection).send()

    return JsonResponse({"result": "ok"})
