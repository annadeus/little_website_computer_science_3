from django.urls import path
from dashboard import views

urlpatterns = [
    path("", views.LandingView.as_view(), name="landing_page"),
    path("dashboard/", views.DashboardView.as_view(), name="index"),
]