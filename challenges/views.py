from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly_challenge_by_number(request, month):
    challenge_text= None
    if month == 1:
        challenge_text = 'Exercise'
    return HttpResponse(challenge_text)

def monthly_challenge(request, month):
    challenge_text= None
    if month == "january":
        challenge_text = 'Exercise'
    elif month == "february":
        challenge_text = 'Eat no meat'
    elif month == "march":
        challenge_text = 'take a walk'
    elif month == "april":
        challenge_text = 'swim'
    else:
        return HttpResponseNotFound('This month is not valid')
    return HttpResponse(challenge_text)



