from django.urls import path
from bug_reports import views

urlpatterns = [
    # Bug Report List
    path("bug-reports/", views.BugReportListView.as_view(), name="bug_report_index"),

    # Bug Report Detail
    path("bug-reports/<int:pk>/", views.BugReportDetailView.as_view(), name="bug_report_detail"),

    # Bug Report Create
    path("bug-reports/add/", views.BugReportCreateView.as_view(), name="bug_report_add"),

    # Bug Report Update
    path("bug-reports/<int:pk>/update/", views.BugReportUpdateView.as_view(), name="bug_report_update"),

    # Bug Report Delete
    path("bug-reports/<int:pk>/delete/", views.BugReportDeleteView.as_view(), name="bug_report_delete"),
]