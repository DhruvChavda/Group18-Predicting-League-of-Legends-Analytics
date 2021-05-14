from django.urls import path
from . import views

urlpatterns = [
    path('upcoming_league/', views.upcomingLeague, name ='upcoming_league'),
    path('listChampBysummoner/', views.listChampBySum, name ='listchampbysum'),
    path('listChampBysummoner/<int:champ_id>', views.ChampBySum, name ='champbysum'),


    #for account finder
    path('SearchByLookupID/', views.SearchByLookupID, name='SearchByLookupID'),
    path('SearchByLookupID/<str:region>/<str:summonername>', views.SearchDoneByLookupID, name='SearchByLookupID'),

    path('SearchByAccountID/', views.SearchByAccountID, name='SearchByAccountID'),
    path('SearchByAccountID/<str:region>/<str:AccountID>', views.SearchDoneByAccountID, name='SearchByLookupID'),
    
    path('SearchBySummonerId', views.SearchBySummonerId, name='SearchBySummonerId'),
    path('SearchBySummonerId/<str:region>/<str:SummonerId>', views.SearchDoneBySummonerId, name='SearchByLookupID'),
    
]