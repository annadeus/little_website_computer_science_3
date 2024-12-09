from django.urls import path
from games import views

urlpatterns = [
    path("games/<int:pk>/", views.GamesDetailView.as_view(), name="game_detail"),
]