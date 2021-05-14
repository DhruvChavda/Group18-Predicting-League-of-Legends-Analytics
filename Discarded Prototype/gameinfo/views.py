from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages 

from .forms import GetNameForlistChamp, GetAccountSearch

# from .forms import SignUpForm, EditProfileForm, AccountAuthenticationForm,Subscribe
# Create your views here.
import requests
import datetime


API = 'Riot api enter  here'

def upcomingLeague(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    
    url = 'https://br1.api.riotgames.com/lol/clash/v1/tournaments?api_key='+ API
    responce = requests.get(url)
    context = {}
    upcoming_league = {}
    if responce.status_code == 200:
        upcoming_league = responce.json()
        for res in upcoming_league:
            for lis in res['schedule']:
                ts = datetime.datetime.fromtimestamp(int(lis['registrationTime']/1000)).isoformat()
                lis['registrationTime'] = ts
                ts = datetime.datetime.fromtimestamp(int(lis['startTime']/1000)).isoformat()
                lis['startTime'] = ts   

    context = {
        'upcoming_league' : upcoming_league,
    } 
    return render(request, 'gameinfo/upcomingLeague.html', context)


## resolve this thing
def listChampBySum(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")

    context = {}
    if request.method == 'POST':
        form = GetNameForlistChamp(request.POST)
        if form.is_valid:
            #summnor_id = request.POST['SummonerId']
            #cd = form.cleaned_data
            summnor_id = request.POST.get('SummonerId')#cd.get('SummonerId')
            url = 'https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/' + summnor_id + '?api_key=' + API
            responce = requests.get(url)
            if responce.status_code == 200:
                listOfChamp = responce.json()
                for res in listOfChamp:
                    ts = datetime.datetime.fromtimestamp(int(res['lastPlayTime']/1000)).isoformat()
                    res['lastPlayTime'] = ts

                context = {
                    "listOfChamp":listOfChamp
                }
            return render(request, 'gameinfo/listChampBySum.html', context)     
    else:
        form = GetNameForlistChamp()
    context = {}
    return render(request, 'gameinfo/listChampBySum.html', context)


def ChampBySum(request, champ_id):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")

    context = {}
    if request.method == 'POST':
        form = GetNameForlistChamp(request.POST)
        if form.is_valid:
            #summnor_id = request.POST['SummonerId']
            #cd = form.cleaned_data
            summnor_id = request.POST.get('SummonerId')#cd.get('SummonerId')
            url = 'https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/' + summnor_id + 'by-champion/' + str(champ_id)+ '?api_key=' + API
            responce = requests.get(url)
            if responce.status_code == 200:
                listOfChamp = responce.json()
                for res in listOfChamp:
                    ts = datetime.datetime.fromtimestamp(int(res['lastPlayTime']/1000)).isoformat()
                    res['lastPlayTime'] = ts

                context = {
                    "listOfChamp":listOfChamp
                }
            elif responce.status_code == 200:
                context = {
                    'listOfChamp': 'champion does not exits by this id'
                }
            return render(request, 'gameinfo/ChampBySum.html', context)     
    else:
        form = GetNameForlistChamp()
    context = {}
    return HttpResponseRedirect(reverse("champbysum", args=(champ_id,))) #render(request, 'gameinfo/ChampBySum.html', context)


def findSumid(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")

    context = {}
    if request.method == 'POST':
        form = GetNameForlistChamp(request.POST)
        if form.is_valid:
            #summnor_id = request.POST['SummonerId']
            #cd = form.cleaned_data
            summnor_id = request.POST.get('SummonerId')#cd.get('SummonerId')
            url = 'https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/' + summnor_id + '?api_key=' + API
            responce = requests.get(url)
            if responce.status_code == 200:
                listOfChamp = responce.json()
                for res in listOfChamp:
                    ts = datetime.datetime.fromtimestamp(int(res['lastPlayTime']/1000)).isoformat()
                    res['lastPlayTime'] = ts

                context = {
                    "listOfChamp":listOfChamp
                }
            return render(request, 'gameinfo/listChampBySum.html', context)     
    else:
        form = GetNameForlistChamp()
    context = {}
    return redirect(request, 'gameinfo/listChampBySum.html', context)






def SearchByLookupID(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    
    context = {}
    if request.method == 'POST':
        form = GetAccountSearch(request.POST)
        if form.is_valid:
            region = request.POST.get('region')
            region = 'br1'
            summonername = request.POST.get('SummonerId')
            return redirect(region + '/' + summonername)
    else:
        form = GetAccountSearch()
    
    return render(request, 'gameinfo/SearchByLookupID.html', context)

def SearchByAccountID(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    
    context = {}
    if request.method == 'POST':
        form = GetAccountSearch(request.POST)
        if form.is_valid:
            region = request.POST.get('region')
            region = 'br1'
            AccountID = request.POST.get('SummonerId')
            print(region, AccountID)
            return redirect( region + '/' + AccountID)
    else:
        form = GetAccountSearch()

    return render(request, 'gameinfo/SearchByAccountID.html', context)

def SearchBySummonerId(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    print("adhbsvf")
    context = {}
    if request.method == 'POST':
        form = GetAccountSearch(request.POST)
        if form.is_valid:
            region = request.POST.get('region')
            region = 'br1'
            SummonerId = request.POST.get('SummonerId')
            print(region, SummonerId)
            return redirect('SearchBySummonerId/' + region + '/' + SummonerId)
    else:
        form = GetAccountSearch()
    return render(request, 'gameinfo/SearchBySummonerId.html', context)



## this view are for account details
def SearchDoneByLookupID(request, region, summonername):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    
    url = 'https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonername + '?api_key=' + API
    responce = requests.get(url)
    if responce.status_code == 200:
        lookup = responce.json()
        context = {
            'lookup' : lookup
        }
        return render(request, 'gameinfo/SearchDoneByLookupID.html', context)
    else:
        context = {
            'status_code' : 'status code' + str(responce.status_code)
        }
        return render(request, 'gameinfo/SearchDoneByLookupID.html', context)

def SearchDoneByAccountID(request, region, AccountID):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")

    url = 'https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-account/' + AccountID + '?api_key=' + API
    responce = requests.get(url)
    if responce.status_code == 200:
        lookup = responce.json()
        context = {
            'lookup' : lookup
        }
        return render(request, 'gameinfo/SearchDoneByLookupID.html', context)
    else:
        context = {
            'status_code' : 'status code' + str(responce.status_code)
        }
        return render(request, 'gameinfo/SearchDoneByLookupID.html', context)
    
def SearchDoneBySummonerId(request, region, SummonerId):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    
    url = 'https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/' + SummonerId + '?api_key=' + API
    responce = requests.get(url)
    if responce.status_code == 200:
        lookup = responce.json()
        context = {
            'lookup' : lookup
        }
        return render(request, 'gameinfo/SearchDoneByLookupID.html', context)
    else:
        context = {
            'status_code' : 'status code' + str(responce.status_code)
        }
        return render(request, 'gameinfo/SearchDoneByLookupID.html', context)

