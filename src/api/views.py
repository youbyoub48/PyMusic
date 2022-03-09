from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def demande_musique(request):
    musique = "tchoupi"
    dico = {"musique": musique}
    return JsonResponse(dico)
