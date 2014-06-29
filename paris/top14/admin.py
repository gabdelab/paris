from django.contrib import admin

from top14.models import Match, Team, Player


class MatchAdmin(admin.ModelAdmin):
  fields = ['homeTeam', 'homeTeamPoints', 'awayTeamPoints', 'awayTeam']


class TeamAdmin(admin.ModelAdmin):
  fields = ['name']


class PlayerAdmin(admin.ModelAdmin):
	fields = ['name', 'points']


admin.site.register(Match, MatchAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
