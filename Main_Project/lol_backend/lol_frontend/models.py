from django.db import models

# Create your models here.

class MatchDataByGameId(models.Model):
        matchId = models.IntegerField()
        region = models.CharField(max_length = 10,  default="br1")
        player1 = models.CharField(max_length = 100, default="")
        player2 = models.CharField(max_length = 100, default="")
        player3 = models.CharField(max_length = 100, default="")
        player4 = models.CharField(max_length = 100, default="")
        player5 = models.CharField(max_length = 100, default="")
        player6 = models.CharField(max_length = 100, default="")
        player7 = models.CharField(max_length = 100, default="")
        player8 = models.CharField(max_length = 100, default="")
        player9 = models.CharField(max_length = 100, default="")
        player10 = models.CharField(max_length = 100, default="")

class Account(models.Model):
        firstname = models.CharField(max_length = 20)
        lastname = models.CharField(max_length = 20)
        emailid = models.EmailField(verbose_name="email", max_length=60, unique=True)
        password = models.CharField(max_length = 100)

class summonerDetails(models.Model):
        summonername = models.CharField(max_length=30)
        region = models.CharField(max_length = 10,  default="br1")
        summonerid = models.CharField(max_length=60)
        accountid = models.CharField(max_length=60)
        