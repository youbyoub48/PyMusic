from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def demande_musique(request):
    musique = "megalovania"
    lien = "http://localhost/Undertale_-_Megalovania%5bConConverter.com%5d.mp3"
    dico = {musique: lien}
    return JsonResponse(dico)
