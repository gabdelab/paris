from django.contrib import admin

from top14.models import Match, Team


class MatchAdmin(admin.ModelAdmin):
  fields = ['homeTeam', 'homeTeamPoints', 'awayTeamPoints', 'awayTeam']


class TeamAdmin(admin.ModelAdmin):
  fields = ['name']


admin.site.register(Match, MatchAdmin)
admin.site.register(Team, TeamAdmin)
