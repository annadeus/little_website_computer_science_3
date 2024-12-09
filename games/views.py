from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView

class GamesDetailView(DetailView):
    """Return a single game"""
    template_name = "games/game_detail.html"