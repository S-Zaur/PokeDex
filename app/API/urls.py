from django.urls import path

from API import views

urlpatterns = [
    path("pokemon/list/", views.api_pokemons_list, name="API.List"),
    path("pokemon/<int:pokemon_id>/", views.api_get_pokemon, name="API.GetPokemon"),
    path("pokemon/random/", views.api_random_pokemon, name="API.RandomPokemon"),
    path("fight/", views.api_fight, name="API.Fight"),
    path("fight/<int:number>/", views.api_hit, name="API.Hit"),
    path("fight/fast/", views.api_fast_fight, name="API.FastFight"),
]
