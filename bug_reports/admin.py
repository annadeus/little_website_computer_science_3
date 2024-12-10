from django.contrib import admin
from bug_reports.models import BugReport

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(BugReport, ProjectAdmin)
