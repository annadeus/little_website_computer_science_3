from django.contrib import admin
from profiles.models import Profile

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProjectAdmin)
