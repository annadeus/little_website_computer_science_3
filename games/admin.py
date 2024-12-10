from django.contrib import admin
from games.models import Game, HighScore

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game, ProjectAdmin)
admin.site.register(HighScore, ProjectAdmin)
