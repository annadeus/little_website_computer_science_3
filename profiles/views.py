from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView


class ProfileDetailView(DetailView):
    """Return the Users profile"""
    template_name = "profiles/profile_index.html"

class ProfileUpdateView(UpdateView):
    """Update the Users profile"""
    pass

class ProfileDeleteView(DeleteView):
    """Delete the Users profile"""
    pass