from django.urls import path

from Core import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("properties/", views.properties, name="Properties"),
    path("search/", views.search, name="Search"),
    path("fight/", views.fight, name="Fight"),
    path("fast/", views.fast, name="Fast"),
    path("revenge/", views.revenge, name="Revenge"),
    path("hit/", views.hit, name="Hit"),
    path("email/", views.send_email, name="SendMail"),
    path("save/", views.save, name="Save"),
    path("dashboards", views.dashboards, name="Dashboards"),
]
