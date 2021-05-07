from django.shortcuts import render, HttpResponse

#FOR USE of rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#from .serializers import *
import os

# for compare the diffrent summnor name
from lol_frontend.functionality.playercompare import compare
from lol_frontend.functionality.playerPlayStyle import playStyle
from lol_frontend.functionality.leaderboardGenerate import callTogenerate
from lol_frontend.functionality.suggestion import generatesuggestion
from lol_frontend.functionality.Match_data import getmatchdata
from lol_frontend.variable import *
import json


def index(request):
    return render(request, 'build/index.html')


@api_view(['POST'])
def leaderboard_view(request):
    
    res = {} 
    #post request is like this {  "region" : "br1" , "queue": "RANKED_SOLO_5x5" , "league":"challengerleagues" }
    if request.method == 'POST':    
        try:
            region = request.data['region']
            queue = request.data['queue']
            league = request.data['league']

            val = region + '_'+league + '_' + queue
            res = leaderboard_DATA[val]
        except:
            res = {}
        Response(res)
    return Response(res)

    
@api_view(['POST'])
def upcomingLeague_view(request):
    
    res = {}
    if request.method == 'POST':
        res = {}
        try:
            region = request.data['region']
            res = upcomingleague_DATA[region]
        except:
            res = {}
        return Response(res)
    return Response(res)


@api_view(['POST'])
def playercompare_view(request):

    res = {}
    #post request data like this 
    #{ "region":  ["na1", "br1", "la1", "oc1"] , "player" : ["Doublelift", "just gap mid", "Faststroke", "C1ock"]  }
    if request.method == 'POST':
        res = {}
        try:
            regionList = request.data['region']
            summnorNameList = request.data['player']
            res = compare(regionList, summnorNameList)
        except:
            res = {}
        return Response(res)
    return Response(res)

  
@api_view(['POST'])
def playerPlayStyle_view(request):
    res = {}
    
    # post request like this { "region":"na1" , "summnorname":"doublelift"}
    if request.method == 'POST':
        try:
            summnorName = request.data['summnorname']
            region = request.data['region']
            res = playStyle(region, summnorName)
        except:
            res = {}
        return Response(res)
    
    return Response(res)

@api_view(['POST'])
def suggestion_view(request):
    res = {}

    # post request like this { "region":"na1" , "summnorname":"doublelift"}
    if request.method == 'POST':
        try:
            region = request.data['region']
            summnorname = request.data['summnorname']
            res = generatesuggestion(region, summnorname)
        except:
            res = {}
        return Response(res)
    
    return Response(res)

@api_view(['POST'])
def summonerdata(request):
    
    res = {}
    # {"region":"na1" , "summnorname":"doublelift"}
    if request.method == 'POST':
        try:
            region = request.data['region']
            summnorname = request.data['summnorname']
            res = getmatchdata(region, summnorname)
        except:
            res = {}

        return Response(res)        
    return Response(res)

