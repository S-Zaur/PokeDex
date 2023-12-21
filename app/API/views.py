import json

from django.core.exceptions import SuspiciousOperation
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from Core.models import Pokemon
from Core.pokemon_utils import pokemons_list, get_payload, get_pokemon, get_random_pokemon, fight_hit, fight_start, \
    fight_fast


@require_http_methods(["GET"])
def api_pokemons_list(request):
    return JsonResponse(pokemons_list(get_payload(request), base_page=reverse('API.List')))


@require_http_methods(["GET"])
def api_get_pokemon(request, pokemon_id):
    return JsonResponse({"pokemon": get_pokemon(pokemon_id).to_json()})


@require_http_methods(["GET"])
def api_random_pokemon(request):
    return JsonResponse({"pokemon": get_random_pokemon().to_json()})


@require_http_methods(["GET"])
def api_fight(request):
    if "player_pokemon" not in request.GET or "opponent_pokemon" not in request.GET:
        raise SuspiciousOperation
    return JsonResponse(fight_start(request.GET["player_pokemon"], request.GET["opponent_pokemon"]))


@require_http_methods(["POST"])
def api_hit(request, number):
    if "player_pokemon" not in request.POST or "opponent_pokemon" not in request.POST:
        raise SuspiciousOperation
    player_pokemon = Pokemon(**json.loads(request.POST["player_pokemon"].replace("'", '"')))
    opponent_pokemon = Pokemon(**json.loads(request.POST["opponent_pokemon"].replace("'", '"')))
    return JsonResponse(fight_hit(request, int(request.POST['round_count']), player_pokemon, opponent_pokemon, number))


@require_http_methods(["GET"])
def api_fast_fight(request):
    if "player_pokemon" not in request.GET or "opponent_pokemon" not in request.GET:
        raise SuspiciousOperation
    opponent_pokemon = Pokemon(**json.loads(request.GET["opponent_pokemon"].replace("'", '"')))
    player_pokemon = Pokemon(**json.loads(request.GET["player_pokemon"].replace("'", '"')))
    return JsonResponse(fight_fast(request, player_pokemon, opponent_pokemon))
