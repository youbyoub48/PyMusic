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
    with open("friends.json", "r") as f:
        friends = json.load(f)

    with open("musique.json", "r") as f:
        dico_musique = json.load(f)

    chef = friends.get(pseudo)

    if chef is None:
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

def add_friends(request, pseudo=None, pseudo2=None):
    # sourcery skip: hoist-statement-from-if, swap-if-else-branches, use-named-expression

    if not os.path.exists("json/friends.json"):
        db_friends ={pseudo:[pseudo2]}

        with open("json/friends.json", "w") as f:
            json.dump(db_friends,f, indent=4)
        return HttpResponse("OK", request)

    else:
        with open("json/friends.json", "r") as f:
            db_friends = json.load(f)
        liste_friends = db_friends.get(pseudo, False)
        
        if not liste_friends:
            db_friends[pseudo] = [pseudo2]

        else:
            liste_friends.append(pseudo2)
            db_friends[pseudo] = liste_friends
               
        with open("json/friends.json", "w") as f:
            json.dump(db_friends, f, indent=4)

        return HttpResponse("OK", request)