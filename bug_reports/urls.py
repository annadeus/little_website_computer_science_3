from django.urls import path
from bug_reports import views

urlpatterns = [
    path("bug-reports/", views.BugReportListView.as_view(), name="bug_report_index"),
    path("bug-reports/<int:pk>/", views.BugReportDetailView.as_view(), name="bug_report_detail"),
    path("bug-reports/add/", views.BugReportCreateView.as_view(), name="bug_report_add"),
    path("bug-reports/<int:pk>/update/", views.BugReportUpdateView.as_view(), name="bug_report_update"),
    path("bug-reports/<int:pk>/delete/", views.BugReportDeleteView.as_view(), name="bug_report_delete"),
]