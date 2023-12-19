from django.urls import path

from Core import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("properties/", views.properties, name="Properties"),
    path("search/", views.search, name="Search"),
    path("fight/", views.fight, name="Fight"),
    path("revenge/", views.revenge, name="Revenge"),
    path("hit/", views.hit, name="Hit"),
]
