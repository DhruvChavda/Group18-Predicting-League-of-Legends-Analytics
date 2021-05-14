from django.contrib import admin
from lol_frontend.models import summonerDetails, MatchDataByGameId

# Register your models here.

admin.site.register(MatchDataByGameId)
admin.site.register(summonerDetails)