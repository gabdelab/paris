from django.db import models


class Team(models.Model):

  name = models.CharField(max_length=30)


class Result(models.Model):

  homeTeamPoints = models.IntegerField(default=0)
  awayTeamPoints = models.IntegerField(default=0)


class Match(models.Model):

  homeTeam = models.CharField(max_length=30)
  awayTeam = models.CharField(max_length=30)
  result = models.ForeignKey(Result)
