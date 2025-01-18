from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january":"Do Exercise",
    "february":"Eat no meat",
    "march":"take a walk",
    "april":"swim",
    "may":"No alcohol",
    "june":"Pray",
    "july":"Trade",
    "august":"Vacation",
    "september":"No movies",
    "october":"No soft drinks",
    "november":"Eat enough Proteins",
    "december":"Enjoy",
}

# Create your views here.
def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
    except:
        return HttpResponseNotFound('This month is not valid')
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound('This month is not valid')
    return HttpResponse(challenge_text)




