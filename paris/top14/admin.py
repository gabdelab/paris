from django.contrib import admin

from top14.models import Match, Team, Result


class MatchAdmin(admin.ModelAdmin):
  fields = ['homeTeam', 'result', 'awayTeam']


class TeamAdmin(admin.ModelAdmin):
  fields = ['name']


class ResultAdmin(admin.ModelAdmin):
  fields = ['homeTeamPoints', 'awayTeamPoints']

admin.site.register(Match, MatchAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Result, ResultAdmin)
