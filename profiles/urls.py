from django.urls import path
from profiles import views

urlpatterns = [
path("profiles/<int:pk>/", views.ProfileDetailView.as_view(), name="profile_index"),
    path("profiles/<int:pk>/update/", views.ProfileUpdateView.as_view(), name="profile_update"),
    path("profiles/<int:pk>/delete/", views.ProfileDeleteView.as_view(), name="profile_delete"),
]