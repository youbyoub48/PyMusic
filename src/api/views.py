from http.client import OK
from django import db
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, os


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

    return JsonResponse({musique: f"http://51.91.251.170:8080/{musique}.mp3"})

@csrf_exempt
def upload(request, pseudo=None):
    if request.method == "POST":
        lien = request.POST.get("lien")
        Convertir(lien)
        Trie(pseudo)
        return HttpResponse("OK", request)

def ajout_amis(request, pseudo=None, pseudo2=None):

    if not os.path.exists("json/amis.json"):
        db_amis ={pseudo:[pseudo2]}

        with open("json/amis.json", "w") as f:
            json.dump(db_amis,f, indent=4)
        return HttpResponse("OK", request)

    else:
        with open("json/amis.json", "r") as f:
            db_amis = json.load(f)
        liste_amis = db_amis.get(pseudo, False)
        
        if not liste_amis:
            print("marche1")
            db_amis[pseudo] = [pseudo2]

        else:
            print("marche2")
            liste_amis.append(pseudo2)
            db_amis[pseudo] = liste_amis
               
        with open("json/amis.json", "w") as f:
            json.dump(db_amis, f, indent=4)

        return HttpResponse("OK", request)