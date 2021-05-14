from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate


class GetNameForlistChamp(forms.Form):
    SummonerId = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'SummonerId'}))

region_choice =(
    ("br1", 'br1'),
    ("eun1", 'eun1'),
    ("euw1", 'euw1'),
    ('jp1', 'jp1'),
    ('kr', 'kr'),
    ('la1', 'la2'),
    ('na1', 'na1'),
    ('oc1', 'oc1'),
    ('ru', 'ru'),
    ('tr1', 'tr1'),
)

class GetAccountSearch(forms.Form):
    SummonerId = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'SummonerId'}))
    region = forms.ChoiceField(choices = region_choice)

