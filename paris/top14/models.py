from django.db import models


class Team(models.Model):

  name = models.CharField(max_length=30)


class Match(models.Model):

  homeTeam = models.CharField(max_length=30)
  awayTeam = models.CharField(max_length=30)


class Result(models.Model):

  homeTeamPoints = models.PositiveSmallIntegerField(default=0)
  awayTeamPoints = models.PositiveSmallIntegerField(default=0)
