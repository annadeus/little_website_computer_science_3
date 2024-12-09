from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView


class BugReportListView(ListView):
    """Return a list of all bug reports"""
    template_name = "bug_reports/bug_report_index.html"

class BugReportDetailView(DetailView):
    """Return a single bug report"""
    template_name = "bug_reports/bug_report_detail.html"

class BugReportCreateView(CreateView):
    """Add a bug report"""
    pass

class BugReportUpdateView(UpdateView):
    """Update a bug report"""
    pass

class BugReportDeleteView(DeleteView):
    """Delete a bug report"""
    pass
