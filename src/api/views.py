from http.client import OK
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from convertisseur import Convertir
from trie import Trie

# Create your views here.

def demande_musique(request, pseudo=None):
    musique = "megalovania"
    lien = "http://localhost/Undertale_-_Megalovania%5bConConverter.com%5d.mp3"
    dico = {musique: lien}
    return JsonResponse(dico)

@csrf_exempt
def upload(request, pseudo=None):
    if request.method == "POST":
        print(pseudo)
        lien = request.POST.get("lien")
        print(lien)
        Convertir(lien)
        Trie(pseudo)
        return HttpResponse("OK", request)

def ajout_amis(request, pseudo=None, pseudo2=None):
    dico = {pseudo2:pseudo}
    with open("amis.json", "w") as f:
        json.dump(dico,f)
    return HttpResponse("OK", request)