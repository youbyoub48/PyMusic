import requests

def Ajout(pseudo, pseudo2):
    requests.get(f"http://51.91.251.170/api/get/ajout/pseudo={pseudo}&pseudo2={pseudo2}")
