from http.client import OK
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from convertisseur import Convertir
from trie import Trie

# Create your views here.

def demande_musique(request, pseudo=None):
    with open("amis.json", "r") as f:
        amis = json.load(f)
        
    with open("musique.json", "r") as f:
        dico_musique = json.load(f)

    chef = amis.get(pseudo)

    if chef == None:
        return HttpResponse("Faux", request)
    
    musique = dico_musique.get(chef)

    return JsonResponse({musique: f"http:51.91.251.170:8080/{musique}.mp3"})

@csrf_exempt
def upload(request, pseudo=None):
    if request.method == "POST":
        lien = request.POST.get("lien")
        Convertir(lien)
        Trie(pseudo)
        return HttpResponse("OK", request)

def ajout_amis(request, pseudo=None, pseudo2=None):
    dico = {pseudo2:pseudo}
    with open("amis.json", "w") as f:
        json.dump(dico,f)
    return HttpResponse("OK", request)