from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView


class DashboardView(TemplateView):
    """Return the Dashboard"""
    template_name = 'dashboard/index.html'
