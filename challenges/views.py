from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly_challenge_by_number(request, month):
    challenge_text= None
    if month == 1:
        challenge_text = "Exercise"
    elif month == 2:
        challenge_text = "Eat no meat"
    elif month == 3:
        challenge_text = "take a walk"
    elif month == 4:
        challenge_text = "swim"
    elif month == 5:
        challenge_text = "No alcohol"
    elif month == 6:
        challenge_text = "Pray"
    elif month == 7:
        challenge_text = "Trade"
    elif month == 8:
        challenge_text = "Vacation"
    elif month == 9:
        challenge_text = "No movies"
    elif month == 10:
        challenge_text = "No soft drinks"
    elif month == 11:
        challenge_text = "Eat enough Proteins"
    elif month == 12:
        challenge_text = "Enjoy"
    else:
        return HttpResponseNotFound('This month is not valid')
    return HttpResponse(challenge_text)

def monthly_challenge(request, month):
    challenge_text= None
    if month == "january":
        challenge_text = "Exercise"
    elif month == "february":
        challenge_text = "Eat no meat"
    elif month == "march":
        challenge_text = "take a walk"
    elif month == "april":
        challenge_text = "swim"
    elif month == "may":
        challenge_text = "No alcohol"
    elif month == "june":
        challenge_text = "Pray"
    elif month == "july":
        challenge_text = "Trade"
    elif month == "august":
        challenge_text = "Vacation"
    elif month == "september":
        challenge_text = "No movies"
    elif month == "october":
        challenge_text = "No soft drinks"
    elif month == "november":
        challenge_text = "Eat enough Proteins"
    elif month == "december":
        challenge_text = "Enjoy"
    else:
        return HttpResponseNotFound('This month is not valid')
    return HttpResponse(challenge_text)



