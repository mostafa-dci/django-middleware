from django.urls import path
from .views import index, addWord, all, search
# define some patterns for urls for my project

urlpatterns = [
    # app paths
    path("", index, name="home"),
    path('add/', addWord, name="addWord"),
    path('all/', all, name="allWords"),
    path('search/', search, name="Search")
]