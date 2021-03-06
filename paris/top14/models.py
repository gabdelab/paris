from django.db import models


class Team(models.Model):

  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name


class Match(models.Model):

  homeTeam = models.ForeignKey(Team, related_name='homeTeam')
  awayTeam = models.ForeignKey(Team, related_name='awayTeam')
  homeTeamPoints = models.IntegerField(default=0)
  awayTeamPoints = models.IntegerField(default=0)


class Player(models.Model):

  name = models.CharField(max_length=30)
  points = models.IntegerField(default=0)

  def __str__(self):
  	return self.name


class Bet(models.Model):

  player = models.ForeignKey(Player, related_name='player')
  match = models.ForeignKey(Match, related_name='match')
